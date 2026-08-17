from __future__ import annotations

import json
import os
from datetime import datetime
from urllib.request import Request, urlopen

from .db import fetch_event_counts, fetch_recent_events


def push_daily_summary(report_url: str | None = None, limit: int | None = None) -> None:
    webhook_url = os.getenv("FEISHU_WEBHOOK_URL")
    if not webhook_url:
        print("Skipped Feishu push: FEISHU_WEBHOOK_URL is not configured.")
        return

    top_n = limit if limit is not None else _resolve_top_n()
    payload = build_feishu_payload(
        rows=fetch_recent_events(limit=top_n),
        top_n=top_n,
        report_url=report_url or os.getenv("FEISHU_REPORT_URL"),
    )
    request = Request(
        webhook_url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urlopen(request, timeout=10) as response:
        body = response.read().decode("utf-8", errors="replace")
    print(f"Feishu push complete: {body}")


def build_feishu_payload(rows, top_n: int, report_url: str | None = None) -> dict:
    today = datetime.now().strftime("%Y-%m-%d")
    counts = fetch_event_counts()
    elements: list[dict] = [
        {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": (
                    f"**Top {top_n} 高优先级事件**\n"
                    f"当前事件池：厂商新品 {counts.get('product_launch', 0)} 条，"
                    f"新模型 {counts.get('model_launch', 0)} 条，"
                    f"新开源项目 {counts.get('open_source_launch', 0)} 条。"
                ),
            },
        },
        {
            "tag": "div",
            "fields": [
                {"is_short": True, "text": {"tag": "lark_md", "content": f"**产品**\n{counts.get('product_launch', 0)}"}},
                {"is_short": True, "text": {"tag": "lark_md", "content": f"**模型**\n{counts.get('model_launch', 0)}"}},
                {"is_short": True, "text": {"tag": "lark_md", "content": f"**开源**\n{counts.get('open_source_launch', 0)}"}},
                {"is_short": True, "text": {"tag": "lark_md", "content": f"**本次推送**\n{len(rows)}"}},
            ],
        },
        {"tag": "hr"},
    ]

    for index, row in enumerate(rows[:top_n], start=1):
        label = _event_label(row["event_type"])
        vendor = row["vendor_name"] or "未知主体"
        score = f'{row["score"]:.2f}' if row["score"] is not None else "n/a"
        summary = _trim((row["summary"] or "").replace("\n", " ").strip(), 120)
        elements.append(
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": (
                        f"**{index}. [{row['title']}]({row['url']})**\n"
                        f"> 类型：{label}｜主体：{vendor}｜评分：{score}\n"
                        f"> 摘要：{summary or '暂无摘要'}"
                    ),
                },
            }
        )
        elements.append(
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": "查看原链接"},
                        "type": "default",
                        "url": row["url"],
                    }
                ],
            }
        )
        elements.append({"tag": "hr"})

    if report_url:
        elements.append(
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": "查看完整日报"},
                        "type": "primary",
                        "url": report_url,
                    }
                ],
            }
        )

    return {
        "msg_type": "interactive",
        "card": {
            "config": {
                "wide_screen_mode": True,
                "enable_forward": True,
            },
            "header": {
                "template": "blue",
                "title": {
                    "tag": "plain_text",
                    "content": f"AI 情报雷达日报 {today}",
                },
            },
            "elements": elements,
        },
    }


def _event_label(value: str) -> str:
    mapping = {
        "product_launch": "产品发布",
        "model_launch": "模型发布",
        "open_source_launch": "开源项目发布",
        "release_update": "版本更新",
        "unknown_ai_event": "一般事件",
    }
    return mapping.get(value, value)


def _resolve_top_n() -> int:
    raw = os.getenv("FEISHU_TOP_N", "6")
    try:
        value = int(raw)
    except ValueError:
        return 6
    return max(1, value)


def _trim(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"
