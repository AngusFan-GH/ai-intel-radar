from __future__ import annotations

import html
import json
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

from .db import fetch_recent_events


SECTION_ORDER = ["厂商新品", "新模型", "新开源项目", "其他观察"]
SECTION_VENDOR_LIMITS = {"厂商新品": 6, "新模型": 6, "新开源项目": 10, "其他观察": 6}
ITEMS_PER_VENDOR = 3


def build_daily_report(output_dir: Path = Path("reports")) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    docs_dir = Path("docs")
    docs_reports_dir = docs_dir / "reports"
    docs_dir.mkdir(parents=True, exist_ok=True)
    docs_reports_dir.mkdir(parents=True, exist_ok=True)

    rows = fetch_recent_events(limit=250)
    items = [_build_item(row) for row in rows]
    grouped = _group_items(items)
    section_totals = {section: sum(len(vendors.values()) and sum(len(v) for v in vendors.values()) or 0 for vendors in [grouped[section]]) for section in SECTION_ORDER}
    pruned = _prune_grouped(grouped)

    today = datetime.now().strftime("%Y-%m-%d")
    markdown_path = output_dir / f"daily-report-{today}.md"
    html_path = output_dir / f"daily-report-{today}.html"
    docs_html_path = docs_reports_dir / f"daily-report-{today}.html"

    markdown_content = _render_markdown_report(today, section_totals, pruned)
    html_report = _render_html_report(
        today=today,
        section_totals=section_totals,
        grouped=pruned,
        primary_href=f"./daily-report-{today}.html",
        home_href="../docs/index.html",
    )
    docs_html_report = _render_html_report(
        today=today,
        section_totals=section_totals,
        grouped=pruned,
        primary_href=f"./daily-report-{today}.html",
        home_href="../index.html",
    )

    markdown_path.write_text(markdown_content, encoding="utf-8")
    html_path.write_text(html_report, encoding="utf-8")
    docs_html_path.write_text(docs_html_report, encoding="utf-8")
    _write_docs_index(docs_dir, today, section_totals)
    return markdown_path


def _build_item(row) -> dict:
    tags = [_tag_label(tag) for tag in json.loads(row["tags_json"])] if row["tags_json"] else []
    payload = _parse_payload(row["raw_payload"])
    canonical_vendor = _canonical_vendor_name(row["vendor_name"] or "", row["title"])
    score_value = row["score"] if row["score"] is not None else 0.0
    score = f"{score_value:.2f}"
    summary = _trim_sentence((row["summary"] or "").replace("\n", " ").strip(), 180)
    display_section = _display_section(row)
    event_label = _event_label(display_section)
    source_label = _source_label(row["source_type"])
    brief = (
        f"主体：{canonical_vendor}；事件类型：{event_label}；来源：{source_label}；"
        f"评分：{score}；标签：{('、'.join(tags) if tags else '未打标签')}。"
    )
    return {
        "title": row["title"],
        "url": row["url"],
        "canonical_vendor": canonical_vendor,
        "display_section": display_section,
        "brief": brief,
        "what_it_is": _describe_what_it_is(row, payload),
        "why_it_matters": _describe_why_it_matters(row),
        "how_to_use": _describe_how_to_use(row, payload),
        "summary": summary,
        "score": score,
        "score_value": score_value,
        "tags": tags,
        "source_label": source_label,
        "event_label": event_label,
    }


def _group_items(items: list[dict]) -> dict[str, dict[str, list[dict]]]:
    grouped: dict[str, dict[str, list[dict]]] = {section: defaultdict(list) for section in SECTION_ORDER}
    for item in items:
        grouped[item["display_section"]][item["canonical_vendor"]].append(item)
    for vendors in grouped.values():
        for vendor_items in vendors.values():
            vendor_items.sort(key=lambda item: item["score_value"], reverse=True)
    return grouped


def _prune_grouped(grouped: dict[str, dict[str, list[dict]]]) -> dict[str, list[tuple[str, list[dict]]]]:
    pruned: dict[str, list[tuple[str, list[dict]]]] = {}
    for section_name in SECTION_ORDER:
        vendors = [(vendor_name, items) for vendor_name, items in grouped[section_name].items()]
        vendors.sort(key=lambda pair: pair[1][0]["score_value"] if pair[1] else 0.0, reverse=True)
        limited = vendors[: SECTION_VENDOR_LIMITS[section_name]]
        pruned[section_name] = [(vendor, items[:ITEMS_PER_VENDOR]) for vendor, items in limited]
    return pruned


