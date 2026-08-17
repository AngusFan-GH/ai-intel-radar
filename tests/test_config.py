import unittest
from pathlib import Path

from ai_intel_radar.config import load_config


class ConfigTests(unittest.TestCase):
    def test_load_config(self):
        vendors, discovery_sources = load_config(Path("config/vendors.toml"))
        self.assertTrue(vendors)
        self.assertTrue(discovery_sources)
        self.assertTrue(any(vendor.name == "OpenAI" for vendor in vendors))
