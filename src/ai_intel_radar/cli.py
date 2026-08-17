from __future__ import annotations

import argparse
from pathlib import Path

from .config import load_config
from .db import bootstrap_schema, fetch_unscored_events, update_scores, upsert_vendors
from .feishu import push_daily_summary
from .pipeline import run_collection
from .reporting import build_daily_report
from .scoring import score_event


def main() -> None:
    parser = argparse.ArgumentParser(prog="ai-intel-radar")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("bootstrap-db")
    subparsers.add_parser("sync-vendors")

    collect_parser = subparsers.add_parser("collect")
    collect_parser.add_argument(
        "--collector",
        choices=["rss", "github_releases", "github_search", "huggingface_models", "all"],
        default="all",
    )

    subparsers.add_parser("score")

    report_parser = subparsers.add_parser("report")
    report_parser.add_argument("--output-dir", default="reports")

    feishu_parser = subparsers.add_parser("push-feishu")
    feishu_parser.add_argument("--report-url", default=None)
    feishu_parser.add_argument("--limit", type=int, default=None)

    subparsers.add_parser("run-daily")

    args = parser.parse_args()

    if args.command == "bootstrap-db":
        bootstrap_schema()
        print("Database schema initialized.")
        return

    if args.command == "sync-vendors":
        vendors, discovery_sources = load_config()
        upsert_vendors(vendors, discovery_sources)
        print(f"Synced {len(vendors)} vendors and {len(discovery_sources)} discovery sources.")
        return

    if args.command == "collect":
        source_type = None if args.collector == "all" else args.collector
        inserted, events = run_collection(source_type=source_type)
        print(f"Collected {len(events)} events, inserted {inserted} new rows.")
        return

    if args.command == "score":
        rows = fetch_unscored_events()
        scored = [(row["url"], score_event(row)) for row in rows]
        update_scores(scored)
        print(f"Scored {len(scored)} events.")
        return

    if args.command == "report":
        report_path = build_daily_report(output_dir=Path(args.output_dir))
        print(f"Wrote report to {report_path}")
        return

    if args.command == "push-feishu":
        push_daily_summary(report_url=args.report_url, limit=args.limit)
        return

    if args.command == "run-daily":
        bootstrap_schema()
        vendors, discovery_sources = load_config()
        upsert_vendors(vendors, discovery_sources)
        inserted, events = run_collection()
        rows = fetch_unscored_events()
        scored = [(row["url"], score_event(row)) for row in rows]
        update_scores(scored)
        report_path = build_daily_report()
        push_daily_summary()
        print(
            f"Daily run complete. collected={len(events)} inserted={inserted} "
            f"scored={len(scored)} report={report_path}"
        )
        return
