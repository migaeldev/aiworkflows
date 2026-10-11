# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Critical Operating Rules

### Immutability Guardrail — Host-Mode Aware

This repo's production boundary is recorded in [`aiworkspace/host.md`](./aiworkspace/host.md) (`host_mode: monorepo` or `bolt-on`; absent means `monorepo`). This repo's own `host.md` records `monorepo`.

- **`monorepo`** (this repo): never directly edit, create, or delete files inside `apps/[workspace]`.
- **`bolt-on`** (a different repo `aiworkspace` was added into): never directly edit, create, or delete anything outside `aiworkspace/` (and `.claude/`) except via that workspace's `index.md` Production Target Map.

All code changes must take place in `aiworkspace/workspaces/[workspace]/processing/`. Only a human issuing an explicit `promote` command may move code from `finalized/` into production.

### Mandatory Step Gate — No Automatic Advancement

After completing work in a lifecycle step, present the changes and wait for explicit human confirmation before advancing to the next step. Never automatically move files between `planning/` → `resources/` → `processing/` → `finalized/` → `apps/`.

### Package Manager — `pnpm` Only

Use `pnpm` (not `npm` or `yarn`) for all Node.js / Next.js dependency installs and scripts.

### Software-Engineering Skill Reference — Mandatory on Code-Writing Tasks

Before writing, generating, or modifying any code, first load and follow [`aiworkspace/skills/engineering/software-engineer/SKILL.md`](./aiworkspace/skills/engineering/software-engineer/SKILL.md). Standing requirement, same force as the rules above — not optional registry discovery.

---

## Development Commands

### Backend API (`apps/feasibility-insights/app/`)

```bash
cd apps/feasibility-insights/app
pip install -r requirements.txt
python -m cmd.api.main        # Starts Flask API on http://127.0.0.1:8080
                              # Swagger UI available at http://127.0.0.1:8080/docs
```

### Backend Batch / CLI

```bash
cd apps/feasibility-insights/app
python -m cmd.cli.main --client_name ALL --relative_period last_month
python -m cmd.cli.main --client_name "clientname" --relative_period last_week --overwrite
```

### Frontend Next.js Studio (`apps/feasibility-insights/ui/`)

```bash
cd apps/feasibility-insights/ui
pnpm install
pnpm dev       # http://localhost:3000
pnpm build
pnpm lint
```

### Cloud Run Deployment

```bash
cd apps/feasibility-insights/app
./deploy.sh    # Builds both container images, deploys Cloud Run Service + Job + Scheduler
```

---

## Architecture

### Repository Structure

```
insights/
├── AGENTS.md                   # AI agent operating rules (read before working)
├── apps/                       # Canonical production applications (AI READ-ONLY)
│   └── feasibility-insights/
│       ├── app/                # Python backend (hexagonal: cmd/ + internal/)
│       └── ui/                 # Next.js 14 Prompt Fine-Tuning Studio
└── aiworkspace/                # OKF v0.1 knowledge base — active development workspace
    ├── skills/                 # Reusable AI skills (design, engineering, productivity, security)
    └── workspaces/
        └── feasibility-insights/   # Active domain workspace
            ├── planning/       # Step 0: Project/Feature plans, research, decisions
            ├── resources/      # Step 1: Input context, schemas, raw data
            ├── processing/     # Step 2: Active development (all AI edits go here)
            └── finalized/      # Step 3: Audited, gate-passed code
```

### 5-Stage Lifecycle Pipeline

```
planning/ → resources/ → processing/ → finalized/ → promote → apps/[workspace]/
(plan)        (input)       (iteration)   (audited)   (human)    (production)
```

Step 0 (`planning/`) runs `aiworkspace/skills/productivity/plan/SKILL.md` — determines Project Plan vs. Feature/Change Plan, always runs `grill-me`, offers `goal-driven` as an opt-in. Step 3 (`finalized/`) requires four gates before promotion: security audit, OpenAPI spec generation, production documentation, and passing tests (plus the dual-axis `code-review`, persisted to `finalized/review.md`). The `promote` step also updates both the root `README.md` and `aiworkspace/index.md`.

