import unittest
from datetime import datetime, timedelta
from pathlib import Path

from ai_intel_radar.config import _resolve_dynamic_text, load_config


class ConfigTests(unittest.TestCase):
    def test_load_config(self):
        vendors, discovery_sources = load_config(Path("config/vendors.toml"))
        self.assertTrue(vendors)
        self.assertTrue(discovery_sources)
        self.assertTrue(any(vendor.name == "OpenAI" for vendor in vendors))
        self.assertTrue(any(source.limit >= 8 for source in discovery_sources))
        self.assertTrue(any(source.query == "text-generation" for source in discovery_sources if source.type == "huggingface_models"))

    def test_resolve_dynamic_text_supports_days_ago(self):
        expected = (datetime.now().date() - timedelta(days=7)).isoformat()
        self.assertEqual(_resolve_dynamic_text("created:>{{days_ago:7}}"), f"created:>{expected}")