def _render_markdown_report(today: str, section_totals: dict[str, int], grouped: dict[str, list[tuple[str, list[dict]]]]) -> str:
    total = sum(section_totals.values())
    lines = [f"# AI 情报雷达日报（{today}）", ""]
    lines.append(f"当前展示池累计 {total} 条事件。日报已改成按厂商合并展示，并补充“这是什么 / 为什么值得看 / 怎么用”。")
    lines.append("")
    lines.append(
        "数据概况："
        f" 厂商新品 {section_totals.get('厂商新品', 0)} 条；"
        f" 新模型 {section_totals.get('新模型', 0)} 条；"
        f" 新开源项目 {section_totals.get('新开源项目', 0)} 条；"
        f" 其他观察 {section_totals.get('其他观察', 0)} 条。"
    )
    lines.append("")
    for section_name in SECTION_ORDER:
        vendor_groups = grouped.get(section_name, [])
        if not vendor_groups:
            continue
        lines.append(f"## {section_name}（{section_totals.get(section_name, 0)}）")
        lines.append("")
        for vendor_name, items in vendor_groups:
            lines.append(f"### {vendor_name}（{len(items)} 条重点）")
            lines.append("")
            for item in items:
                lines.extend(_render_markdown_item(item))
                lines.append("")
    return "\n".join(lines).strip() + "\n"


def _render_markdown_item(item: dict) -> list[str]:
    lines = [f"- [{item['title']}]({item['url']})"]
    lines.append(f"  - 中文说明：{item['brief']}")
    lines.append(f"  - 这是什么：{item['what_it_is']}")
    if item["why_it_matters"]:
        lines.append(f"  - 为什么值得看：{item['why_it_matters']}")
    if item["how_to_use"]:
        lines.append(f"  - 怎么用：{item['how_to_use']}")
    if item["summary"]:
        lines.append(f"  - 原文摘要：{item['summary']}")
    return lines


