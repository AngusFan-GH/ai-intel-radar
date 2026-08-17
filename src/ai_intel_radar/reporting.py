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

    total = sum(len(items) for items in sections.values())
    content = [f"# AI 情报雷达日报（{today}）", ""]
    content.append(f"共整理 {total} 条事件，按“厂商新品 / 新模型 / 新开源项目 / 其他观察”分类展示。")
    content.append("")
    for section_name, items in sections.items():
        if not items:
            continue
        content.append(f"## {section_name}（{len(items)}）")
        content.append("")
        content.extend(items[:15])
        content.append("")

    report_path.write_text("\n".join(content).strip() + "\n", encoding="utf-8")
    return report_path


def _render_line(row) -> str:
    tags = [_tag_label(tag) for tag in json.loads(row["tags_json"])] if row["tags_json"] else []
    vendor = row["vendor_name"] or "未知主体"
    score = f'{row["score"]:.2f}' if row["score"] is not None else "n/a"
    summary = (row["summary"] or "").replace("\n", " ").strip()
    summary = summary[:180]
    tags_display = "、".join(tags) if tags else "未打标签"
    event_label = _event_label(row["event_type"])
    source_label = _source_label(row["source_type"])
    brief = (
        f"主体：{vendor}；事件类型：{event_label}；来源：{source_label}；"
        f"评分：{score}；标签：{tags_display}。"
    )
    if summary:
        return f"- [{row['title']}]({row['url']})\n  - 中文说明：{brief}\n  - 原文摘要：{summary}"
    return f"- [{row['title']}]({row['url']})\n  - 中文说明：{brief}"


def _event_label(value: str) -> str:
    mapping = {
        "product_launch": "产品发布",
        "model_launch": "模型发布",
        "open_source_launch": "开源项目发布",
        "release_update": "版本更新",
        "unknown_ai_event": "一般事件",
    }
    return mapping.get(value, value)


def _source_label(value: str) -> str:
    mapping = {
        "rss": "官方资讯源",
        "github_releases": "GitHub Release",
        "github_search": "GitHub 发现流",
        "huggingface_models": "Hugging Face 模型流",
    }
    return mapping.get(value, value)


def _tag_label(value: str) -> str:
    mapping = {
        "agent": "Agent",
        "coding": "编程",
        "image": "图像",
        "video": "视频",
        "voice": "语音",
        "multimodal": "多模态",
        "reasoning": "推理",
        "infra": "基础设施",
        "china": "中国",
    }
    return mapping.get(value, value)
