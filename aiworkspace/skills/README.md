---
type: index
title: Project Skills Registry
description: Master index of project AI skills categorized into design, engineering, security, and productivity under `aiworkspace/skills/`.
tags: [skills, registry, index, okf]
timestamp: 2026-09-16T16:01:29+02:00
---

# ⚡ Project Skills Registry (`aiworkspace/skills/`)

This registry indexes all specialized project skills available to AI agents operating in this repository. All skills adhere to **Google's Open Knowledge Format (OKF v0.1)** and include mandatory frontmatter metadata (`type: skill`).

A sibling registry, [`aiworkspace/agents/README.md`](../agents/README.md), holds specialist reviewer personas (`type: agent`) that load and use the skills below as fresh, isolated subagents for a second opinion. Start at [`using-agent-skills`](./using-agent-skills/SKILL.md) below if it isn't obvious which skill or agent a task needs.

---

## 🗂️ Skill Categories

```text
aiworkspace/skills/
├── README.md                          # Master Skills Index & Registry (This file)
├── using-agent-skills/                # 🧭 Meta: router — task shape → skill or agent to load
├── design/                            # Branding, visual design, and UI specs
│   ├── README.md                      # Design Skills Index
│   ├── brand-guidelines/              # Design system (M3) + template default brand values
│   └── brand-onboarding/              # Brand & UI-tech onboarding → aiworkspace/brand/ (/brand)
├── engineering/                       # Code review, debugging, TDD, testing, architecture, and frontend UI
│   ├── README.md                      # Engineering Skills Index
│   ├── api-interface-design/          # Contract-first design: Hyrum's Law, One-Version Rule, error semantics
│   ├── code-review/                   # Dual-axis (standards + spec-fidelity) review
│   ├── codebase-map/                  # Permissioned codebase map → aiworkspace/codebase-map.md (/map)
│   ├── codebase-design/               # Module depth/seam/interface vocabulary & principles
│   ├── deprecation-migration/         # Code-as-liability mindset, deprecation & migration patterns
│   ├── diagnose/                      # Hard bug debugging loop
│   ├── domain-modeling/               # GLOSSARY.md ubiquitous-language upkeep
│   ├── frontend-design/               # Production frontend UI generation
│   ├── improve-codebase-architecture/ # Deepening-opportunity scan + visual HTML report
│   ├── observability/                 # Structured logging, RED metrics, tracing, symptom-based alerting
│   ├── prototype/                     # Throwaway logic/UI prototypes to answer a design question
│   ├── research/                      # Background-agent research into a cited Markdown file
│   ├── software-engineer/             # Mandatory code-writing discipline persona
│   ├── test-first/                    # Red-green-refactor loop
│   ├── testing/                       # Unit/integration/functional/e2e test-type router
│   ├── visual-iteration/              # Screenshot-driven UI feedback loop
│   └── web-performance-audit/         # Core Web Vitals, bundle size & render-blocking audit
├── security/                          # CI/CD security, code audit, DoS, TLS & SQL injection
│   ├── README.md                      # Security Skills Index
│   ├── ci-cd-security-review/         # Pipeline & DevSecOps security audit
│   ├── security-code-audit/           # OWASP Top 10 & AppSec code audit
│   ├── dos-resilience-audit/          # DoS, ReDoS, payload caps & rate limiting audit
│   ├── mitm-prevention-audit/         # TLS/SSL, transport security & HSTS audit
│   └── sql-injection-audit/           # Parameterized query & SQL injection audit
└── productivity/                      # Handoffs, context compression, and skill authoring
    ├── README.md                      # Productivity Skills Index
    ├── caveman/                       # Concise token-saving response mode
    ├── context-management/            # Context/session memory management
    ├── define/                        # Step 0 workspace creation & core definition (/define, /spec)
    ├── finalize/                      # Step 4 gates + dual-axis review
    ├── goal-driven/                   # Declarative success-criteria workflow
    ├── grill-me/                      # Interactive requirement grilling
    ├── handoff/                       # Structured session context summary
    ├── humanizer/                     # Remove AI writing tells from prose
    ├── persona/                       # soul.md persona, project or workspace (/persona)
    ├── plan/                          # Step 1 feature plans & task lists
    ├── process/                       # Step 3 iteration through the task list (re-invocable)
    ├── promote/                       # Step 5 human-authorized deployment
    ├── resources/                     # Step 2 input-context catalog/request
    ├── setup/                         # One-time repo onboarding (host_mode)
    └── write-a-skill/                 # Standardized OKF skill authoring tool
```

---

## 📋 Master Index of Available Skills

