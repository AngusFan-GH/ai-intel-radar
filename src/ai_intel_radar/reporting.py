from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from .db import fetch_event_counts, fetch_events_by_type, fetch_recent_events


def build_daily_report(output_dir: Path = Path("reports")) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    section_rows = {
        "厂商新品": fetch_events_by_type("product_launch", limit=10),
        "新模型": fetch_events_by_type("model_launch", limit=10),
        "新开源项目": fetch_events_by_type("open_source_launch", limit=15),
        "其他观察": fetch_recent_events(limit=12),
    }

    today = datetime.now().strftime("%Y-%m-%d")
    report_path = output_dir / f"daily-report-{today}.md"
    counts = fetch_event_counts()
    sections: dict[str, list[str]] = {}
    for section_name, rows in section_rows.items():
        unique_rows = _dedupe_rows(rows)
        if section_name == "其他观察":
            unique_rows = [
                row for row in unique_rows if row["event_type"] not in {"product_launch", "model_launch", "open_source_launch"}
            ]
        sections[section_name] = [_render_line(row) for row in unique_rows]

    total = sum(counts.values())
    content = [f"# AI 情报雷达日报（{today}）", ""]
    content.append(f"当前事件池累计 {total} 条记录。日报按类别单独选取，避免开源项目把产品和模型事件淹没。")
    content.append("")
    content.append(
        "数据概况："
        f" 厂商新品 {counts.get('product_launch', 0)} 条；"
        f" 新模型 {counts.get('model_launch', 0)} 条；"
        f" 新开源项目 {counts.get('open_source_launch', 0)} 条。"
    )
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
    payload = _parse_payload(row["raw_payload"])
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
    what_it_is = _describe_what_it_is(row, payload)
    why_it_matters = _describe_why_it_matters(row, payload)
    lines = [f"- [{row['title']}]({row['url']})"]
    lines.append(f"  - 中文说明：{brief}")
    lines.append(f"  - 它是做什么的：{what_it_is}")
    if why_it_matters:
        lines.append(f"  - 值得关注的原因：{why_it_matters}")
    if summary:
        lines.append(f"  - 原文摘要：{summary}")
    return "\n".join(lines)


def _dedupe_rows(rows) -> list:
    seen: set[str] = set()
    result = []
    for row in rows:
        if row["url"] in seen:
            continue
        seen.add(row["url"])
        result.append(row)
    return result


def _parse_payload(raw_payload: str | None) -> dict:
    if not raw_payload:
        return {}
    try:
        payload = json.loads(raw_payload)
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def _describe_what_it_is(row, payload: dict) -> str:
    if row["source_type"] == "github_search":
        description = payload.get("description") or row["summary"]
        repo = row["github_repo"] or payload.get("full_name") or row["title"]
        language = payload.get("language")
        if description and language:
            return f"`{repo}` 是一个以 {language} 为主的项目，定位是：{_trim_sentence(description, 120)}"
        if description:
            return f"`{repo}` 的定位是：{_trim_sentence(description, 120)}"
        return f"`{repo}` 是新近活跃的开源项目，当前需要进一步补充项目说明。"

    if row["source_type"] == "github_releases":
        repo = row["github_repo"] or row["title"]
        return f"这是 `{repo}` 的新版本发布事件，表示该项目在最近继续演进并发布了可用更新。"

    if row["source_type"] == "huggingface_models":
        model_name = row["title"].replace(" updated", "")
        summary = row["summary"] or ""
        return f"`{model_name}` 是近期更新的模型条目。{_trim_sentence(summary, 120)}"

    if row["source_type"] == "rss":
        summary = row["summary"] or row["title"]
        return f"这是官方发布源中的一条更新，核心内容是：{_trim_sentence(summary, 120)}"

    return _trim_sentence(row["summary"] or row["title"], 120)


def _describe_why_it_matters(row, payload: dict) -> str:
    reasons: list[str] = []
    if row["github_stars"]:
        reasons.append(f"当前记录到约 {row['github_stars']} 个 GitHub stars")
    if row["source_type"] == "github_search":
        reasons.append("进入了 GitHub 发现流，说明近期活跃度或关注度较高")
    if row["source_type"] == "rss":
        reasons.append("来自官方发布源，可信度较高")
    if row["source_type"] == "huggingface_models":
        reasons.append("进入模型跟踪范围，适合后续观察能力和生态反馈")
    published = row["published_at"] or row["discovered_at"]
    if published:
        try:
            dt = datetime.fromisoformat(published)
            age_hours = max((datetime.now(UTC) - dt).total_seconds() / 3600, 0)
            if age_hours <= 24:
                reasons.append("属于近 24 小时内的新鲜事件")
        except ValueError:
            pass
    return "；".join(reasons)


def _trim_sentence(value: str, limit: int) -> str:
    text = " ".join(value.split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


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
