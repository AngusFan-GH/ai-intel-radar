from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Source:
    vendor_name: str | None
    type: str
    event_type: str
    region: str = "unknown"
    entity_type: str = "unknown"
    url: str | None = None
    repo: str | None = None
    author: str | None = None
    query: str | None = None
    name: str | None = None
    limit: int = 10


@dataclass(slots=True)
class Vendor:
    name: str
    region: str
    entity_type: str
    priority: str
    sources: list[Source] = field(default_factory=list)


@dataclass(slots=True)
class Event:
    title: str
    url: str
    source_name: str
    source_type: str
    discovered_at: datetime
    published_at: datetime | None = None
    summary: str | None = None
    vendor_name: str | None = None
    entity_type: str = "unknown"
    event_type: str = "unknown_ai_event"
    region: str = "unknown"
    is_open_source: bool = False
    github_repo: str | None = None
    github_stars: int | None = None
    tags: list[str] = field(default_factory=list)
    raw_payload: str | None = None
    score: float | None = None
