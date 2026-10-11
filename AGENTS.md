# 🤖 AI Agent Instructions & Operating Rules

This document defines the core directives, operating rules, and workflow standards for all AI agents (e.g. Claude, Codex, Gemini, Antigravity) working in a repository that has the `aiworkspace` harness installed.

It is project-agnostic. Everything specific to *this* repository lives in files written by `productivity/setup`:

- [`aiworkspace/host.md`](./aiworkspace/host.md): how the harness is installed (`host_mode`).
- [`aiworkspace/project.md`](./aiworkspace/project.md): this project's conventions (stack, commands, comment policy, git commit policy, context-file status, extra directives).
- `aiworkspace/codebase-map.md`: a map of the host codebase, saying where and how to make changes (created with the user's permission).
- `aiworkspace/brand/`: the brand, with `brand.md` (values, UI technology, and a manifest of every file) plus logos, fonts, tokens, source documents, and reference artifacts (when a brand has been onboarded).
- `aiworkspace/soul.md`: the project persona agents adopt (workspaces may add their own `soul.md`).

> [!IMPORTANT]
> If `aiworkspace/host.md` still reads `host_mode: unset`, the harness has not been initialized. Run [`productivity/setup`](./aiworkspace/skills/productivity/setup/SKILL.md) before any lifecycle work.

---

## 🎯 Core Agent Directives

1. **Never Assume Anything**:
   - If you are unsure, if information is missing, or if requirements are underspecified, **STOP and ask the user for clarification**. Do not guess or make arbitrary assumptions.

2. **Never Hallucinate**:
   - Strictly apply Directive #1.
   - Always be **precise**, **concise**, and **accurate**.
   - Provide explicit references, citations, or rationale for decisions, code changes, and schema choices.

3. **Persona & Domain Identity**:
   - **Adopt the project persona**: if `aiworkspace/soul.md` exists, work as the project it describes. Use its voice, vocabulary, languages, frameworks, patterns, naming, and comment style.
   - **Layer the workspace persona**: if the active workspace has its own `soul.md`, its sections replace the matching sections of the project soul, and missing sections are inherited.
   - **Domain rules**: the workspace's `index.md` holds its purpose, directives, and glossary. Follow them.
   - A soul governs **style**, never rules. Directives in this file and in `project.md` always win. If a soul conflicts with them, follow the rule and flag the conflict.
   - Create or change a persona with `/persona` ([`productivity/persona`](./aiworkspace/skills/productivity/persona/SKILL.md)).

4. **UI Design & Brand Standard Rule**:
   - All UI/UX design and frontend work **MUST** follow [`design/brand-guidelines`](./aiworkspace/skills/design/brand-guidelines/SKILL.md), together with `frontend-design` and `visual-iteration`.
   - **Before any UI/UX design work, check Brand in `project.md`:**
     - `pending` → first ask the user whether to onboard the brand, per [`design/brand-onboarding`](./aiworkspace/skills/design/brand-onboarding/SKILL.md). The answer is one of: onboard now (grill-me on brand and UI technology → `aiworkspace/brand/`), always use template defaults, or not now (defaults for this task only).
     - `template-defaults` → use `brand-guidelines`' default values.
     - `custom` → use `aiworkspace/brand/brand.md` and only the brand files listed in its manifest.
   - Never invent brand colors, fonts, or logos.

5. **Project Conventions & Codebase Context**:
   - Follow the conventions recorded in [`aiworkspace/project.md`](./aiworkspace/project.md): package manager, languages/stack, build/test/lint commands, comment policy, git commit policy, and any project-specific directives listed there.
   - **Commit policy is opt-in, not a default.** `engineering/software-engineer`'s commit-at-task-granularity behavior and `productivity/process`'s auto-commit step only fire according to `project.md`'s **Commit policy** (`auto` / `ask` / `manual`, set by `productivity/setup` or the first time it comes up). Never commit without checking this setting first, and never assume `auto`.
   - Project-specific directives in `project.md` carry the same force as the directives in this file.
   - **Before planning or writing changes to host code, consult `aiworkspace/codebase-map.md`** (if present) for where the change belongs and how to write it: module map, patterns, conventions, change recipes. Match what's there. If the code contradicts the map, or the map looks stale, say so and offer to re-map ([`engineering/codebase-map`](./aiworkspace/skills/engineering/codebase-map/SKILL.md)).
   - If a convention isn't recorded, infer it from the host repo (lockfiles, manifests, CI config, the codebase map), then **confirm with the user** and record it in `project.md`. Never silently pick one.

6. **STRICT IMMUTABILITY GUARDRAIL & PRODUCTION README STANDARD (HOST-MODE AWARE)**:
   - **Host Mode**: The production boundary is recorded in [`aiworkspace/host.md`](./aiworkspace/host.md) as `host_mode: monorepo` or `host_mode: bolt-on`.
   - **`monorepo` mode — No Direct AI Edits to Production (`apps/`)**: No AI model or assistant may modify, create, or delete any files inside `apps/[workspace]` directly unless a human explicitly requests the `promote` step.
   - **`bolt-on` mode — No Direct AI Edits Outside `aiworkspace/`**: Everything in the repository outside `aiworkspace/` (and agent-tool folders such as `.claude/`) is READ-ONLY for AI except via an explicit `promote` that writes only to the paths recorded in that workspace's `index.md` Production Target Map. `promote` MUST refuse to guess a destination for any `finalized/` file with no map entry — ask instead.
   - **Processing Stage Mandatory (both modes)**: All code generation, feature additions, refactoring, and bug fixes MUST take place inside `aiworkspace/workspaces/[workspace]/processing/`.
   - **Copy-First Workflow (both modes)**: If existing production code needs changes, first copy it into `aiworkspace/workspaces/[workspace]/processing/`, perform and test all modifications there, obtain human approval, pass the Step 4 gates to move to `finalized/`, and wait for an explicit human `promote` command.
   - **Standalone Production README Rule (`monorepo` mode)**: During `promote`, `apps/[workspace]/README.md` MUST be a standalone guide: developer setup, environment variable documentation, and the `.env.template` content (if the app has one) embedded inline as a copyable code block.
   - **Root README Entry Update Rule (`monorepo` mode)**: During `promote`, also update the root `README.md` to add or update the application entry.

7. **STRICT EXPLICIT HUMAN APPROVAL FOR STEP TRANSITIONS**:
   - **NO AUTOMATIC STEP ADVANCEMENT**: AI agents MUST NEVER automatically move or copy work between lifecycle steps (e.g. from `processing/` to `finalized/`, or from `finalized/` to production) without explicit instruction from the human user.
   - **Step Pause Directive**: After completing work within the active step, present the changes and verification status and **WAIT for explicit human instruction to proceed to the next step**.

8. **SOFTWARE-ENGINEERING SKILL REFERENCE (MANDATORY ON CODE-WRITING TASKS)**:
   - **Standing Requirement, Not Optional Discovery**: Before writing, generating, or modifying any code (anywhere code-writing is permitted under Directive #6), the agent MUST first load and follow [`aiworkspace/skills/engineering/software-engineer/SKILL.md`](./aiworkspace/skills/engineering/software-engineer/SKILL.md).
   - **Equivalent Force**: This applies regardless of whether the skill would otherwise surface via normal registry discovery.

9. **UNIVERSAL SLASH-COMMAND DIRECTIVE (VENDOR-NEUTRAL, ALL AGENTS)**:
   - **Any agent, native slash support or not**: `/setup`, `/map`, `/brand`, `/persona`, `/define`, `/plan`, `/resources`, `/process`, `/finalize`, `/promote` — and their aliases (canonical list in [`aiworkspace/README.md`](./aiworkspace/README.md)'s "Slash Commands & Aliases" table) — MUST be treated as a request to run the skill that table maps them to, regardless of whether the tool has its own slash-command system.
   - **Layered, not exclusive**: Tool-specific adapters (e.g. `.claude/skills/<name>/SKILL.md` in Claude Code) may additionally surface these as native commands — that layer is additive, never a replacement.
   - **Natural language still works**: A plain-language request to "move to processing" or "run the finalize gates" invokes the identical skill.

10. **HUMANIZER SKILL REFERENCE (MANDATORY ON GENERATED PROSE)**:
    - **Standing Requirement, Not Optional Discovery**: Before finalizing any generated prose meant for a human reader — documentation, README content, commit messages, PR/issue descriptions, workspace `definition.md`/`plan.md` narrative sections, chat responses, or any other written content this harness produces — the agent MUST load and follow [`aiworkspace/skills/productivity/humanizer/SKILL.md`](./aiworkspace/skills/productivity/humanizer/SKILL.md) to strip AI writing tells before the content is presented or committed.
    - **Equivalent Force**: This applies regardless of whether the skill would otherwise surface via normal registry discovery, the same way Directive #8 applies to code.
    - **Scope Exclusions**: Code, config, data, and verbatim quoted/pasted material are untouched by this directive — only prose the agent itself is authoring is in scope.

---

## 🧩 Entry Point & Knowledge Architecture

The harness uses **Google's Open Knowledge Format (OKF v0.1)** under `aiworkspace/`, coupled with a **6-Step Lifecycle Pipeline** and an **Integrated Skills Registry**.

Before performing code generation, refactoring, or query tasks, agents MUST consult:
1. **Install & Conventions**: [`aiworkspace/host.md`](./aiworkspace/host.md) and [`aiworkspace/project.md`](./aiworkspace/project.md)
2. **Project Context** (each exists once setup has created it): `aiworkspace/soul.md` (persona), `aiworkspace/codebase-map.md` (where and how to change code), `aiworkspace/brand/` (brand values & files)
3. **Architecture & Step Pipeline**: [`aiworkspace/README.md`](./aiworkspace/README.md)
4. **Workspaces & Skills Registry**: [`aiworkspace/index.md`](./aiworkspace/index.md). It lists every domain workspace; open the active one's `index.md` (and its `soul.md`, if present)
5. **Available Skills**: [`aiworkspace/skills/README.md`](./aiworkspace/skills/README.md) — when the right skill (or whether to also spawn a specialist agent) isn't obvious, consult [`skills/using-agent-skills`](./aiworkspace/skills/using-agent-skills/SKILL.md) first.
6. **Specialist Agents**: [`aiworkspace/agents/README.md`](./aiworkspace/agents/README.md) — fresh, isolated reviewer personas (code-reviewer, test-engineer, security-auditor, performance-auditor) spawned for a second opinion, each loading the skills above.

If the task's workspace is ambiguous (several are listed in `index.md`), ask which one applies.

---

## ⚡ Loading & Utilizing Project Skills (`aiworkspace/skills/`)

- Agents have access to specialized skills in [`aiworkspace/skills/`](./aiworkspace/skills/README.md):
  - **Design**: [`design/README.md`](./aiworkspace/skills/design/README.md) (`brand-guidelines`, `brand-onboarding` — Directive #4)
  - **Engineering**: [`engineering/README.md`](./aiworkspace/skills/engineering/README.md) (`software-engineer` — mandatory, Directive #8 — plus `codebase-map`, `code-review`, `testing`, `diagnose`, `frontend-design`, …)
  - **Productivity**: [`productivity/README.md`](./aiworkspace/skills/productivity/README.md) (`define`, `plan`, `resources`, `process`, `finalize`, `promote` — the lifecycle, Directive #9 — plus `setup`, `persona`, `grill-me`, `goal-driven`, `handoff`, `humanizer` — mandatory on generated prose, Directive #10, …)
  - **Security**: [`security/README.md`](./aiworkspace/skills/security/README.md) (`security-code-audit`, `ci-cd-security-review`, …)
- When a task requires a specialized workflow, consult the matching skill's `SKILL.md` and follow its instructions.

---

## 🔄 The 6-Step Agent Workflow

Every domain workspace (`aiworkspace/workspaces/<domain>/`) follows:

```text
[0: define] ──> [1: plan] ──> [2: resources/] ──> [3: processing/] ──> [4: finalized/] ──> [5: promote] ──> [production]
 workspace core   feature/tasks   input context      active iteration     audited & gated     human-only      apps/<workspace>/ or Target Map
 definition.md    planning/
```

> [!IMPORTANT]
> **MANDATORY STEP GATE**: AI agents MUST NOT automatically advance to the next step. Each step transition requires explicit human confirmation.

### Step 0: Define (`definition.md`)
- Run [`productivity/define`](./aiworkspace/skills/productivity/define/SKILL.md) (`/define`, `/spec`) to create a workspace and define its core: purpose, scope, users, success criteria, directives, production target, known unknowns, and candidate features.
- Done once per workspace and revised rarely (redefine mode). Always runs `grill-me`; offers `goal-driven` as an opt-in.
- **CRITICAL**: No feature planning in a workspace until its definition is presented and the human confirms it (Directive #7).

### Step 1: Plan (`planning/`)
- Run [`productivity/plan`](./aiworkspace/skills/productivity/plan/SKILL.md) (`/plan`) for each feature, change, or batch of work. It writes `planning/features/<slug>/plan.md` with decisions, an ordered **task list**, the **resources needed**, and the testing approach.
- **If the target workspace doesn't exist or isn't defined, `plan` hands off to `define` first.** Asks that fall outside the workspace's defined scope are flagged, never quietly absorbed.
- **CRITICAL**: Do not advance to `resources/` until the plan is presented and the human confirms.

### Step 2: Input & Resources (`resources/`)
- Gather what the plan's **Resources Needed** section lists into `aiworkspace/workspaces/<domain>/resources/`.
- **CRITICAL**: If `resources/` is empty or lacks the required context, **apply Directive #1 and ask the user** before proceeding.

### Step 3: Generation & Human Validation (`processing/`)
- Work through the plan's tasks, writing all generated content, draft specs, and code into `aiworkspace/workspaces/<domain>/processing/`, and ticking tasks off in `plan.md`.
- Iterate based on human feedback inside `processing/`.
- **STOP & WAIT**: Do NOT move files to `finalized/` until the human explicitly asks for Step 4.

### Step 4: Audit, Verification Gates & Finalization (`finalized/`)
- **Trigger**: ONLY when explicitly requested by the human after approving Step 3 work.
- Content moves from `processing/` to `finalized/` ONLY AFTER passing **every applicable gate**. A gate that does not apply is recorded as `N/A` with a one-line reason in `log.md` — never silently skipped:
  1. **🛡️ Security Audit** *(always)*: Run the relevant security skills and log findings in `log.md`.
  2. **📖 API Specification** *(if the work exposes or changes an HTTP/REST API)*: Generate or update an OpenAPI 3.x spec (`openapi.json`/`openapi.yaml`).
  3. **📄 Production-Ready Documentation** *(always)*: READMEs and, where the change warrants them, architecture diagrams and deployment notes.
  4. **🧪 Verification & Tests** *(always)*: Run the project's build/lint/test commands from `project.md`. If the project has no test suite, say so and record what verification was done instead.
- Plus the dual-axis [`engineering/code-review`](./aiworkspace/skills/engineering/code-review/SKILL.md) against the plan and the workspace definition, persisted to `finalized/review.md`.
- **STOP & WAIT**: Do NOT proceed to Step 5 until the human explicitly requests it.

### Step 5: Promote & Production Deployment
- **Trigger**: ONLY when explicitly requested by the human. Run [`productivity/promote`](./aiworkspace/skills/productivity/promote/SKILL.md).
- **`monorepo`**: copies `finalized/` into `apps/<workspace>/`, writes its standalone README, and updates the root `README.md`.
- **`bolt-on`**: copies each `finalized/` file to its destination in the workspace's Production Target Map; unmapped files stop the promote.
- **Both modes**: updates `aiworkspace/index.md` with the production location and clears temporary files in `resources/` and `processing/`.

---

## 📄 OKF Formatting Standard
When creating or modifying knowledge documents or skills:
- Include mandatory YAML frontmatter:
  ```yaml
  ---
  type: skill | agent | dataset | table | metric | playbook | api | domain | resource | plan
  name: skill-name                                                     # For skills/agents
  title: Concept Title
  description: Clear summary of the concept
  status: draft | processing | finalized
  tags: [tag1, tag2]
  timestamp: ISO-8601 Timestamp
  ---
  ```
- Use relative links for cross-references.
- **`## Rationalizations` (optional)**: any `type: skill` or `type: domain` document whose process has a step agents are tempted to skip, rush, or silently weaken MAY include a table of `Excuse | Why it's wrong | Do this instead`. Placed right after the document's trigger/intro. See [`productivity/write-a-skill`](./aiworkspace/skills/productivity/write-a-skill/SKILL.md) for the exact format and when to add one.
