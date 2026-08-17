from __future__ import annotations

import json
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen


USER_AGENT = "ai-intel-radar/0.1.0"
DEFAULT_TIMEOUT = float(os.getenv("AI_INTEL_HTTP_TIMEOUT", "8"))


def fetch_text(url: str, params: dict[str, str] | None = None) -> str:
    final_url = f"{url}?{urlencode(params)}" if params else url
    request = Request(final_url, headers=_headers())
    with urlopen(request, timeout=DEFAULT_TIMEOUT) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_json(url: str, params: dict[str, str] | None = None) -> dict | list:
    return json.loads(fetch_text(url, params=params))


def _headers() -> dict[str, str]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers
