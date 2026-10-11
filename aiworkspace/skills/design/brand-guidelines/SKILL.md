---
type: skill
name: 28east-brand-guidelines
title: 28East Brand Styling & Visual Identity
description: Applies 28East's official brand identity, Google Maps Premier Partner aesthetics, color palette, typography, logos, and design standards — implemented through Google Material Design 3 (https://m3.material.io/) component/color/shape/motion patterns — to artifacts, UI components, and web applications. Every color beyond the official brand hexes is derived from them via disclosed color-mix() formulas, never invented. Requires pairing with the frontend-design and visual-iteration skills whenever frontend UI is being designed or built.
tags: [skill, design, branding, 28east, google-maps, location-intelligence, material-design-3, color-theory]
license: Complete terms in LICENSE.txt
timestamp: 2026-10-01T00:00:00+02:00
---

# 🌐 28East Brand Styling & Visual Identity

## Overview

**28East** is a boutique software engineering firm and **Google Maps Premier Partner** specializing in location intelligence, interactive map-powered applications, network coverage solutions, and Google Cloud Platform (GCP) services across Africa.

Use this skill to apply **28East**'s official visual identity — colors, typography (`Roboto`), and logo assets — to all UI components, dashboards, documentation, and digital artifacts. This skill supplies the **values**; the mandatory design **system** they get implemented through is Google Material Design 3, below.

**Hard rule: only three colors are the actual 28East brand spec** — Brand Red `#E31B23`, Slate Grey `#414A51`, Process White `#FFFFFF` (plus the separately-sourced Google Premier Partner signal colors in section 3). Everything else — every surface tier, every "on-container" text tone, every tonal chip background — **must be derived from one of those colors via a disclosed `color-mix()` formula, never a hand-picked hex.** If a UI needs a color this doc doesn't cover and no formula derives it cleanly, **stop and ask the user** — do not invent one. (An earlier version of this doc listed a "Deep Navy `#0A1128`" dark-surface scale that was never actually derived from Slate Grey — see the color-theory audit below for how that was found and fixed.)

---

## 🧩 Mandatory Design System: Google Material Design 3

