# AI Intel Radar

AI Intel Radar is a local-first MVP for tracking:

- AI product launches from major vendors
- model launches and updates
- new or fast-rising open source AI projects

It uses a dual-engine design:

- `known vendor monitoring`: official blogs, GitHub releases, Hugging Face orgs
- `unknown discovery`: GitHub search and other broad signals

## Features

- TOML-based vendor and discovery source config
- SQLite event store
- RSS/Atom ingestion without third-party dependencies
- GitHub release and repository discovery ingestion via public API
- Hugging Face model discovery via public API
- event scoring and daily Markdown report generation
- CLI for bootstrapping, collecting, scoring, and report generation

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
ai-intel-radar bootstrap-db
ai-intel-radar sync-vendors
ai-intel-radar run-daily
```

Reports are written to `reports/`, and each daily run now generates both Markdown and HTML versions. A GitHub Pages site is also generated under `docs/`.
The sample daily workflow commits generated Markdown reports back to the repository.

## Environment Variables

- `GITHUB_TOKEN`
  - optional but recommended to avoid unauthenticated GitHub API rate limits
- `AI_INTEL_DB_PATH`
  - optional path override for the SQLite database
- `AI_INTEL_CONFIG_PATH`
  - optional vendor config path override
- `AI_INTEL_HTTP_TIMEOUT`
  - optional HTTP timeout in seconds, default `8`
- `AI_INTEL_MAX_WORKERS`
  - optional concurrent collector worker count, default `8`
- `FEISHU_WEBHOOK_URL`
  - optional Feishu group bot webhook URL; when set, `run-daily` can push a summary card
- `FEISHU_REPORT_URL`
  - optional report URL to include in the Feishu card, for example the GitHub file URL of the generated report
- `FEISHU_TOP_N`
  - optional number of highest-priority events to push to Feishu, default `6`

## CLI

```bash
ai-intel-radar bootstrap-db
ai-intel-radar sync-vendors
ai-intel-radar collect --collector rss
ai-intel-radar collect --collector github_releases
ai-intel-radar collect --collector huggingface_models
ai-intel-radar collect --collector github_search
ai-intel-radar score
ai-intel-radar report
ai-intel-radar push-feishu --limit 6
ai-intel-radar run-daily
```

## Feishu Push

The current integration targets a Feishu group custom bot webhook, which is the simplest deployment path.

1. Create a custom bot in the target Feishu group.
2. Copy the webhook URL into `FEISHU_WEBHOOK_URL`.
3. Optionally set `FEISHU_REPORT_URL` if you want the message to include a report link.
4. Run:

```bash
ai-intel-radar push-feishu --limit 6
```

`run-daily` will automatically push when `FEISHU_WEBHOOK_URL` is configured.
The Feishu push now uses an interactive card and only sends the top N highest-priority events.

## Data Model

The SQLite database maintains:

- `vendors`
- `sources`
- `events`

Each event is normalized into one of:

- `product_launch`
- `model_launch`
- `open_source_launch`
- `release_update`
- `unknown_ai_event`

## Suggested Next Steps

- expand the vendor list from 10 to 50+
- add Product Hunt ingestion with authenticated API access
- add richer Feishu cards and per-section routing
- improve similarity-based dedupe with embeddings
- add a lightweight search UI
