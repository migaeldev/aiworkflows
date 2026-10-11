---
type: domain
title: "<Workspace Title> Domain Workspace"
description: Central knowledge index for the <workspace> domain containing domain identity, planning artifacts, resources, processing iterations, finalized audited artifacts, and the canonical production pointer.
tags: [domain, template, index]
timestamp: 2026-09-09T13:40:45+02:00
---

# <Workspace Title> Domain Knowledge Workspace

Welcome to the **<Workspace Title>** domain workspace, formatted according to the Google Open Knowledge Format (OKF v0.1) and the **5-Step Lifecycle Architecture**.

---

## 🚀 Production Application Location

_Check [`aiworkspace/host.md`](../../host.md)'s `host_mode` before filling this in — it determines which of the two subsections below applies. Delete whichever one doesn't._

### If `host_mode: monorepo` (the default; this repo's own mode)

- **Canonical Production Code**: `apps/<workspace>/`
- **Production README**: `apps/<workspace>/README.md`

> [!CAUTION]
> ### 🛑 STRICT AI ASSISTANT RULE & IMMUTABILITY GUARDRAIL
> **No AI model or assistant is permitted to modify, create, or delete any files directly within `apps/<workspace>/`.**
>
> - **Human Approval Requirement**: All production deployments require explicit human authorization via a `promote` command.
> - **Iteration Location**: All feature additions, bug fixes, refactoring, and code changes MUST take place inside [`aiworkspace/workspaces/<workspace>/processing/`](./processing/README.md).
> - **Copy-First Strategy**: If existing production code requires updates, first sync/copy it back into `processing/`, perform and test all modifications there, gain human approval, pass Step 3 verification gates to move to `finalized/`, and wait for the human to trigger `promote`.

### If `host_mode: bolt-on` (`aiworkspace` added into an existing repo with no `apps/` folder)

> [!CAUTION]
> ### 🛑 STRICT AI ASSISTANT RULE & IMMUTABILITY GUARDRAIL
> **No AI model or assistant is permitted to modify, create, or delete anything outside `aiworkspace/` (and `.claude/`) except via the Production Target Map below, through an explicit `promote` command.**
>
> - **Human Approval Requirement**: All production deployments require explicit human authorization via a `promote` command.
> - **Iteration Location**: All feature additions, bug fixes, refactoring, and code changes MUST take place inside [`aiworkspace/workspaces/<workspace>/processing/`](./processing/README.md).
> - **Copy-First Strategy**: If existing production code requires updates, first sync/copy it back into `processing/`, perform and test all modifications there, gain human approval, pass Step 3 verification gates to move to `finalized/`, and wait for the human to trigger `promote`.

#### 🎯 Production Target Map

| `finalized/` path | Host repo destination |
|---|---|
| _[e.g. `finalized/handlers/foo.py`]_ | _[e.g. `src/handlers/foo.py`]_ |

`productivity/promote` refuses to guess a destination for any `finalized/` file not listed here — it asks instead.

---

## 🎭 Domain Identity, Tone & Specific Instructions

_Filled in by `productivity/plan` running in Project Plan mode (invoked via `productivity/new-workspace`'s Step 3) — this section stays a placeholder until that interview runs. Never pre-fill it with another workspace's real content._

- **Domain Purpose**: _[placeholder]_
- **Identity & Persona**: _[placeholder]_
- **Tone**: _[placeholder]_
- **Domain Directives**: _[placeholder — numbered list of constraints]_

---

## 🗂️ 5-Step Workspace Lifecycle Pipeline

0. **Step 0 - Planning**: [`planning/`](./planning/README.md)
   - Project Plan and Feature/Change Plans, research notes, and (for large work) a decision map. Produced by `productivity/plan`.
1. **Step 1 - Resources Catalog**: [`resources/`](./resources/README.md)
   - Input context, schemas, metrics definitions, and initial specifications, informed by Step 0.
2. **Step 2 - Processing & Iteration**: [`processing/`](./processing/README.md)
   - Generated content, human validation feedback, and active code iterations.
3. **Step 3 - Finalized & Audited**: [`finalized/`](./finalized/README.md)
   - Audited code, dual-axis review (`review.md`), security logs, and test results.
4. **Step 4 - Promote**: see "Production Application Location" above (`apps/<workspace>/` in `monorepo` mode, or the Production Target Map in `bolt-on` mode)
   - Human-authorized deployment.

---

## 📜 Audit & History

- **Domain Change Log**: [`log.md`](./log.md)
