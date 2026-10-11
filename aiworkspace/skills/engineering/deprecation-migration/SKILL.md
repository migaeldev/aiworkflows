---
type: skill
name: deprecation-migration
title: Deprecation & Migration
description: Code-as-liability mindset for retiring old code paths safely — compulsory vs advisory deprecation, migration patterns (strangler fig, shadow/parallel-run, flag-gated cutover), and zombie-code removal. Use when a change supersedes an existing code path, endpoint, or data format, or when promote is about to replace something already in production.
tags: [skill, engineering, deprecation, migration, cleanup]
timestamp: 2026-10-11T00:00:00+02:00
---

# Deprecation & Migration

## Trigger
Use when a change replaces, supersedes, or makes obsolete an existing code path, API version, data format, or config — including when `productivity/promote` is about to overwrite a production destination that already has callers. Also use proactively: when you notice dead code (nothing references it) while working nearby.

## Rationalizations
| Excuse | Why it's wrong | Do this instead |
| :--- | :--- | :--- |
| "I'll just leave the old path in, it's not hurting anyone" | Every surviving path is something that must still be tested, reasoned about, and kept secure — code is a liability carried forward, not a sunk cost | Give it an explicit deprecation status and a removal date, or remove it now if nothing depends on it |
| "Nobody uses this anymore, I'm pretty sure" | A guess about callers is exactly the kind of claim [`engineering/diagnose`](../diagnose/SKILL.md)'s doubt protocol exists to catch | Verify with usage data, a grep for callers, or a deprecation warning period before removing |
| "I'll delete it in a follow-up" | Follow-ups that aren't blocking anything get deprioritized indefinitely — "later" is where zombie code lives | Remove it in this change if nothing depends on it; if something does, start the migration now instead of deferring |

## Core Mindset

### Code as liability, not asset
Every line that exists must be read, maintained, secured, and reasoned about by everyone who touches the codebase after you — existing code has an ongoing cost, not just a one-time cost to write. When a change makes a path obsolete, removing that path is part of finishing the change, not optional cleanup for later.

## Compulsory vs. advisory deprecation
- **Compulsory**: the old path *will* stop working by a date or version (a security fix, a vendor sunset, a breaking dependency upgrade). Callers must migrate; give them the date, the migration path, and loud warnings as the date approaches.
- **Advisory**: the old path keeps working, but a better one exists. Document the recommendation, but don't force a migration deadline that isn't real — a false compulsory deadline trains people to ignore deprecation warnings generally.

State which kind a deprecation is explicitly — don't leave callers guessing whether "deprecated" means "will break" or "we'd prefer."

## Migration Patterns
- **Strangler fig**: route an increasing share of traffic/calls through the new path while the old one still exists, until nothing hits the old path and it can be deleted.
- **Shadow / parallel-run**: run the new path alongside the old one on real traffic without acting on its output, compare results, and only cut over once they agree closely enough to trust.
- **Flag-gated cutover**: put the switch behind a feature flag so cutover (and rollback, if it goes wrong) is a flag flip, not a deploy.
- **Dual-write then backfill**: when migrating a data format or store, write both old and new simultaneously, backfill history into the new format, then stop writing the old one once reads have fully moved over.

Pick the pattern that matches the blast radius — a flag-gated cutover for something with an easy rollback, shadow/parallel-run when correctness needs to be proven on real traffic before it's trusted.

## Zombie Code Removal
Dead code — unreferenced functions, unused config flags, commented-out blocks kept "just in case" — isn't neutral; it's confusing to the next reader and it's exactly the kind of thing that silently breaks when something nearby changes. When you find it while working nearby, remove it as part of the current change rather than leaving it for later (see Rationalizations above).

## Checklist
- [ ] Every code path this change supersedes has an explicit status: removed now, or deprecated with a stated compulsory/advisory distinction and (if compulsory) a date
- [ ] A migration pattern was chosen deliberately, matched to blast radius, not defaulted to "just swap it"
- [ ] Zombie code noticed nearby was removed, not left for a follow-up
- [ ] If this feeds `productivity/promote`, the pre-promote checklist's "does this replace something with callers" question is answered here, not assumed