**All UI/UX design and every component MUST implement [Google Material Design 3](https://m3.material.io/) ("M3").** M3 is the system; the colors/type/logos in this doc are the values poured into it. Concretely, every interface built under this skill must use M3's:

- **Color roles** — `primary`, `secondary`, `tertiary`, `error`, and the `surface`/`surface-container` (-low/-high/-highest) tiers, each resolved from the brand palette below, never from ad hoc hex values scattered through markup.
- **Shape scale** — `xs` 4px / `sm` 8px / `md` 12px / `lg` 16px / `xl` 28px / `full` pill, not arbitrary per-component radii.
- **Elevation** — M3 levels 0–5. Dark surfaces express elevation mostly through shadow depth (tinting barely reads on a dark ground); light surfaces use real, soft umbra shadows. Never fake elevation with a border alone.
- **State layers** — hover/focus/pressed/dragged as a semi-transparent overlay in the relevant color (M3's documented opacities: hover ~8%, focus/pressed ~12%, dragged ~16%), applied consistently — not bespoke per-component hover rules.
- **Type scale** — display/headline/title/body/label, set in **Roboto** (28East's mandated web font, which is also M3's native font — the two systems are never in tension). M3 differentiates headline vs. body by **size/weight**, not by giving headlines a separate, darker text color than body text — don't invent a second "heading color."
- **Motion** — M3's standard easing (`cubic-bezier(0.2,0,0,1)` standard; `cubic-bezier(0.3,0,0.8,0.15)` emphasized-accelerate). Prefer one well-composed entrance (staggered reveal of static elements) over scattered micro-animations, and never animate elements that re-render on a polling interval — it flickers.
- **Components** — reach for M3's actual vocabulary first: filled/outlined/text buttons, assist/filter chips (tonal pattern below), elevated/filled cards, outlined text fields, segmented buttons, top app bars, FABs, linear/circular progress indicators, snackbars. Prefer a segmented button over two near-duplicate forms; prefer a tonal chip over a solid-color badge.

---

## 🎯 Color Theory: Why This Palette, Not a Random One

The brand's three sourced colors plus the Google Premier Partner signals form a deliberate, checkable relationship on the color wheel — not an arbitrary pile of hexes. Measured in HSL:

| Color | Hex | Hue | Sat | Light | Role in the wheel |
| :--- | :--- | :---: | :---: | :---: | :--- |
| Slate Grey | `#414A51` | 206° | 11% | 29% | Achromatic backbone — low-saturation cool grey |
| Light Canvas | `#F8FAFC` | 210° | 40%* | 98% | Same hue family as Slate Grey, pushed to near-white (*high numeric saturation at extreme lightness reads as a near-imperceptible cool tint, not a visible hue) |
| Cloud Cyan | `#00C2FF` | 194° | 100% | 50% | Analogous to Premier Blue (20° apart) |
| Premier Blue | `#1A73E8` | 214° | 82% | 51% | Primary action/info — sits ~150–160° from Brand Red, i.e. **near-complementary**: red reads as a deliberate, high-contrast accent against the blue-toned UI rather than clashing |
| Signal Green | `#34A853` | 136° | 53% | 43% | Roughly triadic against Blue (78° away) and Red (138° away) — far enough from both on the wheel that success/info/error are never visually confusable |
| Amber | `#FBBC04` | 45° | 97% | 50% | Warm midpoint between Red and Green — used sparingly for pending/caution, the one hue intentionally "between" the other two accents |
| Brand Red | `#E31B23` | 358° | 79% | 50% | Primary accent / error — the near-complement to the Blue/Cyan family above |

**The working rule**: Slate Grey (and its near-white Light Canvas sibling) is the *only* neutral — every surface, border, and body-text color is a `color-mix()` of Slate Grey toward black or white, never a separately-invented grey or a blue-tinted "dark mode color." The four signal hues (Blue/Cyan/Green/Amber) plus Red are kept far enough apart on the wheel that they stay semantically distinct (action vs. info vs. success vs. caution vs. error) instead of competing for the same visual attention. Don't introduce a sixth hue without deriving it from one of these seven and writing down the derivation.

---

## 🤝 Required Companion Skills

Whenever this skill is used to design or build frontend UI, **both of the following must also be used in the same pass**:

- **`frontend-design`** — aesthetic execution quality: a committed point of view within the structure above; real typographic/spatial craft; atmosphere and depth rather than solid-color panels.
- **`visual-iteration`** — verification: implement, screenshot the rendered result (or have the user screenshot it if no browser-automation tool is available in the session), compare against intent, and iterate on concrete differences. If no screenshot tool is available, say so explicitly rather than silently skipping verification.

Treat a frontend task as incomplete if it skips either — M3 compliance and a correct palette don't by themselves guarantee good execution or that the implementation actually looks right.

---

## 🎨 Official Brand Specifications & Assets

The official brand assets are stored under `aiworkspace/skills/design/brand-guidelines/assets/`:

- **[Master SVG Logo](file:///Users/migaelhartzenberg/Dev/projects/ai/insights/aiworkspace/skills/design/brand-guidelines/assets/logo.svg)**: `assets/logo.svg`
- **[Standard PNG Logo](file:///Users/migaelhartzenberg/Dev/projects/ai/insights/aiworkspace/skills/design/brand-guidelines/assets/logo.png)**: `assets/logo.png` (light surfaces)
- **[Dark PNG Logo](file:///Users/migaelhartzenberg/Dev/projects/ai/insights/aiworkspace/skills/design/brand-guidelines/assets/logo-dark.png)**: `assets/logo-dark.png` (light surfaces, alternate)
- **[Transparent White Logo](file:///Users/migaelhartzenberg/Dev/projects/ai/insights/aiworkspace/skills/design/brand-guidelines/assets/logo-alpha-white.png)**: `assets/logo-alpha-white.png` (dark surfaces **only** — invisible on light backgrounds)
- **[Official Brand Guidelines PDF](file:///Users/migaelhartzenberg/Dev/projects/ai/insights/aiworkspace/skills/design/brand-guidelines/assets/brand-guidelines.pdf)**: `assets/brand-guidelines.pdf`

### 1. Brand Core Colors (PDF Spec — the only three with Pantone/CMYK backing)

| Color Name | Pantone Match | CMYK Values | RGB Values | Hex Code | Purpose / Usage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **28East Brand Red** | `Pantone 1797C` | `C:0, M:100, Y:99, K:4` | `R:227, G:27, B:35` | `#E31B23` | Primary accent, alert markers — M3 `error` role |
| **28East Slate Grey** | `Pantone 7540EC` | `C:41, M:27, Y:22, K:69` | `R:65, G:74, B:81` | `#414A51` | **The only brand neutral** — every surface/border/muted-text color below is derived from this one hue — M3 `on-surface-variant` role, and the seed for every `surface`/`surface-container` tier |
| **Process White** | `Pantone Process WHITE C` | `C:0, M:0, Y:0, K:0` | `R:255, G:255, B:255` | `#FFFFFF` | Primary white text/background — M3 `on-primary` and light-theme `surface-container-low` |

### 2. UI Background & Surface Colors — derived from Slate Grey, charcoal not navy

**Correction**: an earlier version of this doc listed a "Deep Navy `#0A1128`" dark-theme scale (`#0A1128` / `#0B192C` / `#1E293B`). Measured in HSL, that trio sits at hue 214–226°, saturation 33–60% — that's Premier Blue's hue family, nowhere near Slate Grey's hue 206°, saturation 11%. It was never actually derived from the brand and has been replaced below with a genuine charcoal/slate-grey tonal scale (each step a `color-mix()` of the real Slate Grey toward black or white — compute it yourself, don't copy a fixed hex):

- **Dark theme `surface`**: `color-mix(in srgb, #414A51 18%, black)` — darkest, page background.
- **Dark theme `surface-container-low`**: `color-mix(in srgb, #414A51 26%, black)` — resting cards.
- **Dark theme `surface-container`**: `color-mix(in srgb, #414A51 34%, black)` — table headers, inputs.
- **Dark theme `surface-container-high`**: `color-mix(in srgb, #414A51 44%, black)` — hover states, modals.
- **Dark theme `surface-container-highest`**: `color-mix(in srgb, #414A51 54%, black)`.
- **Dark theme `outline`**: `#414A51` as-is (the native brand color already works as a mid-tone border on a darker ground).
- **Dark theme `on-surface`**: `#FFFFFF` (Process White, official, as-is).
- **Dark theme `on-surface-variant`** (muted text): `color-mix(in srgb, #414A51 55%, white)`.

- **Light theme `surface`**: `#F8FAFC` (Light Canvas) — already the Slate Grey hue pushed to near-white (hue 210° vs. 206° — same family), kept as-is.
- **Light theme `surface-container-low`**: `#FFFFFF` (Process White, official, as-is).
- **Light theme `surface-container`**: `color-mix(in srgb, #414A51 6%, white)`.
- **Light theme `surface-container-high`**: `color-mix(in srgb, #414A51 10%, white)`.
- **Light theme `outline`**: `color-mix(in srgb, #414A51 35%, white)`.
- **Light theme `outline-variant`**: `color-mix(in srgb, #414A51 16%, white)`.
- **Light theme `on-surface`** (headings *and* body — same color, differentiated by type scale, not a separate color): `color-mix(in srgb, #414A51 30%, black)` — a near-black charcoal, not pure black, still traceable to the brand hue.
- **Light theme `on-surface-variant`** (muted text): `#414A51` as-is.

### 3. Google Premier Partner & Location Signals (M3 accent roles)

- **Google Premier Blue** (M3 `primary`): `#1A73E8` / `#1444C3` — primary CTAs, active map overlays, interactive states.
- **Signal / Coverage Green** (M3 `tertiary`): `#34A853` / `#10B981` — network coverage, verified addresses, positive telemetry.
- **Google Cloud Cyan** (M3 `secondary`): `#00C2FF` / `#38BDF8` — data flow highlights, metric tags, route paths.
- **Location Amber / Yellow** (M3 extended `warning`): `#FBBC04` / `#F59E0B` — pending status, route warnings.
- **Alert / Marker Red** (M3 `error`): `#EA4335` / `#E31B23` — error states, pin markers, critical indicators.

Each of these, used as **text on a light background** or as a **tonal chip**, must also be reached via `color-mix()`, never a separately-invented darker/lighter hex:

- **Container (pastel chip background, light theme)**: `color-mix(in srgb, <signal-color> 14%, white)`.
- **On-container (readable text on that pastel chip, light theme)**: `color-mix(in srgb, <signal-color> 65%, black)`.
- **Container (dark theme)**: `color-mix(in srgb, <signal-color> 24%, black)`.
- **On-container (dark theme)**: `color-mix(in srgb, <signal-color> 70%, white)`.

---

## 🔤 Typography & Font Stack

All 28East web interfaces and UI designs **MUST** use **Roboto** as the default primary web font — conveniently, Roboto is also Material Design 3's own native font, so the brand mandate and the M3 mandate never conflict.

- **Default Web Font**: **`Roboto`**
  - **Primary Web Font Stack**: `"Roboto"`, `"Google Sans"`, `"Inter"`, `-apple-system`, `BlinkMacSystemFont`, `sans-serif`
- **Logo Font**: `Handel Gothic Regular` (converted to curves in logo vectors)
- **Monospace / API & Data Stack**: `"Fira Code"`, `"JetBrains Mono"`, `"Roboto Mono"`, `monospace`

### Typography Hierarchy Guidelines (M3 type scale, in Roboto)

- **Headings (M3 headline/title)**: Semi-bold/Bold (600/700 weight). Same `on-surface` color as body text (see section 2) — size/weight carries the hierarchy, not a separate color.
- **Body Text (M3 body)**: Regular (400 weight), line height 1.5–1.6.
- **Labels (M3 label, e.g. buttons/chips)**: Medium (500 weight), slightly tighter tracking.
- **Data Labels & Coordinates**: Monospace (`JetBrains Mono` / `Roboto Mono`) for API payloads, IP addresses, lat/long coordinates, code variables.

---

## 🗺️ UI Component Standards (M3 components, 28East values)

1. **Containers & Cards (M3 elevated/filled card)**: `border-radius: 16px` (`--shape-lg`). Background = the theme's `surface-container-low` from section 2. Border = `outline-variant`. Elevation via shadow (dark) or soft umbra (light), never a border alone.
2. **Buttons (M3 filled/outlined/text) & Chips (M3 assist/filter)**: Filled primary = Premier Blue, full-pill shape, M3 state layer on hover/press. Alternate filled (confirm/positive) = Signal Green. Outlined/text secondary = transparent or surface background with an M3 hover state layer. Status chips = the tonal container/on-container pattern in section 3 — never a solid badge. Prefer a segmented button over two near-duplicate side-by-side forms.
3. **Logos & Branding**: light surfaces → `logo.png`/`logo-dark.png`; dark surfaces → `logo-alpha-white.png` **only**. Check which surface the logo actually sits on before picking the file.

A full worked example of this system (color roles via `color-mix()`, shape, elevation, state layers, chips, segmented control, type scale, all in Roboto) lives in `aiworkspace/workspaces/task-management-system/processing/task-engine/src/cmd/api/static/style.css` — a reference implementation, not a copy-paste template, since every product's layout will differ. (Relocated 2026-10-04 from `etl-pipeline/processing/task-core/` when that engine was extracted into its own workspace.)

---

## 🛠️ CSS Variables Reference

```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
  /* ---- The only three sourced brand colors ---- */
  --east-red: #E31B23;            /* Pantone 1797C -- M3 error */
  --east-slate-grey: #414A51;     /* Pantone 7540EC -- the only brand neutral */
  --east-white: #FFFFFF;          /* Pantone Process WHITE C */

  /* ---- Google Premier Partner signals -- M3 primary/secondary/tertiary/warning ---- */
  --premier-blue: #1A73E8;        /* M3 primary */
  --signal-green: #34A853;        /* M3 tertiary */
  --cloud-cyan: #00C2FF;          /* M3 secondary */
  --location-yellow: #FBBC04;     /* M3 extended warning */

  /* ---- Light Canvas: same hue family as Slate Grey (206-210deg), kept as a named token ---- */
  --east-bg-light: #F8FAFC;

  /* ---- Typography ---- */
  --font-default: 'Roboto', 'Google Sans', 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Roboto Mono', monospace;

  /* ---- M3 shape scale ---- */
  --shape-xs: 4px;
  --shape-sm: 8px;
  --shape-md: 12px;
  --shape-lg: 16px;
  --shape-xl: 28px;
  --shape-full: 999px;
}

/* ---- DARK THEME: every surface/text tone below is color-mix() of --east-slate-grey
   toward black/white, or the brand hex as-is. No invented hex anywhere. ---- */
:root[data-theme="dark"] {
  --md-surface: color-mix(in srgb, var(--east-slate-grey) 18%, black);
  --md-surface-container-low: color-mix(in srgb, var(--east-slate-grey) 26%, black);
  --md-surface-container: color-mix(in srgb, var(--east-slate-grey) 34%, black);
  --md-surface-container-high: color-mix(in srgb, var(--east-slate-grey) 44%, black);
  --md-outline: var(--east-slate-grey);
  --md-on-surface: var(--east-white);
  --md-on-surface-variant: color-mix(in srgb, var(--east-slate-grey) 55%, white);
}

/* ---- LIGHT THEME: Light Canvas + Process White are already Slate-Grey-hue-family;
   everything else is color-mix() toward white, or the native Slate Grey as-is. ---- */
:root[data-theme="light"] {
  --md-surface: var(--east-bg-light);
  --md-surface-container-low: var(--east-white);
  --md-surface-container: color-mix(in srgb, var(--east-slate-grey) 6%, white);
  --md-surface-container-high: color-mix(in srgb, var(--east-slate-grey) 10%, white);
  --md-outline: color-mix(in srgb, var(--east-slate-grey) 35%, white);
  --md-on-surface: color-mix(in srgb, var(--east-slate-grey) 30%, black);
  --md-on-surface-variant: var(--east-slate-grey);
}

body {
  font-family: var(--font-default);
  background-color: var(--md-surface);
  color: var(--md-on-surface);
}
```
