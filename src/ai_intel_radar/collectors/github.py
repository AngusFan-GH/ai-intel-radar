from __future__ import annotations

import json
from datetime import datetime, timezone
from urllib.parse import quote_plus

from ..http import fetch_json
from ..models import Event, Source
from .base import Collector
from .rss import infer_tags


class GitHubReleasesCollector(Collector):
    source_type = "github_releases"

    def collect(self, source: Source) -> list[Event]:
        if not source.repo:
            return []
        releases = fetch_json(f"https://api.github.com/repos/{source.repo}/releases?per_page=5")
        if not isinstance(releases, list):
            return []
        events: list[Event] = []
        for release in releases:
            title = release.get("name") or release.get("tag_name") or f"Release for {source.repo}"
            body = release.get("body") or ""
            published_at = _parse_datetime(release.get("published_at"))
            events.append(
                Event(
                    title=f"{source.repo}: {title}",
                    url=release["html_url"],
                    summary=body[:400].strip() or None,
                    source_name=source.vendor_name or source.repo,
                    source_type=source.type,
                    discovered_at=datetime.now(timezone.utc),
                    published_at=published_at,
                    vendor_name=source.vendor_name,
                    entity_type=source.entity_type,
                    event_type=source.event_type,
                    region=source.region,
                    is_open_source=True,
                    github_repo=source.repo,
                    github_stars=None,
                    tags=infer_tags(title, body),
                    raw_payload=json.dumps(release, ensure_ascii=True),
                )
            )
        return events


class GitHubSearchCollector(Collector):
    source_type = "github_search"

    def collect(self, source: Source) -> list[Event]:
        if not source.query:
            return []
        payload = fetch_json(
            "https://api.github.com/search/repositories",
            params={
                "q": source.query,
                "sort": "updated",
                "order": "desc",
                "per_page": "10",
            },
        )
        items = payload.get("items", []) if isinstance(payload, dict) else []
        events: list[Event] = []
        for item in items:
            summary = item.get("description") or ""
            full_name = item["full_name"]
            events.append(
                Event(
                    title=f"{full_name} is trending",
                    url=item["html_url"],
                    summary=summary[:400] or None,
                    source_name=source.name or "github_search",
                    source_type=source.type,
                    discovered_at=datetime.now(timezone.utc),
                    published_at=_parse_datetime(item.get("updated_at")),
                    vendor_name=item["owner"]["login"],
                    entity_type="unknown",
                    event_type=source.event_type,
                    region="unknown",
                    is_open_source=True,
                    github_repo=full_name,
                    github_stars=item.get("stargazers_count"),
                    tags=infer_tags(full_name, summary),
                    raw_payload=json.dumps(item, ensure_ascii=True),
                )
            )
        return events


def _parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
