import unittest

from ai_intel_radar.feishu import build_feishu_payload


class FeishuPayloadTests(unittest.TestCase):
    def test_build_feishu_payload_contains_chinese_title(self):
        rows = [
            {
                "title": "Qwen 新模型发布",
                "url": "https://example.com/qwen",
                "summary": "这是一条测试摘要",
                "vendor_name": "Qwen",
                "event_type": "model_launch",
                "score": 88.2,
            }
        ]
        payload = build_feishu_payload(rows, report_url="https://example.com/report")
        self.assertEqual(payload["msg_type"], "post")
        self.assertIn("AI 情报雷达日报", payload["content"]["post"]["zh_cn"]["title"])
        self.assertEqual(
            payload["content"]["post"]["zh_cn"]["content"][-1][0]["href"],
            "https://example.com/report",
        )
