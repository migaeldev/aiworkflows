---
type: index
title: Project Skills Registry
description: Master index of project AI skills categorized into design, engineering, security, and productivity under `@aiworkspace/skills`.
tags: [skills, registry, index, okf]
timestamp: 2026-09-16T16:01:29+02:00
---

# ⚡ Project Skills Registry (`@aiworkspace/skills`)

This registry indexes all specialized project skills available to AI agents operating in this repository. All skills adhere to **Google's Open Knowledge Format (OKF v0.1)** and include mandatory frontmatter metadata (`type: skill`).

---

## 🗂️ Skill Categories

```text
aiworkspace/skills/
├── README.md                          # Master Skills Index & Registry (This file)
├── design/                            # Branding, visual design, and UI specs
│   ├── README.md                      # Design Skills Index
│   └── brand-guidelines/              # 28East Official Brand Guidelines Skill
├── engineering/                       # Code review, debugging, TDD, testing, architecture, and frontend UI
│   ├── README.md                      # Engineering Skills Index
│   ├── code-review/                   # Dual-axis (standards + spec-fidelity) review
│   ├── codebase-design/               # Module depth/seam/interface vocabulary & principles
│   ├── diagnose/                      # Hard bug debugging loop
│   ├── domain-modeling/               # GLOSSARY.md ubiquitous-language upkeep
│   ├── frontend-design/               # Production frontend UI generation
│   ├── improve-codebase-architecture/ # Deepening-opportunity scan + visual HTML report
│   ├── prototype/                     # Throwaway logic/UI prototypes to answer a design question
│   ├── research/                      # Background-agent research into a cited Markdown file
│   ├── software-engineer/             # Mandatory code-writing discipline persona
│   └── testing/                       # Unit/integration/functional/e2e test-type router
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
    ├── finalize/                      # Step 3 gates + dual-axis review
    ├── goal-driven/                   # Declarative success-criteria workflow
    ├── grill-me/                      # Interactive requirement grilling
    ├── handoff/                       # Structured session context summary
    ├── new-workspace/                 # Domain workspace scaffolding
    ├── plan/                          # Step 0 planning (Project Plan / Feature-Change Plan)
    ├── process/                       # Step 2 iteration (re-invocable)
    ├── promote/                       # Step 4 human-authorized deployment
    ├── resources/                     # Step 1 input-context catalog/request
    ├── setup/                         # One-time repo onboarding (host_mode)
    └── write-a-skill/                 # Standardized OKF skill authoring tool
```

---

## 📋 Master Index of Available Skills

