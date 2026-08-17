from __future__ import annotations

from datetime import datetime, timezone


def score_event(row: dict) -> float:
    score = 0.0

    if row["source_type"] in {"rss", "github_releases", "huggingface_models"}:
        score += 25
    if row["vendor_name"]:
        score += 10
    if row["event_type"] == "model_launch":
        score += 18
    elif row["event_type"] == "product_launch":
        score += 16
    elif row["event_type"] == "open_source_launch":
        score += 14

    if row["is_open_source"]:
        score += 12

    stars = row["github_stars"] or 0
    score += min(stars / 20, 20)

    published_at = row["published_at"] or row["discovered_at"]
    if published_at:
        try:
            published = datetime.fromisoformat(published_at)
            age_hours = max((datetime.now(timezone.utc) - published).total_seconds() / 3600, 0)
            score += max(20 - min(age_hours / 6, 20), 0)
        except ValueError:
            pass

    return round(score, 2)
