---
type: skill
name: persona
title: Persona (soul.md)
description: Create or change a soul.md — the persona the agent adopts so it speaks, codes, and designs as the project itself (same languages, frameworks, patterns, naming, comment style, vocabulary, and voice). Project-wide at aiworkspace/soul.md, or per workspace at aiworkspace/workspaces/<name>/soul.md layered on top. Use during productivity/setup, or when the user runs /persona or asks to create, change, or review the persona.
tags: [skill, productivity, persona, soul, identity, onboarding]
timestamp: 2026-10-11T00:00:00+02:00
---

# Persona (`soul.md`)

## What a soul is
A `soul.md` is written in the first person, *as the project*: "I am <project>. I'm written in…, I structure code like…, I name things…, I speak to users like…". An agent working in the repo reads it and becomes a contributor who already belongs: same language, frameworks, patterns, naming, comment style, vocabulary, and tone.

**A soul governs style, not rules.** `AGENTS.md` directives and the Project-Specific Directives in `project.md` always win over a soul. If a soul conflicts with them, follow the rule and flag the conflict. Hard requirements go in `project.md`; a soul says how the project *sounds and writes*.

## Scopes & layering

| Scope | File | Applies to |
| :--- | :--- | :--- |
| **Project** | `aiworkspace/soul.md` | All work in the repo |
| **Workspace** | `aiworkspace/workspaces/<name>/soul.md` | Work in that workspace, layered over the project soul |

Layering is **section by section**. A section in the workspace soul replaces the same section of the project soul, and sections it leaves out are inherited. A workspace soul only needs to contain what's different. For example, a `docs-site` workspace might change only *Voice & Tone* and *How I Look*.

## Trigger
- `productivity/setup` (its persona step, project scope).
- `/persona` (alias `/soul`), or a request to create, change, or show the persona.
- Optionally from `productivity/define`, when a workspace's identity clearly differs from the project's.

## Process

### Step 1 — Scope
If the user didn't say, ask: **project-wide** or **a workspace** (and which one, from `aiworkspace/index.md`)? A workspace soul needs a project soul to layer on. If `aiworkspace/soul.md` doesn't exist yet, offer to create that first.

### Step 2 — Create or change?
- **The file doesn't exist → create.** Go to Step 3.
- **The file exists → change.** Show a short summary of each section and ask what to change. Edit only those sections, keep the rest word for word, and go to Step 5.
- **"Show me the persona" → read only.** Summarize the effective persona (project soul with workspace overrides applied) and stop.

### Step 3 — Gather (research first, then ask)
Draft from what's already recorded before asking anything:
- `aiworkspace/codebase-map.md` → languages, frameworks, structure, patterns, naming, comment scheme, testing style. **Code-style statements must come from here (with its evidence) or from an explicit user decision**, never from what's typical for the stack.
- `aiworkspace/project.md` → stack, commands, comment policy, project directives.
- `aiworkspace/brand/brand.md` (if present) → personality adjectives, audience, voice, UI technology; plus any voice/tone docs in `brand/docs/`.
- The workspace's `index.md` (workspace scope) → domain purpose, directives, glossary.

If there's no codebase map (declined or greenfield), say so, and ask the code-style questions directly in Step 4 instead.

### Step 4 — Interview the gaps with grill-me
Invoke [`productivity/grill-me`](../grill-me/SKILL.md): one question at a time, each with your recommended answer, only for what Step 3 couldn't settle. Typical gaps:
1. In one sentence, what is this project, and who is it for?
2. How should I talk to you while working: terse or explanatory, formal or casual? How should I write docs, commit messages, and UI copy?
3. What do you value most when trade-offs come up: correctness, speed, simplicity, performance, accessibility…?
4. Which patterns and libraries should I reach for, and which are we moving away from?
5. Which domain words should always be used, and which should be avoided?
6. What would this project never do?

### Step 5 — Write the soul
Use the template below, first person throughout. Drop sections that would only repeat the project soul in a workspace soul. Link to `codebase-map.md`, `brand/brand.md`, and the workspace `index.md` glossary rather than copying them. The soul is the voice; those files hold the detail.

### Step 6 — Record, log & gate
- Project scope: set **Persona** in `project.md` to `soul.md`.
- Workspace scope: link the soul from the workspace `index.md` Persona line, and append a `log.md` entry.
- Show the soul (or the diff, for a change) and wait for confirmation.

---

## `soul.md` template

```markdown
---
type: resource
name: soul
title: <Project | Workspace> Soul
description: The persona agents adopt to work as <project/workspace> — voice, code style, patterns, and values.
scope: project | workspace:<name>
status: finalized
tags: [resource, persona, soul]
timestamp: <ISO-8601>
---

# I am <name>

## Who I Am
<First person: what I am, what I'm for, who depends on me.>

## Voice & Tone
- **With the developer**: …
- **In docs & READMEs**: …
- **In commit messages / PRs**: …
- **In UI copy**: …

## Vocabulary
- **I say**: … (see the workspace glossary in `index.md`)
- **I never say**: …

## What I'm Made Of
<Languages, frameworks, key libraries — summary; detail in `codebase-map.md`.>

## How I Write Code
- **Structure**: where things go (see Change Recipes in `codebase-map.md`).
- **Patterns I use**: …
- **Patterns I avoid / am moving away from**: …
- **Naming**: …
- **Comments & docs**: … (comment policy from `project.md`)
- **Errors & logging**: …
- **Tests**: …

## How I Look
<UI personality, linking to `brand/brand.md`, or "template defaults" / "no UI".>

## What I Value
<Ordered priorities for trade-offs.>

## What I Never Do
- …
```

## Notes
- Writes only `soul.md` files, the **Persona** line in `project.md`, and (workspace scope) the workspace's `index.md` Persona line and `log.md`.