| Category | Skill Identifier | Title | Primary Purpose / Trigger | Index File |
| :--- | :--- | :--- | :--- | :--- |
| **🎨 Design** | `28east-brand-guidelines` | 28East Official Brand Guidelines | Official brand colors, fonts, logos & UI compliance, implemented through Google Material Design 3; pairs with `frontend-design`/`visual-iteration`. | [`design/brand-guidelines/SKILL.md`](./design/brand-guidelines/SKILL.md) |
| **🛠️ Engineering** | `code-review` | Code Review Skill | Dual-axis (standards + spec-fidelity) code quality audit, persisted to `finalized/review.md`. | [`engineering/code-review/SKILL.md`](./engineering/code-review/SKILL.md) |
| **🛠️ Engineering** | `codebase-design` | Codebase Design Vocabulary | Module/interface/depth/seam/adapter/leverage/locality vocabulary, the deletion test, and the design-it-twice pattern. | [`engineering/codebase-design/SKILL.md`](./engineering/codebase-design/SKILL.md) |
| **🛠️ Engineering** | `diagnose` | Diagnosis & Debugging Loop | Deep bug analysis, root cause diagnosis & fixes. | [`engineering/diagnose/SKILL.md`](./engineering/diagnose/SKILL.md) |
| **🛠️ Engineering** | `domain-modeling` | Domain Modeling | Keep `GLOSSARY.md` ubiquitous language current as domain concepts are named or sharpened. | [`engineering/domain-modeling/SKILL.md`](./engineering/domain-modeling/SKILL.md) |
| **🛠️ Engineering** | `frontend-design` | Frontend UI Design Skill | Next.js, React, Tailwind & responsive UI creation. | [`engineering/frontend-design/SKILL.md`](./engineering/frontend-design/SKILL.md) |
| **🛠️ Engineering** | `improve-codebase-architecture` | Improve Codebase Architecture | Scan for deepening opportunities, present a visual HTML report, then grill through the pick. | [`engineering/improve-codebase-architecture/SKILL.md`](./engineering/improve-codebase-architecture/SKILL.md) |
| **🛠️ Engineering** | `prototype` | Prototype | Throwaway logic demo or switchable UI variants to answer a design question. | [`engineering/prototype/SKILL.md`](./engineering/prototype/SKILL.md) |
| **🛠️ Engineering** | `research` | Research | Background-agent investigation against primary sources, captured as a cited Markdown file. | [`engineering/research/SKILL.md`](./engineering/research/SKILL.md) |
| **🛠️ Engineering** | `software-engineer` | Software Engineer Practices | Mandatory plan/test/review discipline for any code-writing task. | [`engineering/software-engineer/SKILL.md`](./engineering/software-engineer/SKILL.md) |
| **🛠️ Engineering** | `testing` | Testing: Pick the Right Type | Unit/integration/functional/e2e test-type router with per-type conventions. | [`engineering/testing/SKILL.md`](./engineering/testing/SKILL.md) |
| **🛡️ Security** | `ci-cd-security-review` | CI/CD Pipeline Security Review | Pipeline security, secrets scanning, IAM & artifact audit. | [`security/ci-cd-security-review/SKILL.md`](./security/ci-cd-security-review/SKILL.md) |
| **🛡️ Security** | `security-code-audit` | Security Code Audit Skill | OWASP Top 10 vulnerabilities, CORS & AppSec audit. | [`security-code-audit/SKILL.md`](./security/security-code-audit/SKILL.md) |
| **🛡️ Security** | `dos-resilience-audit` | Application DoS & Resource Exhaustion | ReDoS, payload caps, rate limiting & resource bounds audit. | [`security/dos-resilience-audit/SKILL.md`](./security/dos-resilience-audit/SKILL.md) |
| **🛡️ Security** | `mitm-prevention-audit` | Man-in-the-Middle Transport Security | TLS/SSL enforcement, HSTS headers & HTTP client audit. | [`security/mitm-prevention-audit/SKILL.md`](./security/mitm-prevention-audit/SKILL.md) |
| **🛡️ Security** | `sql-injection-audit` | SQL & Query Injection Audit | Parameterized query verification & SQL injection audit. | [`security/sql-injection-audit/SKILL.md`](./security/sql-injection-audit/SKILL.md) |
| **⚡ Productivity** | `caveman` | Caveman Token Saver | Concise, high-density token-saving responses. | [`productivity/caveman/SKILL.md`](./productivity/caveman/SKILL.md) |
| **⚡ Productivity** | `context-management` | Context Management | Manage AI agent context and session memory during long/multi-step sessions. | [`productivity/context-management/SKILL.md`](./productivity/context-management/SKILL.md) |
| **⚡ Productivity** | `finalize` | Finalize (Step 3) | Four verification gates + dual-axis `code-review`, then move to `finalized/`. | [`productivity/finalize/SKILL.md`](./productivity/finalize/SKILL.md) |
| **⚡ Productivity** | `goal-driven` | Goal-Driven Development | Declarative success criteria instead of step-by-step instructions. | [`productivity/goal-driven/SKILL.md`](./productivity/goal-driven/SKILL.md) |
| **⚡ Productivity** | `grill-me` | Interactive Requirement Grilling | Requirement clarification & edge-case stress testing. | [`productivity/grill-me/SKILL.md`](./productivity/grill-me/SKILL.md) |
| **⚡ Productivity** | `handoff` | Session Handoff Summary | Session state serialization & context preservation. | [`productivity/handoff/SKILL.md`](./productivity/handoff/SKILL.md) |
| **⚡ Productivity** | `new-workspace` | New Workspace | Scaffold a new domain workspace from the template, then define its scope via `plan` (Project Plan mode). | [`productivity/new-workspace/SKILL.md`](./productivity/new-workspace/SKILL.md) |
| **⚡ Productivity** | `plan` | Plan (Step 0) | Project Plan vs. Feature/Change Plan, grill-me always, goal-driven only if opted in, before `resources/` work begins. | [`productivity/plan/SKILL.md`](./productivity/plan/SKILL.md) |
| **⚡ Productivity** | `process` | Process (Step 2) | One re-invocable round of `processing/` iteration; loads `software-engineer` for code. | [`productivity/process/SKILL.md`](./productivity/process/SKILL.md) |
| **⚡ Productivity** | `promote` | Promote (Step 4) | Human-authorized deployment of audited `finalized/` content to production. | [`productivity/promote/SKILL.md`](./productivity/promote/SKILL.md) |
| **⚡ Productivity** | `resources` | Resources (Step 1) | Catalog/request input context, schemas & raw data per the Step 0 plan. | [`productivity/resources/SKILL.md`](./productivity/resources/SKILL.md) |
| **⚡ Productivity** | `setup` | Setup (Repository Onboarding) | One-time bootstrap — detect host context, record `host_mode`, scaffold the first workspace. | [`productivity/setup/SKILL.md`](./productivity/setup/SKILL.md) |
| **⚡ Productivity** | `write-a-skill` | OKF Skill Authoring | Creating new standardized OKF skills (`type: skill`). | [`productivity/write-a-skill/SKILL.md`](./productivity/write-a-skill/SKILL.md) |
