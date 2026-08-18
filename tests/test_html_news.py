import unittest
from unittest.mock import patch

from ai_intel_radar.collectors.html_news import HTMLNewsCollector
from ai_intel_radar.models import Source


INDEX_HTML = """
<html>
  <head><title>Vendor News</title></head>
  <body>
    <a href="/news/model-v1">Launch of Model V1</a>
    <a href="/privacy">Privacy</a>
  </body>
</html>
"""

ARTICLE_HTML = """
<html>
  <head>
    <title>Model V1</title>
    <meta name="description" content="A new multimodal reasoning model for enterprise usage." />
  </head>
  <body>
    <time datetime="2026-08-18"></time>
    <h1>Model V1</h1>
    <p>A new multimodal reasoning model for enterprise usage.</p>
  </body>
</html>
"""

SINGLE_HTML = """
<html>
  <head>
    <title>DeepSeek Update</title>
    <meta name="description" content="Date: 2026-08-13" />
  </head>
  <body>
    <h1>DeepSeek V4 Pro Update</h1>
    <p>The latest API update improves coding and agent workflows.</p>
  </body>
</html>
"""


class HTMLNewsCollectorTests(unittest.TestCase):
    def test_collects_matching_links(self):
        source = Source(
            vendor_name="Test Vendor",
            type="html_news",
            event_type="model_launch",
            url="https://vendor.example/news",
            query="/news/",
            limit=3,
        )

        def fake_fetch(url, params=None):
            if url == "https://vendor.example/news":
                return INDEX_HTML
            if url == "https://vendor.example/news/model-v1":
                return ARTICLE_HTML
            raise AssertionError(url)

        with patch("ai_intel_radar.collectors.html_news.fetch_text", side_effect=fake_fetch):
            events = HTMLNewsCollector().collect(source)

        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].title, "Model V1")
        self.assertEqual(events[0].vendor_name, "Test Vendor")
        self.assertEqual(events[0].event_type, "model_launch")

    def test_falls_back_to_single_page_event(self):
        source = Source(
            vendor_name="DeepSeek",
            type="html_news",
            event_type="product_launch",
            url="https://vendor.example/updates",
            limit=1,
        )

        with patch("ai_intel_radar.collectors.html_news.fetch_text", return_value=SINGLE_HTML):
            events = HTMLNewsCollector().collect(source)

        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].url, "https://vendor.example/updates")
        self.assertIn("2026-08-13", events[0].summary)