| Category | Skill Identifier | Title | Primary Purpose / Trigger | Index File |
| :--- | :--- | :--- | :--- | :--- |
| **🧭 Meta** | `using-agent-skills` | Using Agent Skills | Router — task shape → skill or specialist agent to load; not a worker itself. | [`using-agent-skills/SKILL.md`](./using-agent-skills/SKILL.md) |
| **🎨 Design** | `brand-guidelines` | Brand Guidelines | M3 design system filled with `brand/brand.md` values or template defaults; pairs with `frontend-design`/`visual-iteration`. | [`design/brand-guidelines/SKILL.md`](./design/brand-guidelines/SKILL.md) |
| **🎨 Design** | `brand-onboarding` | Brand Onboarding | Detect tokens + grill-me on brand & UI tech → `aiworkspace/brand/` (values + files), or choose template defaults (`/brand`). | [`design/brand-onboarding/SKILL.md`](./design/brand-onboarding/SKILL.md) |
| **🛠️ Engineering** | `api-interface-design` | API & Interface Design | Contract-first design for anything consumed outside your control — Hyrum's Law, One-Version Rule, error semantics, boundary validation. | [`engineering/api-interface-design/SKILL.md`](./engineering/api-interface-design/SKILL.md) |
| **🛠️ Engineering** | `code-review` | Code Review Skill | Dual-axis (standards + spec-fidelity) code quality audit, persisted to `finalized/review.md`. | [`engineering/code-review/SKILL.md`](./engineering/code-review/SKILL.md) |
| **🛠️ Engineering** | `codebase-map` | Codebase Map | Permissioned, evidence-cited map of stack, structure, patterns, conventions & change recipes (`/map`). | [`engineering/codebase-map/SKILL.md`](./engineering/codebase-map/SKILL.md) |
| **🛠️ Engineering** | `codebase-design` | Codebase Design Vocabulary | Module/interface/depth/seam/adapter/leverage/locality vocabulary, the deletion test, and the design-it-twice pattern. | [`engineering/codebase-design/SKILL.md`](./engineering/codebase-design/SKILL.md) |
| **🛠️ Engineering** | `deprecation-migration` | Deprecation & Migration | Code-as-liability mindset, compulsory/advisory deprecation, migration patterns, zombie-code removal. | [`engineering/deprecation-migration/SKILL.md`](./engineering/deprecation-migration/SKILL.md) |
| **🛠️ Engineering** | `diagnose` | Diagnosis & Debugging Loop | Deep bug analysis, root cause diagnosis & fixes. | [`engineering/diagnose/SKILL.md`](./engineering/diagnose/SKILL.md) |
| **🛠️ Engineering** | `domain-modeling` | Domain Modeling | Keep `GLOSSARY.md` ubiquitous language current as domain concepts are named or sharpened. | [`engineering/domain-modeling/SKILL.md`](./engineering/domain-modeling/SKILL.md) |
| **🛠️ Engineering** | `frontend-design` | Frontend UI Design Skill | Distinctive, production-grade frontend UI. | [`engineering/frontend-design/SKILL.md`](./engineering/frontend-design/SKILL.md) |
| **🛠️ Engineering** | `improve-codebase-architecture` | Improve Codebase Architecture | Scan for deepening opportunities, present a visual HTML report, then grill through the pick. | [`engineering/improve-codebase-architecture/SKILL.md`](./engineering/improve-codebase-architecture/SKILL.md) |
| **🛠️ Engineering** | `observability` | Observability & Instrumentation | Structured logging, RED metrics, tracing, symptom-based alerting — instrument as you build. | [`engineering/observability/SKILL.md`](./engineering/observability/SKILL.md) |
| **🛠️ Engineering** | `prototype` | Prototype | Throwaway logic demo or switchable UI variants to answer a design question. | [`engineering/prototype/SKILL.md`](./engineering/prototype/SKILL.md) |
| **🛠️ Engineering** | `research` | Research | Background-agent investigation against primary sources, captured as a cited Markdown file. | [`engineering/research/SKILL.md`](./engineering/research/SKILL.md) |
| **🛠️ Engineering** | `software-engineer` | Software Engineer Practices | Mandatory plan/test/review discipline for any code-writing task. | [`engineering/software-engineer/SKILL.md`](./engineering/software-engineer/SKILL.md) |
| **🛠️ Engineering** | `test-first` | Test-First Development | Red-green-refactor loop: failing test before implementation. | [`engineering/test-first/SKILL.md`](./engineering/test-first/SKILL.md) |
| **🛠️ Engineering** | `testing` | Testing: Pick the Right Type | Unit/integration/functional/e2e test-type router with per-type conventions. | [`engineering/testing/SKILL.md`](./engineering/testing/SKILL.md) |
| **🛠️ Engineering** | `visual-iteration` | Visual Iteration | Screenshot-driven UI feedback loop against a target design. | [`engineering/visual-iteration/SKILL.md`](./engineering/visual-iteration/SKILL.md) |
| **🛠️ Engineering** | `web-performance-audit` | Web Performance Audit Skill | Core Web Vitals, bundle size/code-splitting, render-blocking resources, and client-side fetch waste. | [`engineering/web-performance-audit/SKILL.md`](./engineering/web-performance-audit/SKILL.md) |
| **🛡️ Security** | `ci-cd-security-review` | CI/CD Pipeline Security Review | Pipeline security, secrets scanning, IAM & artifact audit. | [`security/ci-cd-security-review/SKILL.md`](./security/ci-cd-security-review/SKILL.md) |
| **🛡️ Security** | `security-code-audit` | Security Code Audit Skill | OWASP Top 10 vulnerabilities, CORS & AppSec audit. | [`security/security-code-audit/SKILL.md`](./security/security-code-audit/SKILL.md) |
| **🛡️ Security** | `dos-resilience-audit` | Application DoS & Resource Exhaustion | ReDoS, payload caps, rate limiting & resource bounds audit. | [`security/dos-resilience-audit/SKILL.md`](./security/dos-resilience-audit/SKILL.md) |
| **🛡️ Security** | `mitm-prevention-audit` | Man-in-the-Middle Transport Security | TLS/SSL enforcement, HSTS headers & HTTP client audit. | [`security/mitm-prevention-audit/SKILL.md`](./security/mitm-prevention-audit/SKILL.md) |
| **🛡️ Security** | `sql-injection-audit` | SQL & Query Injection Audit | Parameterized query verification & SQL injection audit. | [`security/sql-injection-audit/SKILL.md`](./security/sql-injection-audit/SKILL.md) |
| **⚡ Productivity** | `caveman` | Caveman Token Saver | Concise, high-density token-saving responses. | [`productivity/caveman/SKILL.md`](./productivity/caveman/SKILL.md) |
| **⚡ Productivity** | `context-management` | Context Management | Manage AI agent context and session memory during long/multi-step sessions. | [`productivity/context-management/SKILL.md`](./productivity/context-management/SKILL.md) |
| **⚡ Productivity** | `define` | Define (Step 0) | Create/redefine a workspace and define its core in `definition.md` (`/define`, `/spec`). | [`productivity/define/SKILL.md`](./productivity/define/SKILL.md) |
| **⚡ Productivity** | `finalize` | Finalize (Step 4) | Applicable verification gates + dual-axis `code-review`, then move to `finalized/`. | [`productivity/finalize/SKILL.md`](./productivity/finalize/SKILL.md) |
| **⚡ Productivity** | `goal-driven` | Goal-Driven Development | Declarative success criteria instead of step-by-step instructions. | [`productivity/goal-driven/SKILL.md`](./productivity/goal-driven/SKILL.md) |
| **⚡ Productivity** | `grill-me` | Interactive Requirement Grilling | Requirement clarification & edge-case stress testing. | [`productivity/grill-me/SKILL.md`](./productivity/grill-me/SKILL.md) |
| **⚡ Productivity** | `handoff` | Session Handoff Summary | Session state serialization & context preservation. | [`productivity/handoff/SKILL.md`](./productivity/handoff/SKILL.md) |
| **⚡ Productivity** | `humanizer` | Humanizer | Rewrite AI-sounding text to read like the writer, based on Wikipedia's "Signs of AI writing" patterns. | [`productivity/humanizer/SKILL.md`](./productivity/humanizer/SKILL.md) |
| **⚡ Productivity** | `persona` | Persona (soul.md) | Create/change the project or workspace persona the agent adopts (`/persona`). | [`productivity/persona/SKILL.md`](./productivity/persona/SKILL.md) |
| **⚡ Productivity** | `plan` | Plan (Step 1) | Feature/change plan with ordered tasks & resources needed; defines the workspace first if missing. | [`productivity/plan/SKILL.md`](./productivity/plan/SKILL.md) |
| **⚡ Productivity** | `process` | Process (Step 3) | One re-invocable round of `processing/` iteration; loads `software-engineer` for code. `auto` variant runs every remaining task in one pass. | [`productivity/process/SKILL.md`](./productivity/process/SKILL.md) |
| **⚡ Productivity** | `promote` | Promote (Step 5) | Human-authorized deployment of audited `finalized/` content to production, gated by a pre-promote rollback/rollout/monitoring checklist. | [`productivity/promote/SKILL.md`](./productivity/promote/SKILL.md) |
| **⚡ Productivity** | `resources` | Resources (Step 2) | Catalog/request input context, schemas & raw data per the plan's Resources Needed. | [`productivity/resources/SKILL.md`](./productivity/resources/SKILL.md) |
| **⚡ Productivity** | `setup` | Setup (Repository Onboarding) | One-time bootstrap — host mode, conventions, codebase map, brand, persona, first workspace. | [`productivity/setup/SKILL.md`](./productivity/setup/SKILL.md) |
| **⚡ Productivity** | `write-a-skill` | OKF Skill Authoring | Creating new standardized OKF skills (`type: skill`). | [`productivity/write-a-skill/SKILL.md`](./productivity/write-a-skill/SKILL.md) |
