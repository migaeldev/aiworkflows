---
type: skill
name: domain-modeling
title: Domain Modeling
description: Keep a workspace's domain language — names for concepts, recorded in its index.md Domain Identity/Directives section — current as decisions crystallize during design or architecture work. Use whenever a refactor, review, or planning conversation names or sharpens a domain concept.
tags: [skill, engineering, domain-modeling, glossary, ubiquitous-language]
timestamp: 2026-10-05T12:00:00+02:00
---

# Domain Modeling

## Trigger
Load this skill whenever a conversation about the codebase surfaces, names, or sharpens a domain concept — most often from [`engineering/improve-codebase-architecture`](../improve-codebase-architecture/SKILL.md)'s grilling loop, but also standalone whenever naming comes up during planning or review.

## Where the glossary lives
This repo does not keep a separate `GLOSSARY.md`. Per [`engineering/software-engineer`](../software-engineer/SKILL.md)'s mandate #4, the active domain workspace's `index.md` (`aiworkspace/workspaces/<domain>/index.md`, Domain Identity/Directives section) **is** the glossary — there is no separate file to create or sync. This is the Domain-Driven-Design idea of a **ubiquitous language** applied to this repo's OKF structure: the design doesn't own the vocabulary, the domain workspace's `index.md` does.

If this skill is ever run against a codebase outside this repo's `aiworkspace/` lifecycle (no workspace `index.md` to write into), fall back to a `GLOSSARY.md` at that project's root and say so explicitly — but inside this repo, always use the workspace `index.md`.

## When to update the workspace's `index.md`
- **A new concept gets named.** If a deepened module, a seam, or a refactor is named after a concept not yet in the workspace's Domain Identity/Directives section, add it immediately — not at the end of the session, right when the name is chosen. A name chosen now and recorded later never gets recorded.
- **A fuzzy term gets sharpened.** If a conversation clarifies that "Order" actually means two different things in two different contexts (e.g. "Draft Order" vs. "Confirmed Order"), update the entry on the spot, including splitting it into two entries if the distinction is real and going to recur.
- **A term stops being used correctly.** If code or conversation starts using an existing term loosely (calling something an "Order" that isn't one), that's a prompt to either correct the usage or recognize the entry itself needs to change.

## Entry format
Keep entries short and concrete — one definition, one example, cross-references where a term depends on another — appended under the workspace `index.md`'s Domain Identity/Directives section:

```markdown
### Order
A customer's request to purchase one or more Line Items at a point in time.
Distinct from a **Cart** (not yet committed) and a **Shipment** (the fulfillment
of an Order, tracked separately). See also: Line Item.
```

## What this skill is not
This isn't a data-modeling or schema-design skill — it doesn't decide how a concept is persisted or typed. It only keeps the *names* for domain concepts consistent between the code, the architecture conversation, the people in it, and the workspace's `index.md`. Schema and type decisions belong wherever this project already makes them.