### Feasibility Insights Backend

The backend uses a Go-style project layout (`cmd/` entrypoints + `internal/` library):

- **`cmd/api/main.py`** — Flask REST API (HTTP endpoints, Cloud Run Service)
- **`cmd/cli/main.py`** — CLI batch runner (Cloud Run Job, scheduled execution)
- **`internal/logic/insights_engine.py`** — Core pipeline: BigQuery metric extraction → Gemini Vertex AI generation → structured JSON output → BigQuery MERGE
- **`internal/config.py`** — All environment-driven configuration; BigQuery table names are constructed dynamically from `ENVIRONMENT`
- **`internal/sql/`** — BigQuery DDLs and parameterized extraction queries (numbered 01–07)

**Pipeline flow in `insights_engine.py`:**
1. Deduplication check (skip if record exists in `DESTINATION_TABLE` unless `overwrite=True`)
2. BigQuery metric extraction from pre-aggregated `CLIENT_DAILY_SUMMARY_TABLE`
3. Gemini Enterprise (Vertex AI) structured JSON generation via `InsightsSchema` Pydantic model
4. Post-processing normalization of AI output (executive summary truncation, paragraph splitting, bullet formatting)
5. MERGE into `DESTINATION_TABLE`; batch mode uses `ThreadPoolExecutor` for all active clients in parallel

**API endpoints:** `GET /`, `GET /docs`, `GET /openapi.json`, `POST /generate-insights`, `POST /backfill-daily-summary`

### Frontend (Next.js 14 + Tailwind)

3-column layout: `ScopeSelector` (left) → `PromptWorkbench` (center) → `LivePreview` (right). The UI proxies requests to the Flask API via `API_BASE_URL` (default `http://127.0.0.1:8080`).

---

## Key Context Before Working

Before performing code generation or refactoring, read:

1. [`AGENTS.md`](./AGENTS.md) — Full AI operating directives
2. [`aiworkspace/workspaces/feasibility-insights/index.md`](./aiworkspace/workspaces/feasibility-insights/index.md) — Active domain entry point with tone, identity, and domain-specific rules
3. [`aiworkspace/skills/README.md`](./aiworkspace/skills/README.md) — Available skills (security audit, brand guidelines, etc.)

---

## Brand & UI Standards

- **Colors**: Dark Navy `#0A1128`, Container Slate `#0B192C`, Brand Red `#E31B23`, Slate Grey `#414A51`, Premier Blue `#1A73E8`, Signal Green `#34A853`
- **Typography**: `Roboto` (primary), `Google Sans`, `Inter`
- Full brand guidelines: [`aiworkspace/skills/design/brand-guidelines/SKILL.md`](./aiworkspace/skills/design/brand-guidelines/SKILL.md)

---

## Environment Setup

Copy `.env.template` to `apps/feasibility-insights/app/.env` and configure:

- `ENVIRONMENT` — `dev` | `staging` | `prod` (drives BigQuery table names)
- `USE_VERTEX_AI` / `GOOGLE_CLOUD_PROJECT` / `GOOGLE_CLOUD_LOCATION` — Vertex AI auth
- `GEMINI_MODEL` / `GEMINI_TEMPERATURE` / `GEMINI_MAX_TOKENS` — Model configuration
- `BIGQUERY_PROJECT_ID`, `LOGS_TABLE`, `CLIENT_DAILY_SUMMARY_TABLE`, `DESTINATION_TABLE` — BigQuery routing

Requires `gcloud auth application-default login` with BigQuery and Vertex AI access.

---

## OKF Document Frontmatter

Knowledge documents in `aiworkspace/` require YAML frontmatter:

```yaml
---
type: skill | dataset | table | metric | playbook | api | domain | resource | plan
name: kebab-slug
title: Title
description: Summary
status: draft | processing | finalized
tags: [tag1, tag2]
timestamp: ISO-8601
---
```