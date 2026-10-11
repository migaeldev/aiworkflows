---
type: skill
name: write-a-skill
title: Write a Skill
description: Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, or build a new skill.
tags: [skill, productivity, meta, skill-authoring]
timestamp: 2026-09-09T13:45:03+02:00
---

# Writing Skills

## Process

1. **Gather requirements** - ask user about:
    - What task/domain does the skill cover?
    - What specific use cases should it handle?
    - Does it need executable scripts or just instructions?
    - Any reference materials to include?

2. **Draft the skill** - create:
    - SKILL.md with concise instructions and OKF frontmatter (`type: skill`)
    - Additional reference files if content exceeds 500 lines
    - Utility scripts if deterministic operations needed

3. **Review with user** - present draft and ask:
    - Does this cover your use cases?
    - Anything missing or unclear?
    - Should any section be more/less detailed?

## Skill Structure

```
skill-name/
├── SKILL.md           # Main instructions & OKF frontmatter (required)
├── REFERENCE.md       # Detailed docs (if needed)
├── EXAMPLES.md        # Usage examples (if needed)
└── scripts/           # Utility scripts (if needed)
    └── helper.js
```

## SKILL.md Template (OKF Standard)

```md
---
type: skill
name: skill-name
title: Human Readable Title
description: Brief description of capability. Use when [specific triggers].
tags: [skill, category]
timestamp: 2026-09-09T13:45:03+02:00
---

# Skill Name

## Trigger

[When to use this skill]

## Rationalizations (optional — add when the skill enforces costly discipline)

| Excuse | Why it's wrong | Do this instead |
| :--- | :--- | :--- |
| [Common excuse to skip/rush/weaken a step] | [Why that reasoning fails] | [The right move instead] |

## Workflows

[Step-by-step processes with checklists for complex tasks]

## Advanced features

[Link to separate files: See [REFERENCE.md](REFERENCE.md)]
```

### When to add a `## Rationalizations` table
This is an OKF-level convention (see `AGENTS.md`'s "OKF Formatting Standard"), available to any `type: skill` or `type: domain` document — not just this template. Add one when the skill's process includes a step that's costly or inconvenient to follow (testing, review, a verification gate, a diagnosis loop) and agents are likely to talk themselves out of it. Keep it short — 3-6 rows naming the actual excuses seen in practice, not a generic list. Place it right after the skill's `## Trigger`/intro, before the main process. Skip it entirely for skills with no tempting shortcut (e.g. a pure lookup or formatting skill).

## Description Requirements

The description is **the only thing your agent sees** when deciding which skill to load. It's surfaced in the system prompt alongside all other installed skills. Your agent reads these descriptions and picks the relevant skill based on the user's request.

**Goal**: Give your agent just enough info to know:

1. What capability this skill provides
2. When/why to trigger it (specific keywords, contexts, file types)

**Format**:

- Max 1024 chars
- Write in third person
- First sentence: what it does
- Second sentence: "Use when [specific triggers]"

**Good example**:

```
Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction.
```

**Bad example**:

```
Helps with documents.
```

The bad example gives your agent no way to distinguish this from other document skills.

## When to Add Scripts

Add utility scripts when:

- Operation is deterministic (validation, formatting)
- Same code would be generated repeatedly
- Errors need explicit handling

Scripts save tokens and improve reliability vs generated code.

## When to Split Files

Split into separate files when:

- SKILL.md exceeds 100 lines
- Content has distinct domains (finance vs sales schemas)
- Advanced features are rarely needed

## Review Checklist

After drafting, verify:

- [ ] Frontmatter contains `type: skill` (OKF standard)
- [ ] Description includes triggers ("Use when...")
- [ ] `## Rationalizations` added if the skill enforces costly discipline; omitted otherwise
- [ ] SKILL.md under 100 lines
- [ ] No time-sensitive info
- [ ] Consistent terminology
- [ ] Concrete examples included
- [ ] References one level deep