def _render_html_report(
    today: str,
    section_totals: dict[str, int],
    grouped: dict[str, list[tuple[str, list[dict]]]],
    primary_href: str,
    home_href: str,
) -> str:
    total = sum(section_totals.values())
    stats = [
        ("厂商新品", section_totals.get("厂商新品", 0), "官方产品、服务、发布动作"),
        ("新模型", section_totals.get("新模型", 0), "模型上新、更新、上架"),
        ("新开源项目", section_totals.get("新开源项目", 0), "GitHub / 开源生态高热度"),
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
        _render_html_section(section_name, section_totals.get(section_name, 0), grouped.get(section_name, []))
        for section_name in SECTION_ORDER
        if grouped.get(section_name)
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>AI 情报雷达日报 {html.escape(today)}</title>
    <style>
      :root {{
        --bg: #f7f3ea;
        --surface: rgba(255, 251, 245, 0.84);
        --surface-strong: #fffaf2;
        --ink: #1b1814;
        --muted: #655f56;
        --line: rgba(38, 33, 26, 0.12);
        --accent: #0057ff;
        --accent-soft: #dce7ff;
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
      .page {{ width: min(1280px, calc(100vw - 32px)); margin: 24px auto 48px; }}
      .hero {{
        background: linear-gradient(135deg, rgba(255,250,242,0.95), rgba(246,241,232,0.92));
        border: 1px solid var(--line);
        border-radius: 28px;
        box-shadow: var(--shadow);
        padding: 28px;
      }}
      .eyebrow {{ margin: 0; color: var(--warm); letter-spacing: 0.08em; text-transform: uppercase; font-size: 12px; font-weight: 700; }}
      h1 {{
        margin: 10px 0 12px;
        font-family: "Space Grotesk", "Noto Sans SC", sans-serif;
        font-size: clamp(34px, 5vw, 58px);
        line-height: 0.95;
        letter-spacing: -0.04em;
      }}
      .hero p {{ margin: 0; max-width: 860px; color: var(--muted); font-size: 15px; line-height: 1.7; }}
      .hero-actions {{ display: flex; flex-wrap: wrap; gap: 12px; margin-top: 20px; }}
      .hero-link {{
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 999px;
        padding: 12px 18px;
        font-weight: 700;
        border: 1px solid var(--line);
        background: var(--surface-strong);
        color: var(--ink);
      }}
      .hero-link.primary {{ background: var(--accent); color: white; border-color: transparent; }}
      .stats {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin-top: 22px; }}
      .stat-card {{ background: var(--surface-strong); border: 1px solid var(--line); border-radius: 20px; padding: 18px; }}
      .stat-label {{ margin: 0 0 8px; color: var(--muted); font-size: 13px; }}
      .stat-value {{ margin: 0; font-family: "Space Grotesk", "Noto Sans SC", sans-serif; font-size: 36px; line-height: 1; }}
      .stat-note {{ margin: 10px 0 0; color: var(--muted); font-size: 13px; line-height: 1.6; }}
      .section {{ margin-top: 28px; }}
      .section-header {{ display: flex; align-items: baseline; justify-content: space-between; gap: 12px; margin-bottom: 14px; }}
      .section-title {{ margin: 0; font-family: "Space Grotesk", "Noto Sans SC", sans-serif; font-size: 30px; letter-spacing: -0.03em; }}
      .section-meta {{ color: var(--muted); font-size: 13px; }}
      .vendor-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; }}
      .vendor-card {{ background: var(--surface); backdrop-filter: blur(10px); border: 1px solid var(--line); border-radius: 22px; box-shadow: var(--shadow); padding: 20px; }}
      .vendor-head {{ display: flex; justify-content: space-between; gap: 12px; margin-bottom: 14px; }}
      .vendor-name {{ margin: 0; font-size: 22px; line-height: 1.2; }}
      .vendor-count {{ color: var(--accent); background: var(--accent-soft); border-radius: 999px; padding: 8px 12px; font-weight: 700; white-space: nowrap; height: fit-content; }}
      .event-list {{ display: grid; gap: 14px; }}
      .event-item {{ border-top: 1px solid var(--line); padding-top: 14px; }}
      .event-item:first-child {{ border-top: none; padding-top: 0; }}
      .event-title {{ margin: 0; font-size: 18px; line-height: 1.4; }}
      .meta {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }}
      .pill {{ display: inline-flex; align-items: center; border-radius: 999px; border: 1px solid var(--line); background: rgba(255,255,255,0.64); padding: 6px 10px; color: var(--muted); font-size: 12px; }}
      .blurb {{ margin: 10px 0 0; color: var(--muted); line-height: 1.72; font-size: 14px; }}
      .label {{ color: var(--ink); font-weight: 700; }}
      .actions {{ display: flex; justify-content: flex-end; margin-top: 12px; }}
      .link {{ text-decoration: none; font-weight: 700; color: var(--accent); }}
      .footer {{ margin-top: 24px; color: var(--muted); font-size: 12px; }}
      @media (max-width: 960px) {{ .stats, .vendor-grid {{ grid-template-columns: 1fr; }} .vendor-head {{ flex-direction: column; }} }}
    </style>
  </head>
  <body>
    <main class="page">
      <section class="hero">
        <p class="eyebrow">AI Intel Radar</p>
        <h1>AI 情报雷达日报</h1>
        <p>{html.escape(today)} · 当前展示池累计 {total} 条事件。日报已按厂商合并展示，并为每条消息补充“这是什么 / 为什么值得看 / 怎么用”，帮助读者快速理解消息本身。</p>
        <div class="hero-actions">
          <a class="hero-link primary" href="{html.escape(primary_href)}">打开本日报 HTML</a>
          <a class="hero-link" href="{html.escape(home_href)}">返回最新首页</a>
        </div>
        <div class="stats">{stat_html}</div>
      </section>
      {sections_html}
      <p class="footer">注：当前产品/模型类源存在可用性差异，因此日报已做“按厂商聚合 + 重分类展示”，减少单一厂商刷屏。</p>
    </main>
  </body>
