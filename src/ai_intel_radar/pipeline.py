from __future__ import annotations

from datetime import datetime, timezone

from .collectors.github import GitHubReleasesCollector, GitHubSearchCollector
from .collectors.huggingface import HuggingFaceModelsCollector
from .collectors.rss import RSSCollector
from .db import load_sources, save_events
from .models import Event, Source


COLLECTORS = {
    "rss": RSSCollector(),
    "github_releases": GitHubReleasesCollector(),
    "github_search": GitHubSearchCollector(),
    "huggingface_models": HuggingFaceModelsCollector(),
}


def run_collection(source_type: str | None = None) -> tuple[int, list[Event]]:
    sources = load_sources(source_type=source_type)
    events: list[Event] = []
    for source in sources:
        collector = COLLECTORS.get(source.type)
        if not collector:
            continue
        try:
            events.extend(collector.collect(source))
        except Exception as exc:
            events.append(
                Event(
                    title=f"Collection error for {source.type}",
                    url=f"error://{source.type}/{source.vendor_name or source.name or 'unknown'}",
                    summary=str(exc),
                    source_name=source.vendor_name or source.name or source.type,
                    source_type=source.type,
                    discovered_at=datetime.now(timezone.utc),
                    vendor_name=source.vendor_name,
                    entity_type="system",
                    event_type="unknown_ai_event",
                    region="unknown",
                    is_open_source=False,
                    tags=["error"],
                )
            )
    inserted = save_events([event for event in events if not event.url.startswith("error://")])
    return inserted, events
