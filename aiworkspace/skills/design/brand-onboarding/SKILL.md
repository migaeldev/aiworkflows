---
type: skill
name: brand-onboarding
title: Brand Onboarding
description: Capture the project's brand — values, files, and artifacts — and its UI technology into the aiworkspace/brand/ folder (brand.md plus logos, fonts, tokens, source docs, and reference artifacts), by detecting what the codebase already has and interviewing with grill-me; or settle on brand-guidelines' template defaults. Use for /brand, during productivity/setup, and before any UI/UX design or frontend work while project.md's Brand status is pending.
tags: [skill, design, branding, onboarding, grill-me]
timestamp: 2026-10-11T00:00:00+02:00
---

# Brand Onboarding

## Trigger
- **`/brand`**, or a request to set up, change, or show the brand.
- `productivity/setup` (its brand step).
- **Any UI/UX design or frontend task** while **Brand** in `aiworkspace/project.md` is `pending`. Run Step 1 before designing anything (`AGENTS.md` Directive #4).

What `/brand` does depends on **Brand** in `project.md`:

| Brand status | `/brand` does |
| :--- | :--- |
| `pending` | Step 1 (the opening question). |
| `template-defaults` | Asks whether to onboard a real brand now. If yes, starts at Step 2. |
| `custom` | Change mode: summarize `brand/brand.md` and its manifest, ask what to change (values, files, or both), then go through Steps 3–6 for just those parts. |

## The `aiworkspace/brand/` folder

A brand is more than a few hex codes. Everything about it lives in one folder:

```text
aiworkspace/brand/
├── brand.md        # Source of truth: identity, values, UI technology, and a manifest of every file below
├── logos/          # Logo variants (SVG preferred, plus PNGs), favicons, app icons
├── fonts/          # Self-hosted font files + their licenses (skip if fonts come from a CDN)
├── tokens/         # Design tokens supplied by the brand owner or exported for the codebase (tokens.json, theme.css, Tailwind preset, …)
├── docs/           # Source brand documents: guidelines PDF, voice & tone guide, accessibility statement
└── references/     # Artifacts: approved mockups, screenshots, moodboards, marketing pages, do/don't examples
```

Rules:
- **Create subfolders only when they have content.** An empty brand has just `brand.md`.
- **Every file in the folder is listed in `brand.md`'s Manifest**, with its purpose and source. Agents use only manifest-listed files; an unlisted file is unknown until the user confirms it.
- **Files that already live in the host repo** (e.g. `public/logo.svg`) are *referenced* in the manifest by their repo path, not copied. Copies drift.
- **Licenses travel with fonts and third-party assets.** If a license is unknown, note that in the manifest.
- **No secrets.** Brand files must not contain API keys or credentials (e.g. a Figma token). Note where such things live instead.

## Step 1 — Opening question
Ask the user:

> "This project has no brand set up yet. Do you want to onboard the brand now (colors, fonts, logos, any brand documents or design files, and your UI stack), or use the neutral template defaults?"

| Answer | Action |
| :--- | :--- |
| **Onboard now** | Continue to Step 2. |
| **Use template defaults** | Set **Brand** in `project.md` to `template-defaults`. Stop. `brand-guidelines` uses its defaults, and only `/brand` brings this up again. |
| **Not now** | Use template defaults for the current task only. Leave **Brand** as `pending`, so the question comes back at the next UI task. |

## Step 2 — Detect what already exists (read-only)
Before asking anything, find what the codebase and any provided files already answer. Start with `aiworkspace/codebase-map.md` if it exists. Then check:
- **Tokens & themes**: `tailwind.config.*`, CSS custom properties (`:root { --… }`), theme files (`theme.ts`, MUI/Chakra theme objects), design-token JSON, SCSS variables.
- **Fonts**: `@font-face`, Google Fonts imports, `next/font` usage, font files in the repo.
- **Logos & images**: `public/`, `assets/`, `static/`, `logo*`, `favicon*`, brand SVGs.
- **UI stack**: framework (React/Vue/Svelte/Angular/…), meta-framework (Next/Nuxt/…), styling approach (Tailwind, CSS Modules, styled-components, plain CSS, …), component library (shadcn/ui, MUI, Chakra, Radix, Vuetify, …), icon set.
- **Anything already in `aiworkspace/brand/`**, e.g. files the user dropped in before running `/brand`.

Present what you found, with file paths as evidence, before the interview.

## Step 3 — Collect brand files & artifacts
Ask the user for anything that defines the brand, and say which subfolder each kind goes in:
- Logos (light/dark variants, icon-only mark, favicon) → `logos/`
- Font files and licenses, if self-hosted → `fonts/`
- A brand guidelines document, voice & tone guide → `docs/`
- Token files from a design tool or the brand owner → `tokens/`
- Approved designs, mockups, screenshots, moodboards, do/don't examples → `references/`
- Links (Figma, website, brand portal) → recorded in the manifest as links, not downloaded unless the user asks

The user can drop files in themselves, or point at paths in the repo (referenced, not copied). **Read every provided document and artifact**, and extract colors, fonts, logo rules, voice, and do/don'ts from them. Record where each extracted value came from (e.g. `docs/guidelines.pdf p.4`). Extracted values feed Step 4, and the user confirms them there.

## Step 4 — Interview with grill-me
Invoke [`productivity/grill-me`](../../productivity/grill-me/SKILL.md): one question at a time, each with your recommended answer, skipping anything Steps 2–3 already settled. Cover:

**Brand**
1. Brand name, a one-line description, and 3–5 personality adjectives (e.g. "calm, precise, trustworthy").
2. Audience: who uses the UI, and in what setting (desktop dashboards, mobile, kiosk, …).
3. Core colors: the neutral and primary, plus secondary/success/warning/error if they exist. Confirm extracted values. **Never invent a brand color.** Fill any gap from the template defaults and say so.
4. Fonts: primary and monospace (or keep the template defaults), and where they're loaded from.
5. Logos: which file to use on light surfaces and which on dark, plus any clear-space or minimum-size rules.
6. Themes: light, dark, or both? Which is the default?
7. Accessibility target: WCAG AA (recommended) or AAA.
8. Voice in UI copy and any other rules from the brand documents (imagery, iconography, do/don'ts).

**Technology**
9. Confirm the detected UI framework, styling approach, component library, and icon set, or ask if nothing was detected.
10. Design system: Material Design 3 (the `brand-guidelines` default), or the project's own component library's system?
11. Where tokens should live in the codebase: the existing theme/config file, or a new one (propose a path that fits the codebase).

## Step 5 — Write `aiworkspace/brand/brand.md`
Use the template below. Every value is something the user confirmed, something extracted from a listed file (cite it), or a template default marked `(default)`. Check contrast for each text/surface pair against the agreed WCAG target, and record any pair that fails along with the adjusted `color-mix()` percentage. Make sure the Manifest lists every file in `aiworkspace/brand/` and every referenced repo path.

Then set **Brand** in `project.md` to `custom`.

## Step 6 — Present & gate
Show `brand.md`, the folder contents, and the `project.md` change, and wait for confirmation. Don't edit the project's actual token, theme, or asset files from here. That's normal lifecycle work (`processing/` → `promote`).

---

## `brand/brand.md` template

```markdown
---
type: resource
name: brand
title: <Brand> Brand
description: Brand values, files, and UI technology for <project>. Read by design/brand-guidelines.
status: finalized
tags: [resource, brand, design]
timestamp: <ISO-8601>
---

# <Brand> Brand

## Identity
- **Name**: …
- **Description**: …
- **Personality**: …, …, …
- **Audience**: …
- **Voice in UI copy**: …

## Core Colors
| Token | Hex | Source |
| :--- | :--- | :--- |
| neutral | `#…` | user / `docs/guidelines.pdf p.4` / `src/theme.ts:12` / (default) |
| primary | `#…` | … |
| secondary | `#…` | … |
| success | `#…` | … |
| warning | `#…` | … |
| error | `#…` | … |

## Typography
- **Primary font**: … (loaded from: CDN / `fonts/…`)
- **Mono font**: …

## Logos
- **Light surfaces**: `logos/…`
- **Dark surfaces**: `logos/…`
- **Rules**: clear space, minimum size, don'ts

## Themes & Accessibility
- **Themes**: light / dark / both (default: …)
- **WCAG target**: AA / AAA
- **Contrast adjustments**: … (or "none needed")

## UI Technology
- **Framework**: …
- **Styling**: …
- **Component library**: …
- **Icon set**: …
- **Design system**: Material Design 3 / <other>
- **Tokens live in (codebase)**: `…`

## Additional Rules
- … (imagery, iconography, do/don'ts from `docs/` and `references/`)

## Manifest
| Path | Kind | Purpose / when to use | Source | License |
| :--- | :--- | :--- | :--- | :--- |
| `logos/logo.svg` | logo | Primary mark, light surfaces | user | n/a |
| `docs/guidelines.pdf` | doc | Source of colors & logo rules | brand owner | n/a |
| `references/dashboard-v2.png` | reference | Approved dashboard look | design team | n/a |
| `public/favicon.ico` (repo) | logo | Favicon — referenced, not copied | repo | n/a |
| <Figma URL> | link | Design source of truth | — | — |
```

## Notes
- Writes only inside `aiworkspace/brand/` and the **Brand** line in `project.md`.
- In change mode, edit `brand.md` in place, keep values that haven't changed, keep the Manifest in sync with any files added or removed, and log the change in the active workspace's `log.md` if there is one.
