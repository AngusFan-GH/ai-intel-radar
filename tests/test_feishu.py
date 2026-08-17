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
        payload = build_feishu_payload(rows, top_n=3, report_url="https://example.com/report")
        self.assertEqual(payload["msg_type"], "interactive")
        self.assertIn("AI 情报雷达日报", payload["card"]["header"]["title"]["content"])
        self.assertEqual(
            payload["card"]["elements"][-1]["actions"][0]["url"],
            "https://example.com/report",
        )