</html>
"""


def _render_html_section(section_name: str, section_total: int, vendor_groups: list[tuple[str, list[dict]]]) -> str:
    cards = "\n".join(_render_html_vendor_card(vendor, items) for vendor, items in vendor_groups)
    return f"""
    <section class="section">
      <div class="section-header">
        <h2 class="section-title">{html.escape(section_name)}</h2>
        <span class="section-meta">累计 {section_total} 条，当前展示 {len(vendor_groups)} 个厂商组</span>
      </div>
      <div class="vendor-grid">{cards}</div>
    </section>
    """


def _render_html_vendor_card(vendor: str, items: list[dict]) -> str:
    events = "\n".join(_render_html_event_item(item) for item in items)
    return f"""
    <article class="vendor-card">
      <div class="vendor-head">
        <h3 class="vendor-name">{html.escape(vendor)}</h3>
        <span class="vendor-count">{len(items)} 条重点</span>
      </div>
      <div class="event-list">{events}</div>
    </article>
    """


def _render_html_event_item(item: dict) -> str:
    tags_html = "".join(f'<span class="pill">{html.escape(tag)}</span>' for tag in item["tags"]) or '<span class="pill">未打标签</span>'
    summary_html = (
        f'<p class="blurb"><span class="label">原文摘要：</span>{html.escape(item["summary"])}</p>'
        if item["summary"]
        else ""
    )
    return f"""
    <div class="event-item">
      <h4 class="event-title">{html.escape(item["title"])}</h4>
      <div class="meta">
        <span class="pill">{html.escape(item["event_label"])}</span>
        <span class="pill">Score {html.escape(item["score"])}</span>
        <span class="pill">{html.escape(item["source_label"])}</span>
        {tags_html}
      </div>
      <p class="blurb"><span class="label">这是什么：</span>{html.escape(item["what_it_is"])}</p>
      <p class="blurb"><span class="label">为什么值得看：</span>{html.escape(item["why_it_matters"] or "当前主要是厂商/项目动态，建议结合原链接查看详情。")}</p>
      <p class="blurb"><span class="label">怎么用：</span>{html.escape(item["how_to_use"])}</p>
      {summary_html}
      <div class="actions">
        <a class="link" href="{html.escape(item["url"])}" target="_blank" rel="noreferrer">查看原链接</a>
      </div>
    </div>
    """


def _write_docs_index(docs_dir: Path, today: str, section_totals: dict[str, int]) -> None:
    total = sum(section_totals.values())
    index_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>AI 情报雷达</title>
    <style>
      body {{
        margin: 0;
        font-family: "IBM Plex Sans", "Noto Sans SC", "PingFang SC", sans-serif;
        background: linear-gradient(180deg, #fcfaf5 0%, #efe7da 100%);
        color: #171512;
      }}
      .page {{
        width: min(980px, calc(100vw - 32px));
        margin: 40px auto;
        background: rgba(255,255,255,0.75);
        border: 1px solid rgba(23,21,18,0.12);
        border-radius: 28px;
        padding: 30px;
        box-shadow: 0 18px 50px rgba(44, 29, 10, 0.10);
      }}
      h1 {{
        margin: 0 0 10px;
        font-family: "Space Grotesk", "Noto Sans SC", sans-serif;
        font-size: clamp(32px, 5vw, 56px);
        line-height: 0.95;
      }}
      p {{ color: #625b52; line-height: 1.7; }}
      .cta {{
        display: inline-flex;
        margin-top: 8px;
        padding: 14px 18px;
        border-radius: 999px;
        background: #0057ff;
        color: white;
        text-decoration: none;
        font-weight: 700;
      }}
      .stats {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 14px;
        margin-top: 22px;
      }}
      .stat {{
        border-radius: 18px;
        border: 1px solid rgba(23,21,18,0.12);
        background: rgba(255,250,242,0.9);
        padding: 16px;
      }}
      .stat b {{ display: block; font-size: 30px; margin-top: 8px; }}
      .archive {{ margin-top: 28px; padding-top: 20px; border-top: 1px solid rgba(23,21,18,0.12); }}
      .archive a {{ color: #0057ff; text-decoration: none; font-weight: 700; }}
      @media (max-width: 760px) {{ .stats {{ grid-template-columns: 1fr; }} }}
    </style>
  </head>
  <body>
    <main class="page">
      <h1>AI 情报雷达</h1>
      <p>这个页面用于 GitHub Pages 展示最新日报，打开后直接进入 HTML 报告，不需要再看 Markdown 文件。</p>
      <a class="cta" href="./reports/daily-report-{html.escape(today)}.html">打开最新日报</a>
      <div class="stats">
        <section class="stat">厂商新品<b>{section_totals.get('厂商新品', 0)}</b></section>
        <section class="stat">新模型<b>{section_totals.get('新模型', 0)}</b></section>
        <section class="stat">新开源项目<b>{section_totals.get('新开源项目', 0)}</b></section>
      </div>
      <div class="archive">
        <p>当前展示池累计 {total} 条事件。</p>
        <a href="./reports/daily-report-{html.escape(today)}.html">查看 {html.escape(today)} 归档页</a>
      </div>
    </main>
  </body>
</html>
"""
    (docs_dir / "index.html").write_text(index_html, encoding="utf-8")


