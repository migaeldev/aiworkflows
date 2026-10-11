---
type: skill_category
title: Design Skills Category
description: Skills related to visual design, branding, and user interface aesthetics formatted per Google OKF specs.
tags: [skills, design, category, okf]
timestamp: 2026-09-09T13:52:28+02:00
---

# Design Skills

This category contains skills related to visual design, branding, and user interface aesthetics. All UI/UX work follows `brand-guidelines`, with a brand-onboarding check first while the brand is still `pending` (`AGENTS.md` Directive #4).

## Available Skills

### [`brand-guidelines`](./brand-guidelines/SKILL.md)
The design system for all UI work — Material Design 3 structure and `color-mix()` derivation rules, filled with `aiworkspace/brand/brand.md` values or neutral template defaults. Pairs with `frontend-design` and `visual-iteration`.

### [`brand-onboarding`](./brand-onboarding/SKILL.md)
Capture the brand, its files and artifacts, and the UI technology into `aiworkspace/brand/` (detect existing tokens, then grill-me), or settle on template defaults. Command: `/brand`. Also runs during `setup` and before any UI work while Brand is `pending`.
