from __future__ import annotations

import html
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
    markdown_path = output_dir / f"daily-report-{today}.md"
    html_path = output_dir / f"daily-report-{today}.html"
    counts = fetch_event_counts()
    sections: dict[str, list[dict]] = {}
    for section_name, rows in section_rows.items():
        unique_rows = _dedupe_rows(rows)
        if section_name == "其他观察":
            unique_rows = [
                row for row in unique_rows if row["event_type"] not in {"product_launch", "model_launch", "open_source_launch"}
            ]
        sections[section_name] = [_build_item(row) for row in unique_rows]

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
        content.extend(_render_markdown_item(item) for item in items[:15])
        content.append("")

    markdown_path.write_text("\n".join(content).strip() + "\n", encoding="utf-8")
    html_path.write_text(_render_html_report(today, total, counts, sections), encoding="utf-8")
    return markdown_path


def _build_item(row) -> dict:
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
    return {
        "title": row["title"],
        "url": row["url"],
        "brief": brief,
        "what_it_is": what_it_is,
        "why_it_matters": why_it_matters,
        "summary": summary,
        "vendor": vendor,
        "score": score,
        "event_label": event_label,
        "source_label": source_label,
        "tags": tags,
    }


def _render_markdown_item(item: dict) -> str:
    lines = [f"- [{item['title']}]({item['url']})"]
    lines.append(f"  - 中文说明：{item['brief']}")
    lines.append(f"  - 它是做什么的：{item['what_it_is']}")
    if item["why_it_matters"]:
        lines.append(f"  - 值得关注的原因：{item['why_it_matters']}")
    if item["summary"]:
        lines.append(f"  - 原文摘要：{item['summary']}")
    return "\n".join(lines)


def _render_html_report(today: str, total: int, counts: dict[str, int], sections: dict[str, list[dict]]) -> str:
    stats = [
        ("厂商新品", counts.get("product_launch", 0), "追踪官方产品与平台更新"),
        ("新模型", counts.get("model_launch", 0), "追踪模型发布、更新与上架"),
        ("新开源项目", counts.get("open_source_launch", 0), "追踪 GitHub 与开放生态信号"),
    ]
    stat_html = "\n".join(
        f"""
        <article class="stat-card">
          <p class="stat-label">{html.escape(label)}</p>
          <p class="stat-value">{value}</p>
          <p class="stat-note">{html.escape(note)}</p>
        </article>
        """
        for label, value, note in stats
    )
    sections_html = "\n".join(
        _render_html_section(section_name, items)
        for section_name, items in sections.items()
        if items
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>AI 情报雷达日报 {html.escape(today)}</title>
    <style>
      :root {{
        --bg: #f6f2e8;
        --surface: rgba(255, 251, 245, 0.84);
        --surface-strong: #fffaf2;
        --ink: #1a1814;
        --muted: #655f56;
        --line: rgba(38, 33, 26, 0.12);
        --accent: #0057ff;
        --accent-soft: #d9e5ff;
        --warm: #d86a31;
        --shadow: 0 18px 50px rgba(44, 29, 10, 0.10);
      }}
      * {{ box-sizing: border-box; }}
      body {{
        margin: 0;
        font-family: "IBM Plex Sans", "Noto Sans SC", "PingFang SC", sans-serif;
        color: var(--ink);
        background:
          radial-gradient(circle at top left, rgba(0,87,255,0.12), transparent 28%),
          radial-gradient(circle at top right, rgba(216,106,49,0.12), transparent 24%),
          linear-gradient(180deg, #fbf8f1 0%, var(--bg) 100%);
      }}
      a {{ color: inherit; }}
      .page {{
        width: min(1240px, calc(100vw - 32px));
        margin: 24px auto 48px;
      }}
      .hero {{
        background: linear-gradient(135deg, rgba(255,250,242,0.92), rgba(246,241,232,0.92));
        border: 1px solid var(--line);
        border-radius: 28px;
        box-shadow: var(--shadow);
        padding: 28px;
        overflow: hidden;
        position: relative;
      }}
      .hero::after {{
        content: "";
        position: absolute;
        inset: auto -10% -25% auto;
        width: 260px;
        height: 260px;
        background: radial-gradient(circle, rgba(0,87,255,0.15), transparent 68%);
        pointer-events: none;
      }}
      .eyebrow {{
        margin: 0;
        color: var(--warm);
        letter-spacing: 0.08em;
        text-transform: uppercase;
        font-size: 12px;
        font-weight: 700;
      }}
      h1 {{
        margin: 10px 0 12px;
        font-family: "Space Grotesk", "Noto Sans SC", sans-serif;
        font-size: clamp(34px, 5vw, 58px);
        line-height: 0.95;
        letter-spacing: -0.04em;
      }}
      .hero p {{
        margin: 0;
        max-width: 820px;
        color: var(--muted);
        font-size: 15px;
        line-height: 1.7;
      }}
      .stats {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 16px;
        margin-top: 22px;
      }}
      .stat-card {{
        background: var(--surface-strong);
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 18px;
      }}
      .stat-label {{
        margin: 0 0 8px;
        color: var(--muted);
        font-size: 13px;
      }}
      .stat-value {{
        margin: 0;
        font-family: "Space Grotesk", "Noto Sans SC", sans-serif;
        font-size: 36px;
        line-height: 1;
      }}
      .stat-note {{
        margin: 10px 0 0;
        color: var(--muted);
        font-size: 13px;
        line-height: 1.6;
      }}
      .section {{
        margin-top: 28px;
      }}
      .section-header {{
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 14px;
      }}
      .section-title {{
        margin: 0;
        font-family: "Space Grotesk", "Noto Sans SC", sans-serif;
        font-size: 30px;
        letter-spacing: -0.03em;
      }}
      .section-meta {{
        color: var(--muted);
        font-size: 13px;
      }}
      .grid {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 16px;
      }}
      .card {{
        background: var(--surface);
        backdrop-filter: blur(10px);
        border: 1px solid var(--line);
        border-radius: 22px;
        box-shadow: var(--shadow);
        padding: 20px;
        display: grid;
        gap: 14px;
      }}
      .card-head {{
        display: flex;
        justify-content: space-between;
        gap: 12px;
      }}
      .card-title {{
        margin: 0;
        font-size: 20px;
        line-height: 1.35;
        font-weight: 700;
      }}
      .score {{
        flex-shrink: 0;
        min-width: 78px;
        text-align: center;
        border-radius: 999px;
        background: var(--accent-soft);
        color: var(--accent);
        font-weight: 700;
        padding: 10px 12px;
        height: fit-content;
      }}
      .meta {{
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
      }}
      .pill {{
        display: inline-flex;
        align-items: center;
        border-radius: 999px;
        border: 1px solid var(--line);
        background: rgba(255,255,255,0.64);
        padding: 6px 10px;
        color: var(--muted);
        font-size: 12px;
      }}
      .blurb {{
        margin: 0;
        color: var(--muted);
        line-height: 1.7;
        font-size: 14px;
      }}
      .label {{
        color: var(--ink);
        font-weight: 700;
      }}
      .actions {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
        padding-top: 4px;
      }}
      .link {{
        text-decoration: none;
        font-weight: 700;
        color: var(--accent);
      }}
      .footer {{
        margin-top: 24px;
        color: var(--muted);
        font-size: 12px;
      }}
      @media (max-width: 900px) {{
        .stats, .grid {{ grid-template-columns: 1fr; }}
        .card-head {{ flex-direction: column; }}
        .score {{ width: fit-content; }}
      }}
    </style>
  </head>
  <body>
    <main class="page">
      <section class="hero">
        <p class="eyebrow">AI Intel Radar</p>
        <h1>AI 情报雷达日报</h1>
        <p>{html.escape(today)} · 当前事件池累计 {total} 条记录。日报按类别分别选取，减少单一类型事件淹没全局的情况，并补充“它是做什么的 / 为什么值得看”。</p>
        <div class="stats">
          {stat_html}
        </div>
      </section>
      {sections_html}
      <p class="footer">本页面由 AI Intel Radar 自动生成。Markdown 版本与 HTML 版本保存在同一 reports 目录。</p>
    </main>
  </body>
