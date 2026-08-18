from __future__ import annotations

import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

from ..http import fetch_text
from ..models import Event, Source
from .base import Collector
from .rss import infer_tags


class HTMLNewsCollector(Collector):
    source_type = "html_news"

    def collect(self, source: Source) -> list[Event]:
        if not source.url:
            return []

        html = fetch_text(source.url)
        page = ParsedHTML.from_html(source.url, html)
        candidates = _build_candidates(source, page)
        if not candidates:
            return [_event_from_page(source, page)]

        article_limit = min(source.limit, len(candidates))
        results: list[Event] = []
        max_workers = min(4, article_limit)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(_fetch_candidate_event, source, candidate): candidate
                for candidate in candidates[:article_limit]
            }
            for future in as_completed(futures):
                event = future.result()
                if event:
                    results.append(event)
        results.sort(key=lambda event: event.published_at or event.discovered_at, reverse=True)
        return results


@dataclass(slots=True)
class Anchor:
    href: str
    text: str


@dataclass(slots=True)
class ParsedHTML:
    url: str
    title: str
    meta_title: str | None
    meta_description: str | None
    anchors: list[Anchor]
    headings: list[str]
    paragraphs: list[str]
    datetimes: list[str]

    @classmethod
    def from_html(cls, url: str, html: str) -> "ParsedHTML":
        parser = _HTMLPageParser(base_url=url)
        parser.feed(html)
        parser.close()
        return cls(
            url=url,
            title=parser.title.strip(),
            meta_title=parser.meta_title.strip() or None,
            meta_description=parser.meta_description.strip() or None,
            anchors=parser.anchors,
            headings=[value.strip() for value in parser.headings if value.strip()],
            paragraphs=[value.strip() for value in parser.paragraphs if value.strip()],
            datetimes=[value.strip() for value in parser.datetimes if value.strip()],
        )


class _HTMLPageParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.title = ""
        self.meta_title = ""
        self.meta_description = ""
        self.anchors: list[Anchor] = []
        self.headings: list[str] = []
        self.paragraphs: list[str] = []
        self.datetimes: list[str] = []
        self._in_title = False
        self._active_anchor: dict[str, str] | None = None
        self._collect_tag: str | None = None
        self._text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        attr_map = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = (attr_map.get("name") or attr_map.get("property") or "").lower()
            content = attr_map.get("content", "")
            if name in {"description", "og:description", "twitter:description"} and content:
                if not self.meta_description:
                    self.meta_description = content
            if name in {"og:title", "twitter:title"} and content:
                if not self.meta_title:
                    self.meta_title = content
        elif tag == "a":
            href = attr_map.get("href", "").strip()
            if href:
                self._active_anchor = {"href": urljoin(self.base_url, href), "text": ""}
        elif tag in {"h1", "h2", "h3", "p"}:
            self._collect_tag = tag
            self._text_parts = []
        elif tag == "time":
            value = attr_map.get("datetime", "").strip()
            if value:
                self.datetimes.append(value)

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        if self._active_anchor is not None:
            self._active_anchor["text"] += data
        if self._collect_tag:
            self._text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == "a" and self._active_anchor is not None:
            text = " ".join(self._active_anchor["text"].split())
            self.anchors.append(Anchor(href=self._active_anchor["href"], text=text))
            self._active_anchor = None
        elif tag == self._collect_tag and self._collect_tag is not None:
            text = " ".join("".join(self._text_parts).split())
            if text:
                if self._collect_tag in {"h1", "h2", "h3"}:
                    self.headings.append(text)
                elif self._collect_tag == "p":
                    self.paragraphs.append(text)
            self._collect_tag = None
            self._text_parts = []


def _build_candidates(source: Source, page: ParsedHTML) -> list[Anchor]:
    pattern = re.compile(source.query, re.IGNORECASE) if source.query else None
    base_host = urlparse(source.url or "").netloc
    chosen: list[Anchor] = []
    seen: set[str] = set()
    for anchor in page.anchors:
        if not anchor.text or len(anchor.text) < 8:
            continue
        if not _is_allowed_link(anchor.href, base_host):
            continue
        haystack = f"{anchor.href} {anchor.text}"
        if pattern and not pattern.search(haystack):
            continue
        if _looks_like_navigation(anchor.href, anchor.text):
            continue
        if anchor.href in seen:
            continue
        seen.add(anchor.href)
        chosen.append(anchor)
    return chosen


