from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from .db import fetch_recent_events


def build_daily_report(output_dir: Path = Path("reports")) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = fetch_recent_events(limit=60)

    today = datetime.now().strftime("%Y-%m-%d")
    report_path = output_dir / f"daily-report-{today}.md"

    sections = {
        "厂商新品": [],
        "新模型": [],
        "新开源项目": [],
        "其他观察": [],
    }

    for row in rows:
        line = _render_line(row)
        if row["event_type"] == "product_launch":
            sections["厂商新品"].append(line)
        elif row["event_type"] == "model_launch":
            sections["新模型"].append(line)
        elif row["event_type"] == "open_source_launch":
            sections["新开源项目"].append(line)
        else:
            sections["其他观察"].append(line)

    content = [f"# AI Intel Radar Daily Report ({today})", ""]
    for section_name, items in sections.items():
        if not items:
            continue
        content.append(f"## {section_name}")
        content.append("")
        content.extend(items[:15])
        content.append("")

    report_path.write_text("\n".join(content).strip() + "\n", encoding="utf-8")
    return report_path


def _render_line(row) -> str:
    tags = ", ".join(json.loads(row["tags_json"])) if row["tags_json"] else ""
    vendor = row["vendor_name"] or "unknown"
    score = f'{row["score"]:.2f}' if row["score"] is not None else "n/a"
    summary = (row["summary"] or "").replace("\n", " ").strip()
    summary = summary[:180]
    return f"- [{row['title']}]({row['url']}) | vendor={vendor} | score={score} | tags={tags} | {summary}"
