from __future__ import annotations

import hashlib
import json
import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

from .models import Event, Source, Vendor


DEFAULT_DB_PATH = Path("data/ai_intel_radar.sqlite3")


def resolve_db_path() -> Path:
    configured = os.getenv("AI_INTEL_DB_PATH")
    return Path(configured) if configured else DEFAULT_DB_PATH


@contextmanager
def get_connection(db_path: Path | None = None) -> Iterator[sqlite3.Connection]:
    path = db_path or resolve_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()


def bootstrap_schema(db_path: Path | None = None) -> None:
    with get_connection(db_path) as connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS vendors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                region TEXT NOT NULL,
                entity_type TEXT NOT NULL,
                priority TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS sources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_key TEXT NOT NULL UNIQUE,
                vendor_name TEXT,
                type TEXT NOT NULL,
                event_type TEXT NOT NULL,
                region TEXT NOT NULL,
                entity_type TEXT NOT NULL,
                url TEXT,
                repo TEXT,
                author TEXT,
                query_text TEXT,
                name TEXT,
                limit_count INTEGER NOT NULL DEFAULT 10,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE,
                summary TEXT,
                source_name TEXT NOT NULL,
                source_type TEXT NOT NULL,
                vendor_name TEXT,
                entity_type TEXT NOT NULL,
                event_type TEXT NOT NULL,
                region TEXT NOT NULL,
                is_open_source INTEGER NOT NULL,
                github_repo TEXT,
                github_stars INTEGER,
                tags_json TEXT NOT NULL,
                raw_payload TEXT,
                published_at TEXT,
                discovered_at TEXT NOT NULL,
                score REAL
            );
            """
        )
        _ensure_column(connection, "sources", "limit_count", "INTEGER NOT NULL DEFAULT 10")
        connection.commit()


def upsert_vendors(vendors: list[Vendor], discovery_sources: list[Source], db_path: Path | None = None) -> None:
    now = datetime.now(timezone.utc).isoformat()
    with get_connection(db_path) as connection:
        for vendor in vendors:
            connection.execute(
                """
                INSERT INTO vendors(name, region, entity_type, priority, updated_at)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(name) DO UPDATE SET
                    region = excluded.region,
                    entity_type = excluded.entity_type,
                    priority = excluded.priority,
                    updated_at = excluded.updated_at
                """,
                (vendor.name, vendor.region, vendor.entity_type, vendor.priority, now),
            )
            for source in vendor.sources:
                _upsert_source(connection, source, now)

        for source in discovery_sources:
            _upsert_source(connection, source, now)

        connection.commit()


def _upsert_source(connection: sqlite3.Connection, source: Source, now: str) -> None:
    source_key = _source_key(source)
    connection.execute(
        """
        INSERT INTO sources(source_key, vendor_name, type, event_type, region, entity_type, url, repo, author, query_text, name, limit_count, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(source_key)
        DO UPDATE SET
            event_type = excluded.event_type,
            region = excluded.region,
            entity_type = excluded.entity_type,
            limit_count = excluded.limit_count,
            updated_at = excluded.updated_at
        """,
        (
            source_key,
            source.vendor_name,
            source.type,
            source.event_type,
            source.region,
            source.entity_type,
            source.url,
            source.repo,
            source.author,
            source.query,
            source.name,
            source.limit,
            now,
        ),
    )


def load_sources(source_type: str | None = None, db_path: Path | None = None) -> list[Source]:
    with get_connection(db_path) as connection:
        if source_type:
            rows = connection.execute(
                "SELECT vendor_name, type, event_type, region, entity_type, url, repo, author, query_text, name, limit_count FROM sources WHERE type = ?",
                (source_type,),
            ).fetchall()
        else:
            rows = connection.execute(
                "SELECT vendor_name, type, event_type, region, entity_type, url, repo, author, query_text, name, limit_count FROM sources"
            ).fetchall()
    return [
        Source(
            vendor_name=row["vendor_name"],
            type=row["type"],
            event_type=row["event_type"],
            region=row["region"],
            entity_type=row["entity_type"],
            url=row["url"],
            repo=row["repo"],
            author=row["author"],
            query=row["query_text"],
            name=row["name"],
            limit=row["limit_count"],
        )
        for row in rows
    ]


def save_events(events: list[Event], db_path: Path | None = None) -> int:
    inserted = 0
    with get_connection(db_path) as connection:
        for event in events:
            cursor = connection.execute(
                """
                INSERT OR IGNORE INTO events(
                    title, url, summary, source_name, source_type, vendor_name, entity_type,
                    event_type, region, is_open_source, github_repo, github_stars, tags_json,
                    raw_payload, published_at, discovered_at, score
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    event.title,
                    event.url,
                    event.summary,
                    event.source_name,
                    event.source_type,
                    event.vendor_name,
                    event.entity_type,
                    event.event_type,
                    event.region,
                    int(event.is_open_source),
                    event.github_repo,
                    event.github_stars,
                    json.dumps(event.tags, ensure_ascii=True),
                    event.raw_payload,
                    event.published_at.isoformat() if event.published_at else None,
                    event.discovered_at.isoformat(),
                    event.score,
                ),
            )
            inserted += cursor.rowcount
        connection.commit()
    return inserted


def fetch_recent_events(limit: int = 100, db_path: Path | None = None) -> list[sqlite3.Row]:
    with get_connection(db_path) as connection:
        return connection.execute(
            """
            SELECT *
            FROM events
            ORDER BY COALESCE(score, 0) DESC, COALESCE(published_at, discovered_at) DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()


def fetch_events_by_type(event_type: str, limit: int = 20, db_path: Path | None = None) -> list[sqlite3.Row]:
    with get_connection(db_path) as connection:
        return connection.execute(
            """
            SELECT *
            FROM events
            WHERE event_type = ?
            ORDER BY COALESCE(score, 0) DESC, COALESCE(published_at, discovered_at) DESC
            LIMIT ?
            """,
            (event_type, limit),
        ).fetchall()


def fetch_event_counts(db_path: Path | None = None) -> dict[str, int]:
    with get_connection(db_path) as connection:
        rows = connection.execute(
            "SELECT event_type, COUNT(*) AS count FROM events GROUP BY event_type"
        ).fetchall()
    return {row["event_type"]: row["count"] for row in rows}


def update_scores(scored_events: list[tuple[str, float]], db_path: Path | None = None) -> None:
    with get_connection(db_path) as connection:
        connection.executemany(
            "UPDATE events SET score = ? WHERE url = ?",
            [(score, url) for url, score in scored_events],
        )
        connection.commit()


def fetch_unscored_events(db_path: Path | None = None) -> list[sqlite3.Row]:
    with get_connection(db_path) as connection:
        return connection.execute("SELECT * FROM events WHERE score IS NULL").fetchall()


def _source_key(source: Source) -> str:
    raw = "|".join(
        [
            source.vendor_name or "",
            source.type,
            source.url or "",
            source.repo or "",
            source.author or "",
            source.query or "",
            source.name or "",
        ]
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _ensure_column(connection: sqlite3.Connection, table: str, column: str, ddl: str) -> None:
    rows = connection.execute(f"PRAGMA table_info({table})").fetchall()
    if any(row["name"] == column for row in rows):
        return
    connection.execute(f"ALTER TABLE {table} ADD COLUMN {column} {ddl}")
