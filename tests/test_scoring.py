import unittest

from ai_intel_radar.scoring import score_event


class ScoringTests(unittest.TestCase):
    def test_score_event_prefers_recent_model_launch(self):
        row = {
            "source_type": "huggingface_models",
            "vendor_name": "Test Vendor",
            "event_type": "model_launch",
            "is_open_source": 1,
            "github_stars": 120,
            "published_at": "2026-08-17T00:00:00+00:00",
            "discovered_at": "2026-08-17T00:00:00+00:00",
        }
        self.assertGreater(score_event(row), 60)