def _fetch_candidate_event(source: Source, candidate: Anchor) -> Event | None:
    try:
        html = fetch_text(candidate.href)
    except Exception:
        return None
    page = ParsedHTML.from_html(candidate.href, html)
    title = page.meta_title or page.title or candidate.text
    summary = _pick_summary(page) or candidate.text
    tags = sorted(set(infer_tags(title, summary)))
    published_at = _pick_published_at(page, summary)
    return Event(
        title=title,
        url=candidate.href,
        summary=summary[:400] if summary else None,
        source_name=source.vendor_name or source.name or source.url or "html_news",
        source_type=source.type,
        discovered_at=datetime.now(timezone.utc),
        published_at=published_at,
        vendor_name=source.vendor_name,
        entity_type=source.entity_type,
        event_type=_infer_event_type(source.event_type, title, summary),
        region=source.region,
        is_open_source=False,
        tags=tags,
        raw_payload=json.dumps(
            {
                "title": page.title,
                "meta_title": page.meta_title,
                "meta_description": page.meta_description,
                "headings": page.headings[:6],
                "paragraphs": page.paragraphs[:4],
            },
            ensure_ascii=True,
        ),
    )


def _event_from_page(source: Source, page: ParsedHTML) -> Event:
    title = page.meta_title or page.title or (source.vendor_name or source.name or source.url or "HTML page update")
    summary = _pick_summary(page)
    return Event(
        title=title,
        url=page.url,
        summary=summary[:400] if summary else None,
        source_name=source.vendor_name or source.name or page.url,
        source_type=source.type,
        discovered_at=datetime.now(timezone.utc),
        published_at=_pick_published_at(page, summary or ""),
        vendor_name=source.vendor_name,
        entity_type=source.entity_type,
        event_type=_infer_event_type(source.event_type, title, summary),
        region=source.region,
        is_open_source=False,
        tags=sorted(set(infer_tags(title, summary))),
        raw_payload=json.dumps(
            {
                "title": page.title,
                "meta_title": page.meta_title,
                "meta_description": page.meta_description,
                "headings": page.headings[:6],
                "paragraphs": page.paragraphs[:4],
            },
            ensure_ascii=True,
        ),
    )


def _pick_summary(page: ParsedHTML) -> str | None:
    if page.meta_description:
        return page.meta_description
    for paragraph in page.paragraphs:
        if len(paragraph) >= 40:
            return paragraph
    if page.headings:
        return page.headings[0]
    return None


def _pick_published_at(page: ParsedHTML, summary: str | None) -> datetime | None:
    candidates = list(page.datetimes)
    if summary:
        match = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", summary)
        if match:
            candidates.append(match.group(1))
    for heading in page.headings[:3]:
        match = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", heading)
        if match:
            candidates.append(match.group(1))
    for value in candidates:
        parsed = _parse_datetime(value)
        if parsed:
            return parsed
    return None


def _parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.strip().replace("Z", "+00:00")
    for candidate in (normalized, normalized[:10]):
        try:
            parsed = datetime.fromisoformat(candidate)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.astimezone(timezone.utc)
        except ValueError:
            continue
    return None


def _is_allowed_link(url: str, base_host: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return False
    if parsed.netloc != base_host:
        return False
    if parsed.fragment:
        return False
    if any(parsed.path.lower().endswith(ext) for ext in (".css", ".js", ".png", ".jpg", ".svg", ".ico", ".mp4", ".pdf")):
        return False
    return True


def _looks_like_navigation(url: str, text: str) -> bool:
    corpus = f"{url} {text}".lower()
    noise = (
        "privacy",
        "terms",
        "careers",
        "contact",
        "home",
        "research",
        "products",
        "about",
        "download",
        "documentation",
        "developer",
        "support",
        "page/",
        "all-news",
        "newsroom",
        "view_from",
    )
    return any(token in corpus for token in noise)


def _infer_event_type(default: str, title: str, summary: str | None) -> str:
    corpus = f"{title} {summary or ''}".lower()
    if any(token in corpus for token in ("model", "reasoning", "llm", "vlm", "multimodal", "audio model")):
        return "model_launch"
    if any(token in corpus for token in ("api", "platform", "agent", "studio", "launch", "release", "available", "update")):
        return default
    return default