def _display_section(row) -> str:
    corpus = f"{row['title']} {row['summary'] or ''}".lower()
    if row["source_type"] in {"github_search", "github_releases"}:
        return "新开源项目"
    if row["event_type"] == "model_launch":
        return "新模型"
    if row["event_type"] == "product_launch":
        if any(token in corpus for token in ("appoint", "chief revenue officer", "letter to", "case study", "how ", "enterprise", "governor")):
            return "其他观察"
        return "厂商新品"
    return "其他观察"


def _canonical_vendor_name(vendor_name: str, title: str) -> str:
    vendor = (vendor_name or "").strip()
    title_lower = title.lower()
    mapping = {
        "qwenlm": "Qwen",
        "deepseek-ai": "DeepSeek",
        "tencent-hunyuan": "腾讯混元",
        "moonshotai": "月之暗面",
        "minimax-ai": "MiniMax",
        "baichuan-inc": "百川智能",
        "stepfun-ai": "StepFun",
        "bytedance-seed": "字节 Seed",
        "internlm": "InternLM",
        "modelscope": "ModelScope",
        "zhipuai": "智谱",
        "zai-org": "智谱",
        "openai": "OpenAI",
        "anthropic": "Anthropic",
    }
    if vendor.lower() in mapping:
        return mapping[vendor.lower()]
    if "qwen" in title_lower:
        return "Qwen"
    if "deepseek" in title_lower:
        return "DeepSeek"
    if "moonshot" in title_lower or "kimi" in title_lower:
        return "月之暗面"
    return vendor or "未知主体"


def _parse_payload(raw_payload: str | None) -> dict:
    if not raw_payload:
        return {}
    try:
        payload = json.loads(raw_payload)
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def _describe_what_it_is(row, payload: dict) -> str:
    corpus = f"{row['title']} {row['summary'] or ''}".lower()
    if row["source_type"] == "github_search":
        description = payload.get("description") or row["summary"] or ""
        repo = row["github_repo"] or payload.get("full_name") or row["title"]
        return f"`{repo}` 是一个{_infer_project_kind(corpus)}。当前公开描述是：{_trim_sentence(description or '暂无更详细描述。', 130)}"
    if row["source_type"] == "github_releases":
        repo = row["github_repo"] or row["title"]
        return f"这是 `{repo}` 的新版本发布，表示这个 SDK 或开源项目最近发布了新的可安装版本。"
    if row["source_type"] == "huggingface_models":
        model_name = row["title"].replace(" updated", "")
        return f"`{model_name}` 是近期更新的模型条目，通常意味着模型权重、模型卡或可用性发生了变化。"
    if row["source_type"] == "rss":
        return _describe_rss_item(row["title"], row["summary"] or "")
    return _trim_sentence(row["summary"] or row["title"], 130)


def _describe_why_it_matters(row) -> str:
    reasons: list[str] = []
    if row["github_stars"]:
        reasons.append(f"当前记录到约 {row['github_stars']} 个 GitHub stars")
    if row["source_type"] == "github_search":
        reasons.append("近期在 GitHub 发现流中活跃，说明关注度或增长较高")
    if row["source_type"] == "rss":
        reasons.append("来自官方发布源，可信度较高")
    if row["source_type"] == "huggingface_models":
        reasons.append("属于模型分发平台上的更新，适合关注模型能力和生态反馈")
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


