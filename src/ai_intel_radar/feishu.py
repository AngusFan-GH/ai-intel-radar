from __future__ import annotations

import json
import os
from datetime import datetime
from urllib.request import Request, urlopen

from .db import fetch_recent_events


def push_daily_summary(report_url: str | None = None, limit: int = 8) -> None:
    webhook_url = os.getenv("FEISHU_WEBHOOK_URL")
    if not webhook_url:
        print("Skipped Feishu push: FEISHU_WEBHOOK_URL is not configured.")
        return

    payload = build_feishu_payload(
        rows=fetch_recent_events(limit=limit),
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


def build_feishu_payload(rows, report_url: str | None = None) -> dict:
    today = datetime.now().strftime("%Y-%m-%d")
    content: list[list[dict[str, str]]] = [
        [
            {
                "tag": "text",
                "text": f"AI 情报雷达日报 {today}",
            }
        ],
        [
            {
                "tag": "text",
                "text": f"共选取 {len(rows)} 条高优先级事件，按优先级排序展示。",
            }
        ],
    ]

    for index, row in enumerate(rows[:8], start=1):
        label = _event_label(row["event_type"])
        vendor = row["vendor_name"] or "未知主体"
        score = f'{row["score"]:.2f}' if row["score"] is not None else "n/a"
        summary = (row["summary"] or "").replace("\n", " ").strip()[:80]
        line = f"{index}. [{label}] {row['title']} | 主体：{vendor} | 评分：{score}"
        content.append([{"tag": "text", "text": line}])
        if summary:
            content.append([{"tag": "text", "text": f"摘要：{summary}"}])
        content.append([{"tag": "a", "text": "查看原链接", "href": row["url"]}])

    if report_url:
        content.append([{"tag": "a", "text": "查看完整日报", "href": report_url}])

    return {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": f"AI 情报雷达日报 {today}",
                    "content": content,
                }
            }
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
