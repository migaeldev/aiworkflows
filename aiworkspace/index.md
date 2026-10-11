---
type: index
title: AI Workspaces & Skills Registry
description: Master index of domain workspaces and project skills hosted under `@aiworkspace`, listing domain purposes, 5-step lifecycle stages, available skills, and OKF resources.
tags: [aiworkspace, registry, index, okf, skills]
timestamp: 2026-10-08T20:42:00+02:00
---

# 🌐 AI Workspaces & Skills Registry

This registry indexes all domain knowledge workspaces and available AI skills inside `@aiworkspace`. Everything is built using **Google's Open Knowledge Format (OKF v0.1)**.

---

## 🗂️ Domain Workspaces

| Workspace Domain | Purpose & Domain Description | Entry Point | Canonical Production App | Stages | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`feasibility-insights`** | Telemetry MoM analysis, spatial GIS lookups, Vertex AI Gemini Enterprise insights, and Next.js Prompt Workbench. | [`workspaces/feasibility-insights/index.md`](./workspaces/feasibility-insights/index.md) | [`apps/feasibility-insights/`](../apps/feasibility-insights/) | `planning/`<br>`resources/`<br>`processing/`<br>`finalized/`<br>`promote` | 🟢 Active |
| **`etl-pipeline`** | Multi-format geospatial data ingestion/validation/publishing into a PostgreSQL+PostGIS medallion warehouse. Consumes `task-management-system`'s `task-engine` for task/pipeline execution (extracted 2026-10-04). | [`workspaces/etl-pipeline/index.md`](./workspaces/etl-pipeline/index.md) | Not yet promoted | `planning/`<br>`resources/`<br>`processing/`<br>`finalized/`<br>`promote` | 🟢 Active |
| **`task-management-system`** | Generic, domain-agnostic task/pipeline execution engine (`task-engine`) — durable Postgres queuing, scheduling, health-checks, cancellation. Extracted from `etl-pipeline` 2026-10-04; consumed as a library by it and future domains. | [`workspaces/task-management-system/index.md`](./workspaces/task-management-system/index.md) | Not yet promoted | `planning/`<br>`resources/`<br>`processing/`<br>`finalized/`<br>`promote` | 🟢 Active |
| **`bulk-feasibility-checker`** | Async/offline batch feasibility checking against 28East Coverage API, powered by `task-engine`. Processes multiple locations concurrently with bounded safety-rails. | [`workspaces/bulk-feasibility-checker/index.md`](./workspaces/bulk-feasibility-checker/index.md) | Not yet promoted | `planning/`<br>`resources/`<br>`processing/`<br>`finalized/`<br>`promote` | 🟢 Active |
| **`pluscode-sub-addressing`** | Hybrid research blueprint, operational workflows, and data contracts for informal settlement addressing in South Africa (e.g. Alexandra). Solves sub-dwelling granularity, eliminates ad-hoc plate printing bottlenecks, and binds ONT devices on-site. | [`workspaces/pluscode-sub-addressing/index.md`](./workspaces/pluscode-sub-addressing/index.md) | Not yet promoted | `planning/`<br>`resources/`<br>`processing/`<br>`finalized/`<br>`promote` | 🟢 Active |
| **`ui-test-agent`** | Autonomous Playwright UI testing agent powered by Google ADK & Gemini Enterprise. Enables technical and non-technical testers to run tests from any URL, persist declarative scenarios, and inspect videos/screenshots. | [`workspaces/ui-test-agent/index.md`](./workspaces/ui-test-agent/index.md) | Not yet promoted | `planning/`<br>`resources/`<br>`processing/`<br>`finalized/`<br>`promote` | 🟢 Active |
| **`qa-automation`** | Chat-driven Playwright UI testing agent (Google ADK on Agent Runtime, registered in Gemini Enterprise, with a Cloud Run Python runner) for 28East's Google Maps-based client UIs. Testers turn a URL plus plain-English steps into saved, deterministically replayable scenarios with screenshots/video/trace reports. Approved scenarios export as `@playwright/test` bundles. | [`workspaces/qa-automation/index.md`](./workspaces/qa-automation/index.md) | Not yet promoted | `planning/`<br>`resources/`<br>`processing/`<br>`finalized/`<br>`promote` | 🟢 Active |

---

## ⚡ Project Available AI Skills (`@aiworkspace/skills`)

Skills provide specialized capabilities, workflows, and tools formatted per OKF standards. All skills are model-agnostic.

| Skill Category | Category Description | Master Index | Total Skills |
| :--- | :--- | :--- | :--- |
| **🎨 Design** | Visual design, 28East branding, and user interface aesthetics. | [`skills/design/README.md`](./skills/design/README.md) | 1 Skill |
| **🛠️ Engineering** | Code review (dual-axis), debugging loops, TDD, testing (unit/integration/functional/e2e), the mandatory software-engineer practices skill, visual iteration, and frontend UI. | [`skills/engineering/README.md`](./skills/engineering/README.md) | 7 Skills |
| **🛡️ Security** | CI/CD pipeline security review, AppSec code auditing, DoS resilience, TLS, and SQL injection. | [`skills/security/README.md`](./skills/security/README.md) | 5 Skills |
| **⚡ Productivity** | Token-saving, context management, goal-driven dev, the full lifecycle (plan/resources/process/finalize/promote), repo onboarding (`setup`), handoffs, workspace scaffolding, and skill authoring. | [`skills/productivity/README.md`](./skills/productivity/README.md) | 13 Skills |

👉 **Full Skills Registry**: [`aiworkspace/skills/README.md`](./skills/README.md)

---

## 🔄 5-Step Lifecycle Summary

0. **Step 0 (`planning/`)**: Project Plan or Feature/Change Plan, via `productivity/plan`. Always runs `grill-me`; `goal-driven` only if the user opts in. Gates into `resources/`.
1. **Step 1 (`resources/`)**: Input context & specifications. Prompt user if empty.
2. **Step 2 (`processing/`)**: Application & content generation. Active development workspace and human validation.
3. **Step 3 (`finalized/`)**: Content transferred from `processing/` to `finalized/` after passing 4 verification gates: (1) Security audit logging, (2) OpenAPI specs generation, (3) Production docs, and (4) System tests verification.
4. **Step 4 (`promote`)**: **Human-authorized deployment action**. Moves production application code from `finalized/` (or `processing/`) to `apps/[workspace]/`, clears input `resources/`, and updates production entry pointers.

> [!CAUTION]
> ### 🛑 IMMUTABILITY GUARDRAIL
> No AI model can edit `apps/[workspace]` directly. All changes must be executed inside `aiworkspace/workspaces/[workspace]/processing/` first.

---

## 🧭 Navigation & Routes

- **Architecture & Pipeline Spec**: [`aiworkspace/README.md`](./README.md)
- **Master Skills Index**: [`aiworkspace/skills/README.md`](./skills/README.md)
- **Agent Directives & Guardrails**: [`AGENTS.md`](../AGENTS.md)
