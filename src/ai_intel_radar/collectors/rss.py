from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

from ..http import fetch_text
from ..models import Event, Source
from .base import Collector


class RSSCollector(Collector):
    source_type = "rss"

    def collect(self, source: Source) -> list[Event]:
        if not source.url:
            return []
        xml_payload = fetch_text(source.url)
        root = ET.fromstring(xml_payload)
        items = root.findall(".//item")
        entries = root.findall(".//{http://www.w3.org/2005/Atom}entry")
        events: list[Event] = []

        if items:
            for item in items[:10]:
                title = _text(item, "title")
                link = _text(item, "link")
                summary = _sanitize(_text(item, "description"))
                published_at = _parse_datetime(_text(item, "pubDate"))
                events.append(
                    _event_from_source(
                        source=source,
                        title=title,
                        link=link,
                        summary=summary,
                        published_at=published_at,
                    )
                )
        else:
            for entry in entries[:10]:
                title = _text(entry, "{http://www.w3.org/2005/Atom}title")
                link = ""
                for child in entry.findall("{http://www.w3.org/2005/Atom}link"):
                    if child.attrib.get("href"):
                        link = child.attrib["href"]
                        break
                summary = _sanitize(
                    _text(entry, "{http://www.w3.org/2005/Atom}summary")
                    or _text(entry, "{http://www.w3.org/2005/Atom}content")
                )
                published_at = _parse_datetime(
                    _text(entry, "{http://www.w3.org/2005/Atom}updated")
                    or _text(entry, "{http://www.w3.org/2005/Atom}published")
                )
                events.append(
                    _event_from_source(
                        source=source,
                        title=title,
                        link=link,
                        summary=summary,
                        published_at=published_at,
                    )
                )
        return [event for event in events if event.title and event.url]


def _event_from_source(source: Source, title: str, link: str, summary: str | None, published_at: datetime | None) -> Event:
    tags = infer_tags(title=title, summary=summary)
    return Event(
        title=title,
        url=link,
        summary=summary,
        source_name=source.vendor_name or source.name or link,
        source_type=source.type,
        discovered_at=datetime.now(timezone.utc),
        published_at=published_at,
        vendor_name=source.vendor_name,
        entity_type=source.entity_type,
        event_type=_infer_event_type(source.event_type, title, summary),
        region=source.region,
        is_open_source="github" in (summary or "").lower() or "open source" in (summary or "").lower(),
        tags=tags,
        raw_payload=None,
    )


def infer_tags(title: str, summary: str | None) -> list[str]:
    corpus = f"{title} {summary or ''}".lower()
    tag_rules = {
        "agent": ["agent", "agents"],
        "coding": ["code", "coding", "developer"],
        "image": ["image", "diffusion"],
        "video": ["video"],
        "voice": ["voice", "speech", "audio"],
        "multimodal": ["multimodal"],
        "reasoning": ["reasoning"],
        "infra": ["inference", "deployment", "api", "infrastructure"],
        "china": ["china", "chinese"],
    }
    return [tag for tag, patterns in tag_rules.items() if any(pattern in corpus for pattern in patterns)]


def _infer_event_type(default: str, title: str, summary: str | None) -> str:
    corpus = f"{title} {summary or ''}".lower()
    if any(token in corpus for token in ("model", "checkpoint", "weights")):
        return "model_launch"
    if any(token in corpus for token in ("appoint", "chief revenue officer", "letter", "governor", "case study")):
        return "unknown_ai_event"
    if any(token in corpus for token in ("release", "launch", "available", "introducing", "announcing", "preview", "service tier", "ads in chatgpt")):
        return default
    if any(token in corpus for token in ("guide", "how enterprises", "how ", "builds ai-native")):
        return "unknown_ai_event"
    return "unknown_ai_event"


def _text(node: ET.Element, selector: str) -> str:
    found = node.find(selector)
    return (found.text or "").strip() if found is not None and found.text else ""


def _sanitize(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def _parse_datetime(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return parsedate_to_datetime(value).astimezone(timezone.utc)
    except (TypeError, ValueError):
        pass
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None
