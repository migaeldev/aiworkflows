# 🤖 AI Agent Instructions & Operating Rules

This document defines the core directives, operating rules, and workflow standards for all AI agents (e.g. Antigravity, Gemini, Codex, Claude) interacting with this codebase.

---

## 🎯 Core Agent Directives

1. **Never Assume Anything**:
   - If you are unsure, if information is missing, or if requirements are underspecified, **STOP and ask the user for clarification**. Do not guess or make arbitrary assumptions.

2. **Never Hallucinate**:
   - Strictly apply Directive #1.
   - Always be **precise**, **concise**, and **accurate**.
   - Provide explicit references, citations, or rationale for decisions, code changes, and schema choices.

3. **Domain-Defined Identity & Tone**:
   - The active domain workspace (`aiworkspace/workspaces/<domain>/`) defines the **tone**, **identity**, **rules**, and **specific instructions** for that domain.
   - Agents must adopt and adhere to the identity, tone, and directives specified in the domain's `index.md` or resource configurations.

4. **UI Design & Brand Standard Rule**:
   - **Mandatory Brand Compliance**: All UI designs, web dashboards, frontend components, CSS color palettes, typography choices, background shades, and brand visuals **MUST** strictly follow the official 28East brand guidelines skill at [`aiworkspace/skills/design/brand-guidelines/SKILL.md`](./aiworkspace/skills/design/brand-guidelines/SKILL.md).
   - **Default Web Font**: Web user interfaces must use **`Roboto`** as the default primary web font (`Roboto`, `Google Sans`, `Inter`).
   - **Primary Palette**: Primary dark navy background (`#0A1128`), container slate (`#0B192C`), brand red (`#E31B23`), slate grey (`#414A51`), Google Premier Blue (`#1A73E8`), and signal green (`#34A853`).
   - **Logo Assets**: Use official brand logo assets from [`aiworkspace/skills/design/brand-guidelines/assets/`](./aiworkspace/skills/design/brand-guidelines/assets/).

5. **Package Manager Standard (PNPM)**:
   - **Mandatory Package Manager**: Always use **`pnpm`** (NOT `npm` or `yarn`) for installing dependencies (`pnpm install`), running development servers (`pnpm dev`), building applications (`pnpm build`), and executing scripts across all Node.js / Next.js / frontend projects in this repository.

6. **STRICT IMMUTABILITY GUARDRAIL & PRODUCTION README STANDARD (HOST-MODE AWARE)**:
   - **Host Mode**: This repository's production boundary is recorded in [`aiworkspace/host.md`](./aiworkspace/host.md) as `host_mode: monorepo` or `host_mode: bolt-on`. If that file is absent, assume `monorepo`. This repo's own `aiworkspace/host.md` records `monorepo`.
   - **`monorepo` mode — No Direct AI Edits to Production (`apps/`)**: No AI model or assistant is permitted to modify, edit, create, or delete any files inside `apps/[workspace]` directly unless a human user explicitly requests the `promote` step.
   - **`bolt-on` mode — No Direct AI Edits Outside `aiworkspace/`**: Everything in the repository outside `aiworkspace/` (and `.claude/`) is READ-ONLY for AI except via an explicit `promote` that writes only to the paths recorded in that workspace's `index.md` Production Target Map. `promote` MUST refuse to guess a destination for any `finalized/` file with no map entry — ask instead.
   - **Processing Stage Mandatory (both modes)**: All code generation, feature additions, refactoring, and bug fixes MUST take place inside `aiworkspace/workspaces/[workspace]/processing/`.
   - **Copy-First Workflow (both modes)**: If existing production code needs changes, the AI assistant MUST first sync/copy it into `aiworkspace/workspaces/[workspace]/processing/`, perform and test all modifications inside `processing/`, obtain human approval, pass Step 3 verification gates to move to `finalized/`, and wait for an explicit human `promote` command to move changes to production.
   - **Standalone Production README Rule (`monorepo` mode)**: During the `promote` step, `apps/[workspace]/README.md` MUST be populated as a standalone master guide containing full developer setup instructions, comprehensive environment variable documentation, and the raw `.env.template` file content embedded directly inline as a copyable code block.
   - **Root README Entry Update Rule**: During the `promote` step, the model MUST also update the root [`README.md`](./README.md) to add or update the application entry in the directory structure and quick links/navigation table.

