from __future__ import annotations

import json
import os
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


USER_AGENT = "ai-intel-radar/0.1.0"


def fetch_text(url: str, params: dict[str, str | int] | None = None) -> str:
    final_url = f"{url}?{urlencode(params)}" if params else url
    request = Request(final_url, headers=_headers())
    last_error: Exception | None = None
    for attempt in range(_resolve_retry_count()):
        try:
            with urlopen(request, timeout=_resolve_timeout()) as response:
                return response.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            if 400 <= exc.code < 500 and exc.code != 429:
                raise
            last_error = exc
        except URLError as exc:
            last_error = exc
        if attempt < _resolve_retry_count() - 1:
            time.sleep(0.6 * (attempt + 1))
    if last_error:
        raise last_error
    raise RuntimeError(f"Failed to fetch {final_url}")


def fetch_json(url: str, params: dict[str, str | int] | None = None) -> dict | list:
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


def _resolve_timeout() -> float:
    return float(os.getenv("AI_INTEL_HTTP_TIMEOUT", "15"))


def _resolve_retry_count() -> int:
    raw = os.getenv("AI_INTEL_HTTP_RETRIES", "3")
    try:
        return max(1, int(raw))
    except ValueError:
        return 3