def _describe_how_to_use(row, payload: dict) -> str:
    corpus = f"{row['title']} {row['summary'] or ''}".lower()
    if row["source_type"] == "github_search":
        repo = row["github_repo"] or payload.get("full_name") or "该项目"
        if any(token in corpus for token in ("plugin", "plugins", "harness")):
            return f"优先阅读 `{repo}` 的 README 与安装说明，把它作为插件或扩展接入现有 agent / harness 环境。"
        if any(token in corpus for token in ("benchmark", "eval", "evaluation")):
            return f"把 `{repo}` 当作评测工具使用，准备待测模型或 agent，然后按仓库脚本运行 benchmark。"
        if any(token in corpus for token in ("speech", "asr", "audio", "voice")):
            return f"把 `{repo}` 用作语音能力组件，常见用法是本地推理、批量转写，或包装成服务接口。"
        if any(token in corpus for token in ("agent", "coding", "terminal", "code")):
            return f"开发者可以先 clone `{repo}`，按 README 安装依赖，然后在本地终端或开发流程中试用。"
        if any(token in corpus for token in ("model", "weights", "checkpoint")):
            return f"通常需要先获取模型权重，再配合官方脚本、Transformers、vLLM 等框架推理或部署。"
        return f"建议先查看 `{repo}` 的 README、示例和安装命令，先确认它是库、应用还是评测工具，再决定接入方式。"
    if row["source_type"] == "github_releases":
        return "如果你已经在用这个 SDK 或项目，优先查看 release notes 和升级说明，再决定是否更新依赖版本。"
    if row["source_type"] == "huggingface_models":
        return "通常在 Hugging Face 页面查看模型卡、许可证和示例代码，再决定是直接推理、微调还是部署服务。"
    if row["source_type"] == "rss":
        if "aws" in corpus or "bedrock" in corpus:
            return "如果你在 AWS 体系内，可以优先通过 Bedrock 或相关官方接入路径启用，而不是自行部署。"
        if "api" in corpus or "service tier" in corpus:
            return "这类内容通常通过官方 API、控制台或服务配置启用，适合先看定价、限额和接入文档。"
        if any(token in corpus for token in ("case study", "how ", "customer", "builds", "enterprise")):
            return "这更像案例或实践参考，适合借鉴落地方式，而不是直接安装使用。"
        return "优先打开原链接查看官方说明、接入方式和限制条件，再决定是否纳入你的工作流。"
    return "建议先查看原链接中的官方文档、README 或示例代码，再确认具体接入方式。"


def _describe_rss_item(title: str, summary: str) -> str:
    corpus = f"{title} {summary}".lower()
    if "service tier" in corpus or "api" in corpus:
        return "这是一项新的 API / 服务能力更新，重点在于更快、更便宜或更易接入的调用方式。"
    if "available on aws" in corpus or "bedrock" in corpus:
        return "这是模型或能力在云平台上的可用性更新，重点在于企业可以通过现有云服务更快接入。"
    if "ads in chatgpt" in corpus:
        return "这是面向终端产品体验的变更，重点不是模型本身，而是 ChatGPT 的产品形态和商业化策略。"
    if any(token in corpus for token in ("guide", "builder", "use gpt", "how enterprises put ai to work")):
        return "这是一篇官方实践或方法说明，核心是解释某个模型或能力在真实业务中的使用方式。"
    if any(token in corpus for token in ("appoint", "chief revenue officer", "letter", "governor")):
        return "这更偏公司运营或政策沟通，并不是严格意义上的新产品发布。"
    return f"这是官方发布源中的一条更新，核心内容是：{_trim_sentence(summary or title, 120)}"


def _infer_project_kind(corpus: str) -> str:
    if any(token in corpus for token in ("agent", "terminal")):
        return "面向 AI agent 或编码助手的开源项目"
    if any(token in corpus for token in ("benchmark", "eval", "evaluation")):
        return "用于评测模型或 agent 能力的开源项目"
    if any(token in corpus for token in ("speech", "asr", "voice", "audio")):
        return "用于语音处理或语音识别的开源项目"
    if any(token in corpus for token in ("plugin", "plugins", "integration")):
        return "用于扩展现有 AI 系统能力的插件或集成项目"
    if any(token in corpus for token in ("model", "weights", "llm")):
        return "围绕模型权重、模型推理或模型家族的开源项目"
    return "面向 AI 应用或基础设施的开源项目"


def _trim_sentence(value: str, limit: int) -> str:
    text = " ".join(value.split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def _event_label(section_name: str) -> str:
    mapping = {"厂商新品": "产品发布", "新模型": "模型发布", "新开源项目": "开源项目发布", "其他观察": "观察事项"}
    return mapping.get(section_name, section_name)


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
