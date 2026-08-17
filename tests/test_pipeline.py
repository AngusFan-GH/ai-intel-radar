import os
import unittest

from ai_intel_radar.pipeline import _resolve_max_workers


class PipelineConfigTests(unittest.TestCase):
    def test_resolve_max_workers_falls_back_for_invalid_value(self):
        previous = os.environ.get("AI_INTEL_MAX_WORKERS")
        os.environ["AI_INTEL_MAX_WORKERS"] = "invalid"
        try:
            self.assertEqual(_resolve_max_workers(), 8)
        finally:
            if previous is None:
                os.environ.pop("AI_INTEL_MAX_WORKERS", None)
            else:
                os.environ["AI_INTEL_MAX_WORKERS"] = previous
