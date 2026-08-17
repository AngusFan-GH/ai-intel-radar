from __future__ import annotations

import os
import tomllib
from pathlib import Path

from .models import Source, Vendor


DEFAULT_CONFIG_PATH = Path("config/vendors.toml")


def resolve_config_path() -> Path:
    configured = os.getenv("AI_INTEL_CONFIG_PATH")
    return Path(configured) if configured else DEFAULT_CONFIG_PATH


def load_config(path: Path | None = None) -> tuple[list[Vendor], list[Source]]:
    config_path = path or resolve_config_path()
    payload = tomllib.loads(config_path.read_text(encoding="utf-8"))

    vendors: list[Vendor] = []
    for item in payload.get("vendor", []):
        sources = [
            Source(
                vendor_name=item["name"],
                type=source["type"],
                event_type=source["event_type"],
                region=item["region"],
                entity_type=item["entity_type"],
                url=source.get("url"),
                repo=source.get("repo"),
                author=source.get("author"),
                query=source.get("query"),
                name=source.get("name"),
            )
            for source in item.get("source", [])
        ]
        vendors.append(
            Vendor(
                name=item["name"],
                region=item["region"],
                entity_type=item["entity_type"],
                priority=item["priority"],
                sources=sources,
            )
        )

    discovery_sources = [
        Source(
            vendor_name=None,
            type=source["type"],
            event_type=source["event_type"],
            region="unknown",
            entity_type="unknown",
            url=source.get("url"),
            repo=source.get("repo"),
            author=source.get("author"),
            query=source.get("query"),
            name=source.get("name"),
        )
        for source in payload.get("discovery_source", [])
    ]
    return vendors, discovery_sources