</html>
"""


def _render_html_section(section_name: str, items: list[dict]) -> str:
    cards = "\n".join(_render_html_card(item) for item in items[:15])
    return f"""
    <section class="section">
      <div class="section-header">
        <h2 class="section-title">{html.escape(section_name)}</h2>
        <span class="section-meta">共 {len(items)} 条</span>
      </div>
      <div class="grid">
        {cards}
      </div>
    </section>
    """


def _render_html_card(item: dict) -> str:
    tag_html = "".join(f'<span class="pill">{html.escape(tag)}</span>' for tag in item["tags"]) or '<span class="pill">未打标签</span>'
    return f"""
    <article class="card">
      <div class="card-head">
        <h3 class="card-title">{html.escape(item["title"])}</h3>
        <div class="score">Score<br />{html.escape(item["score"])}</div>
      </div>
      <div class="meta">
        <span class="pill">{html.escape(item["event_label"])}</span>
        <span class="pill">{html.escape(item["vendor"])}</span>
        <span class="pill">{html.escape(item["source_label"])}</span>
        {tag_html}
      </div>
      <p class="blurb"><span class="label">中文说明：</span>{html.escape(item["brief"])}</p>
      <p class="blurb"><span class="label">它是做什么的：</span>{html.escape(item["what_it_is"])}</p>
      {f'<p class="blurb"><span class="label">值得关注的原因：</span>{html.escape(item["why_it_matters"])}</p>' if item["why_it_matters"] else ''}
      {f'<p class="blurb"><span class="label">原文摘要：</span>{html.escape(item["summary"])}</p>' if item["summary"] else ''}
      <div class="actions">
        <span class="pill">已结构化</span>
        <a class="link" href="{html.escape(item["url"])}" target="_blank" rel="noreferrer">查看原链接</a>
      </div>
    </article>
    """


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