7. **STRICT EXPLICIT HUMAN APPROVAL FOR STEP TRANSITIONS**:
   - **NO AUTOMATIC STEP ADVANCEMENT**: AI agents MUST NEVER automatically move or copy work between lifecycle steps (e.g. from `processing/` to `finalized/`, or from `finalized/` to `promote`/`apps/`) without explicit instruction from the human user.
   - **Step Pause Directive**: After completing work within the active step (e.g. performing modifications in `processing/`), the AI assistant MUST present the changes and verification status to the user and **WAIT for explicit human instruction to proceed to the next step**.

8. **SOFTWARE-ENGINEERING SKILL REFERENCE (MANDATORY ON CODE-WRITING TASKS)**:
   - **Standing Requirement, Not Optional Discovery**: Before writing, generating, or modifying any code (anywhere code-writing is otherwise permitted under Directive #6's immutability rule), the agent MUST first load and follow [`aiworkspace/skills/engineering/software-engineer/SKILL.md`](./aiworkspace/skills/engineering/software-engineer/SKILL.md).
   - **Equivalent Force**: This is equivalent in force to the `pnpm` and immutability rules above — it applies regardless of whether the skill would otherwise surface via normal registry discovery.

9. **UNIVERSAL SLASH-COMMAND DIRECTIVE (VENDOR-NEUTRAL, ALL AGENTS)**:
   - **Any agent, native slash support or not**: Whether this repository is opened in Claude Code, another CLI/IDE agent, or read by a human, `/plan`, `/resources`, `/process`, `/finalize`, `/promote` — and their aliases (canonical list in [`aiworkspace/README.md`](./aiworkspace/README.md)'s "Slash Commands & Aliases" table) — MUST be treated as a request to run the matching `aiworkspace/skills/productivity/<name>/SKILL.md`, regardless of whether that tool has its own native slash-command system.
   - **Layered, not exclusive**: In Claude Code specifically, `.claude/skills/<name>/SKILL.md` adapters additionally surface these as auto-discovered commands — that layer is additive on top of this directive, never a replacement for it.
   - **Natural language still works**: These commands are a faster on-ramp into the same skill content described elsewhere in this document — a plain-language request to "move to processing" or "run the finalize gates" invokes the identical skill and is never blocked for lack of the slash form.

---

## 🧩 Entry Point & Knowledge Architecture

This repository uses **Google's Open Knowledge Format (OKF v0.1)** hosted under `@aiworkspace` (`aiworkspace/`) coupled with a **5-Step Lifecycle Pipeline** and an **Integrated Skills Registry**.

Before performing code generation, refactoring, or query tasks, agents MUST consult:
1. **AI Workspace Architecture & Step Pipeline**: [`aiworkspace/README.md`](./aiworkspace/README.md)
2. **AI Workspaces & Skills Registry**: [`aiworkspace/index.md`](./aiworkspace/index.md)
3. **Project Available AI Skills**: [`aiworkspace/skills/README.md`](./aiworkspace/skills/README.md)
4. **Active Workspace Entry Point**: [`aiworkspace/workspaces/feasibility-insights/index.md`](./aiworkspace/workspaces/feasibility-insights/index.md)

---

## ⚡ Loading & Utilizing Project Skills (`aiworkspace/skills/`)

- Agents have access to specialized project skills located in [`aiworkspace/skills/`](./aiworkspace/skills/README.md).
- Categories include:
  - **Design Skills**: [`aiworkspace/skills/design/README.md`](./aiworkspace/skills/design/README.md) (`28east-brand-guidelines`)
  - **Engineering Skills**: [`aiworkspace/skills/engineering/README.md`](./aiworkspace/skills/engineering/README.md) (`software-engineer` — mandatory, Directive #8 — plus `code-review`, `testing`, `diagnose`, `frontend-design`)
  - **Productivity Skills**: [`aiworkspace/skills/productivity/README.md`](./aiworkspace/skills/productivity/README.md) (`plan`, `resources`, `process`, `finalize`, `promote` — the lifecycle, Directive #9 — plus `setup`, `grill-me`, `goal-driven`, `new-workspace`, `handoff`, `caveman`)
  - **Security Skills**: [`aiworkspace/skills/security/README.md`](./aiworkspace/skills/security/README.md) (`ci-cd-security-review`, `security-code-audit`)
- When user tasks require specialized workflows, consult the corresponding skill's `SKILL.md` file and follow its instructions.

---

## 🔄 The 5-Step Agent Workflow

Agents MUST execute work according to the 5-step architecture for every domain workspace (`aiworkspace/workspaces/<domain>/`):

```text
[Step 0: planning/] ──> [Step 1: resources/] ──> [Step 2: processing/] ──> [Step 3: finalized/] ──> [Step 4: promote] ──> [apps/<workspace>/]
 (Plan & Research)        (Input Context)          (Active Iteration)        (Audited Gates & Code)     (Human Deployment)      (Production Code & Specs)
```

> [!IMPORTANT]
> **MANDATORY STEP GATE**: AI agents MUST NOT automatically advance to the next step. Each step transition requires explicit human confirmation.

### Step 0: Planning (`planning/`)
- Run [`aiworkspace/skills/productivity/plan/SKILL.md`](./aiworkspace/skills/productivity/plan/SKILL.md) before populating `resources/` for a new ask.
- Determines whether this is a **Project Plan** (whole workspace, rare — e.g. via `new-workspace`) or a **Feature/Change Plan** (one unit of work, frequent). Always runs `grill-me`; offers `goal-driven` as an opt-in rather than auto-loading it.
- **CRITICAL**: Do not advance to `resources/` until the plan is presented and the human explicitly confirms (Directive #7).

### Step 1: Input & Resources (`resources/`)
- Inspect all files under `aiworkspace/workspaces/<domain>/resources/`.
- **CRITICAL**: If `resources/` is empty or lacks the required input context/specifications for the prompt, **apply Directive #1: Ask the user for context or required information** before proceeding.

### Step 2: Generation & Human Validation (`processing/`)
- Write all generated content, draft specs, code artifacts, and active iterations into `aiworkspace/workspaces/<domain>/processing/`.
- Perform iterative refinement based on human feedback inside `processing/`.
- **STOP & WAIT**: Do NOT copy or move files to `finalized/` until the human user explicitly commands you to proceed to Step 3.

### Step 3: Audit, Verification Gates & Finalization (`finalized/`)
- **Trigger**: Executed ONLY when explicitly requested by a human user after approving Step 2 work.
- Content is transferred from `processing/` to `finalized/` ONLY AFTER executing and passing **all four mandatory verification gates**:
  1. **🛡️ Security Audit Logging Checks**: Execute security skills (`ci-cd-security-review`, `security-code-audit`) and log audit findings in `log.md`.
  2. **📖 OpenAPI Specs Generation**: Create machine-readable OpenAPI 3.0 specifications (`openapi.json`) for any HTTP/REST APIs.
  3. **📄 Production-Ready Documentation**: Generate master architecture diagrams, READMEs, and deployment specs.
  4. **🧪 Final System Verification & Tests**: Run compilation/syntax checks, test suites, and confirm all system tests pass cleanly.
- **STOP & WAIT**: Do NOT proceed to Step 4 (`promote`) until the human user explicitly requests it.

### Step 4: Promote & Production Deployment (`promote` ➔ `apps/<workspace>/`)
- **Trigger**: Executed ONLY when explicitly requested by a human user.
- **Action**: Copies/moves application files from `finalized/` (or `processing/`) into `apps/<workspace>/`.
- **Cleanup**: Removes temporary files in `resources/` and `processing/`.
- **Production README Specification**: Populates `apps/<workspace>/README.md` with complete developer setup steps, full environment variable definitions, and the raw `.env.template` file content embedded inline.
- **Root README & Index Updates**: Updates the root [`README.md`](./README.md) to add or update the application entry in the directory tree and navigation table, and updates `aiworkspace/index.md` to point to `apps/<workspace>/` as the canonical production code location.

---

## 📄 OKF Formatting Standard
When creating or modifying knowledge concept documents or skills:
- Include mandatory YAML frontmatter:
  ```yaml
  ---
  type: skill | dataset | table | metric | playbook | api | domain | resource | plan
  name: skill-name                                                     # For skills
  title: Concept Title
  description: Clear summary of the concept
  status: draft | processing | finalized
  tags: [tag1, tag2]
  timestamp: ISO-8601 Timestamp
  ---
  ```
- Use relative links for cross-references.
