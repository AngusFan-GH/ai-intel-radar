from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

from .collectors.github import GitHubReleasesCollector, GitHubSearchCollector
from .collectors.html_news import HTMLNewsCollector
from .collectors.huggingface import HuggingFaceModelsCollector
from .collectors.rss import RSSCollector
from .db import load_sources, save_events
from .models import Event, Source


COLLECTORS = {
    "rss": RSSCollector(),
    "github_releases": GitHubReleasesCollector(),
    "github_search": GitHubSearchCollector(),
    "huggingface_models": HuggingFaceModelsCollector(),
    "html_news": HTMLNewsCollector(),
}


def run_collection(source_type: str | None = None) -> tuple[int, list[Event]]:
    sources = load_sources(source_type=source_type)
    events: list[Event] = []
    if not sources:
        return 0, events

    max_workers = max(1, min(_resolve_max_workers(), len(sources)))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(_collect_source, source): source
            for source in sources
            if COLLECTORS.get(source.type)
        }
        for future in as_completed(futures):
            events.extend(future.result())

    inserted = save_events([event for event in events if not event.url.startswith("error://")])
    return inserted, events


def _collect_source(source: Source) -> list[Event]:
    collector = COLLECTORS.get(source.type)
    if not collector:
        return []
    try:
        return collector.collect(source)
    except Exception as exc:
        return [
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
        ]


def _resolve_max_workers() -> int:
    raw = os.getenv("AI_INTEL_MAX_WORKERS", "8")
    try:
        return int(raw)
    except ValueError:
        return 8
