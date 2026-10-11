---
type: skill_category
title: Productivity Skills Category
description: Skills designed to improve efficiency, workflow, context management, goal-driven development, communication, and tool building formatted per Google OKF specs.
tags: [skills, productivity, category, okf]
timestamp: 2026-09-09T14:02:14+02:00
---

# Productivity Skills

This category contains skills designed to improve the efficiency and effectiveness of the development workflow. Use these skills to speed up common tasks, manage context, define testable goals, improve communication, and create new tools.

## Available Skills

### [`caveman`](./caveman/SKILL.md)
Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler, articles, and pleasantries while keeping full technical accuracy.

### [`context-management`](./context-management/SKILL.md)
Manage AI agent context and session memory effectively. Use during long sessions, multi-step tasks, or when responses start degrading.

### [`finalize`](./finalize/SKILL.md)
Step 3 of the lifecycle — run every applicable verification gate plus the dual-axis code-review, then move passing content to finalized/.

### [`goal-driven`](./goal-driven/SKILL.md)
Define success criteria instead of step-by-step instructions. Enables autonomous LLM iteration toward testable goals.

### [`grill-me`](./grill-me/SKILL.md)
Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree.

### [`handoff`](./handoff/SKILL.md)
Compact the current conversation into a handoff document for another agent to pick up.

### [`new-workspace`](./new-workspace/SKILL.md)
Scaffold a new domain workspace from the template-workspace boilerplate, define its scope via `plan` (Project Plan mode), then collect input resources.

### [`persona`](./persona/SKILL.md)
Create or change a `soul.md` persona — project-wide or per workspace — so the agent speaks, codes, and designs as the project itself. Command: `/persona`.

### [`plan`](./plan/SKILL.md)
Step 0 of the lifecycle — determine Project Plan vs. Feature/Change Plan, interview with grill-me, optionally frame with goal-driven, research where needed, and write the plan before resources/ work begins.

### [`process`](./process/SKILL.md)
Step 2 of the lifecycle — one re-invocable round of active iteration in processing/, loading `software-engineer` when code is involved.

### [`promote`](./promote/SKILL.md)
Step 4 of the lifecycle — human-authorized deployment of audited finalized/ content to production.

### [`resources`](./resources/SKILL.md)
Step 1 of the lifecycle — catalog or request the input context, schemas, and raw data a workspace needs.

### [`setup`](./setup/SKILL.md)
One-time repository onboarding — detect the stack, record `host_mode` and conventions, map the codebase (with permission), onboard the brand or use template defaults, create the project persona, then scaffold the first workspace via `new-workspace`.

### [`write-a-skill`](./write-a-skill/SKILL.md)
Create new agent skills with proper structure, progressive disclosure, and bundled resources.
