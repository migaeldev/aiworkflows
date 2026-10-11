---
type: index
title: AI Workspaces & Skills Registry
description: Master index of domain workspaces and skills hosted under `aiworkspace/`, listing domain purposes, lifecycle stages, available skills, and production locations.
tags: [aiworkspace, registry, index, okf, skills]
timestamp: 2026-10-11T00:00:00+02:00
---

# 🌐 AI Workspaces & Skills Registry

This registry indexes all domain workspaces and available AI skills inside `aiworkspace/`. Everything is built using **Google's Open Knowledge Format (OKF v0.1)**.

---

## 🗂️ Domain Workspaces

_No workspaces yet. `productivity/define` (`/define`) adds a row here for each workspace it creates; `productivity/promote` fills in the production location._

| Workspace Domain | Purpose & Domain Description | Entry Point | Production Location | Status |
| :--- | :--- | :--- | :--- | :--- |

---

## ⚡ Available AI Skills (`aiworkspace/skills/`)

Skills provide specialized capabilities, workflows, and tools formatted per OKF standards. All skills are model-agnostic.

| Skill Category | Category Description | Master Index |
| :--- | :--- | :--- |
| **🎨 Design** | Brand onboarding and the Material Design 3 brand guidelines (with template defaults). | [`skills/design/README.md`](./skills/design/README.md) |
| **🛠️ Engineering** | Codebase mapping, code review (dual-axis), debugging, TDD, testing (unit/integration/functional/e2e), the mandatory software-engineer practices skill, architecture, prototyping, and frontend UI. | [`skills/engineering/README.md`](./skills/engineering/README.md) |
| **🛡️ Security** | CI/CD pipeline security review, AppSec code auditing, DoS resilience, TLS, and injection audits. | [`skills/security/README.md`](./skills/security/README.md) |
| **⚡ Productivity** | The full lifecycle (define/plan/resources/process/finalize/promote), onboarding (`setup`), personas (`/persona`), workspace scaffolding, goal-driven dev, handoffs, context management, and skill authoring. | [`skills/productivity/README.md`](./skills/productivity/README.md) |

👉 **Full Skills Registry**: [`skills/README.md`](./skills/README.md)

---

## 🔄 6-Step Lifecycle Summary

0. **Step 0 (`define`)**: Create a workspace and define its core in `definition.md`, via `productivity/define` (`/define`, `/spec`).
1. **Step 1 (`plan`)**: Plan a feature, change, or batch of tasks in `planning/features/<slug>/plan.md`, via `productivity/plan`. If the workspace doesn't exist or isn't defined yet, `plan` hands off to `define` first.
2. **Step 2 (`resources/`)**: Gather the input context the plan lists. Ask the user if anything is missing.
3. **Step 3 (`processing/`)**: Work through the plan's tasks; active development and human validation.
4. **Step 4 (`finalized/`)**: Content moves from `processing/` after passing every applicable gate (security audit, API spec if an HTTP API changed, docs, tests) plus the dual-axis code review.
5. **Step 5 (`promote`)**: **Human-authorized** copy to production: `apps/<workspace>/` (`monorepo`) or the workspace's Production Target Map (`bolt-on`), per [`host.md`](./host.md).

> [!CAUTION]
> ### 🛑 IMMUTABILITY GUARDRAIL
> No AI model may edit production code directly. All changes are made inside `aiworkspace/workspaces/[workspace]/processing/` first. See `AGENTS.md` Directive #6.

---

## 🧭 Navigation & Routes

- **Architecture & Pipeline Spec**: [`README.md`](./README.md)
- **Install & Conventions**: [`host.md`](./host.md), [`project.md`](./project.md)
- **Project Context** (once created): `codebase-map.md`, `brand/`, `soul.md`
- **Master Skills Index**: [`skills/README.md`](./skills/README.md)
- **Agent Directives & Guardrails**: [`AGENTS.md`](../AGENTS.md)
