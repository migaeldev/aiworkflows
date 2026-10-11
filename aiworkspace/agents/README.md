---
type: index
title: Specialist Agents Registry
description: Registry of fresh-subagent reviewer personas (OKF type: agent) — isolated second opinions that load and use the skills in aiworkspace/skills/ rather than duplicating them.
tags: [agents, registry, index, okf]
timestamp: 2026-10-11T00:00:00+02:00
---

# 🕵️ Specialist Agents Registry (`aiworkspace/agents/`)

A specialist agent is a persona brief, not a worker that does something itself. Each `AGENT.md` here defines a mindset, a scope, and which skill(s) from [`aiworkspace/skills/`](../skills/README.md) it loads — then gets spawned as a **fresh, isolated subagent** (no shared context with whoever wrote the code) for a second opinion.

See [`skills/using-agent-skills`](../skills/using-agent-skills/SKILL.md) for the full decision table on when to load a skill yourself versus spawn one of these.

---

## 🗂️ Roster

| Agent | Loads | Scope | Spawn when |
| :--- | :--- | :--- | :--- |
| [`code-reviewer`](./code-reviewer/AGENT.md) | [`engineering/code-review`](../skills/engineering/code-review/SKILL.md) | Dual-axis Standards + Spec Fidelity | Before merging significant work, or any time you want a second opinion |
| [`test-engineer`](./test-engineer/AGENT.md) | [`engineering/testing`](../skills/engineering/testing/SKILL.md), [`engineering/test-first`](../skills/engineering/test-first/SKILL.md) | Coverage adequacy and test quality | Coverage is in doubt, or a bug slipped past existing tests |
| [`security-auditor`](./security-auditor/AGENT.md) | the applicable [`security/*`](../skills/security/README.md) skills | OWASP, injection, DoS, transport security | Security-sensitive change, auth/data-handling code, before `finalize`'s security gate |
| [`performance-auditor`](./performance-auditor/AGENT.md) | [`engineering/web-performance-audit`](../skills/engineering/web-performance-audit/SKILL.md) | Core Web Vitals, bundle size, render blocking | Frontend or perf-sensitive change |

---

## How to spawn one

1. Read the agent's `AGENT.md` for its exact Identity, Scope, and Skills Loaded.
2. Spawn it as a **fresh** subagent — it must not inherit the writer's conversation context. Frame the brief as "you did not write this code; review it as if seeing it for the first time."
3. Give it: the file paths or diff to review, and whatever it needs to check against — the workspace's `definition.md`, the feature's `plan.md` (including its Constraints section), or both.
4. Its findings are a report back to you, not a change to the code — you (or the human) decide what to do with them.

## Why fresh, not reused
The agent that wrote the code is attached to its own implementation decisions and unlikely to question its own assumptions — its context is full of *how* the code got built, not a reviewer's perspective on *whether* it should have been built that way. A fresh instance has neither bias.
