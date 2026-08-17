from __future__ import annotations

import json
from datetime import datetime, timezone

from ..http import fetch_json
from ..models import Event, Source
from .base import Collector
from .rss import infer_tags


class HuggingFaceModelsCollector(Collector):
    source_type = "huggingface_models"

    def collect(self, source: Source) -> list[Event]:
        params = {"limit": "10", "sort": "lastModified", "direction": "-1"}
        if source.author:
            params["author"] = source.author
        if source.query:
            params["search"] = source.query
        items = fetch_json("https://huggingface.co/api/models", params=params)
        if not isinstance(items, list):
            return []

        events: list[Event] = []
        for item in items:
            model_id = item.get("id")
            if not model_id:
                continue
            tags = list(item.get("tags", []))
            events.append(
                Event(
                    title=f"{model_id} updated",
                    url=f"https://huggingface.co/{model_id}",
                    summary=_summary_from_item(item),
                    source_name=source.vendor_name or source.name or "huggingface",
                    source_type=source.type,
                    discovered_at=datetime.now(timezone.utc),
                    published_at=_parse_datetime(item.get("lastModified")),
                    vendor_name=source.vendor_name or item.get("author"),
                    entity_type=source.entity_type if source.vendor_name else "unknown",
                    event_type=source.event_type,
                    region=source.region,
                    is_open_source=bool(item.get("private") is False),
                    github_repo=None,
                    github_stars=item.get("likes"),
                    tags=sorted(set(tags + infer_tags(model_id, " ".join(tags)))),
                    raw_payload=json.dumps(item, ensure_ascii=True),
                )
            )
        return events


def _summary_from_item(item: dict) -> str:
    tags = ", ".join(item.get("tags", [])[:6])
    downloads = item.get("downloads")
    likes = item.get("likes")
    return f"tags={tags}; downloads={downloads}; likes={likes}"


def _parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
