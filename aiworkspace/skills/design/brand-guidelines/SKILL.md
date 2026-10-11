---
type: skill
name: brand-guidelines
title: Brand Guidelines
description: The design system every UI is built with — Google Material Design 3 (https://m3.material.io/) structure, color-mix() derivation rules, typography, and component standards — filled with the project's brand values from aiworkspace/brand/brand.md, or with this skill's template defaults when no brand has been onboarded. Every derived color is a disclosed color-mix() formula, never an invented hex. Use for any UI/UX design or frontend work; requires pairing with frontend-design and visual-iteration.
tags: [skill, design, branding, material-design-3, color-theory]
timestamp: 2026-10-11T00:00:00+02:00
---

# 🎨 Brand Guidelines

## Before you start — which values apply?

Check **Brand** in [`aiworkspace/project.md`](../../../project.md):

| Brand status | Do this |
| :--- | :--- |
| `pending` | Run [`design/brand-onboarding`](../brand-onboarding/SKILL.md)'s opening question first. It will either onboard the brand or settle on the defaults. |
| `template-defaults` | Use the **Template Default Values** below. |
| `custom` | Use the values in `aiworkspace/brand/brand.md`. Where `brand/brand.md` leaves a value out, fall back to the default below and say so. |

Whatever the source, the **hard rule** holds: only the core colors are hand-entered. Every surface tier, on-container tone, and tonal chip background **must be derived from a core color via a disclosed `color-mix()` formula, never a hand-picked hex.** If a UI needs a color nothing here derives cleanly, **stop and ask the user**.

Brand values take precedence over [`frontend-design`](../../engineering/frontend-design/SKILL.md)'s generic aesthetic advice (e.g. its font suggestions). `frontend-design` decides *how well* the brand is executed, not *which* brand.

---

## 🧩 Design System: Google Material Design 3

Unless `brand/brand.md` names a different design system, **all UI/UX and every component implement [Google Material Design 3](https://m3.material.io/) ("M3")**. M3 is the system; the brand values are poured into it:

- **Color roles** — `primary`, `secondary`, `tertiary`, `error`, and the `surface`/`surface-container` (-low/-high/-highest) tiers, each resolved from the brand values, never from ad hoc hex values scattered through markup.
- **Shape scale** — `xs` 4px / `sm` 8px / `md` 12px / `lg` 16px / `xl` 28px / `full` pill, not arbitrary per-component radii.
- **Elevation** — M3 levels 0–5. Dark surfaces express elevation mostly through shadow depth; light surfaces use soft umbra shadows. Never fake elevation with a border alone.
- **State layers** — hover/focus/pressed/dragged as a semi-transparent overlay (hover ~8%, focus/pressed ~12%, dragged ~16%), applied consistently.
- **Type scale** — display/headline/title/body/label in the brand font. Differentiate headline vs. body by **size/weight**, not by a separate "heading color."
- **Motion** — M3 standard easing (`cubic-bezier(0.2,0,0,1)`; emphasized-accelerate `cubic-bezier(0.3,0,0.8,0.15)`). Prefer one well-composed entrance over scattered micro-animations; never animate elements that re-render on a polling interval.
- **Components** — M3 vocabulary first: filled/outlined/text buttons, assist/filter chips, elevated/filled cards, outlined text fields, segmented buttons, top app bars, FABs, progress indicators, snackbars.

If `brand/brand.md` names another system (e.g. the project's own component library), use that system's structure instead and keep this skill's color-derivation and contrast rules.

---

## 🎯 Template Default Values

Used when Brand is `template-defaults`, and as the fallback for anything `brand/brand.md` omits. A deliberately neutral, accessible palette:

| Token | Default | M3 role | Hue (approx.) |
| :--- | :--- | :--- | :---: |
| `neutral` | `#475569` (slate) | Only neutral — seed for every surface/border/muted-text tone; `on-surface-variant` | 215° |
| `primary` | `#2563EB` (blue) | `primary` — CTAs, links, active states | 221° |
| `secondary` | `#0891B2` (cyan) | `secondary` — highlights, tags, data accents | 192° |
| `success` | `#16A34A` (green) | `tertiary` — positive states | 142° |
| `warning` | `#D97706` (amber) | extended `warning` — pending/caution | 32° |
| `error` | `#DC2626` (red) | `error` — destructive actions, failures | 0° |
| `white` | `#FFFFFF` | `on-primary`, light `surface-container-low` | — |
| Primary font | `"IBM Plex Sans"` | All UI text | — |
| Mono font | `"IBM Plex Mono"` | Code, IDs, data values | — |

**The working rule**: one neutral hue is the *only* neutral — every surface, border, and body-text color is a `color-mix()` of it toward black or white. The signal hues (action / info / success / caution / error) sit far enough apart on the wheel to stay semantically distinct. Don't add a hue without deriving it from an existing one and writing down the derivation.

---

## 🤝 Required Companion Skills

Whenever this skill is used to design or build frontend UI, **both** of these must also be used in the same pass:

- **[`frontend-design`](../../engineering/frontend-design/SKILL.md)** — aesthetic execution quality within the structure above.
- **[`visual-iteration`](../../engineering/visual-iteration/SKILL.md)** — implement, screenshot the result (or ask the user to if no browser tool is available), compare against intent, iterate. If no screenshot tool is available, say so explicitly rather than silently skipping verification.

---

## 🎨 Derived Colors

Below, `{neutral}` etc. mean the active value (from `brand/brand.md` or the defaults). Adjust percentages only to meet contrast (WCAG AA: 4.5:1 body text, 3:1 large text/UI) — and keep them formulas.

### Surfaces — derived from the neutral

- **Dark `surface`**: `color-mix(in srgb, {neutral} 18%, black)`
- **Dark `surface-container-low`**: `color-mix(in srgb, {neutral} 26%, black)`
- **Dark `surface-container`**: `color-mix(in srgb, {neutral} 34%, black)`
- **Dark `surface-container-high`**: `color-mix(in srgb, {neutral} 44%, black)`
- **Dark `outline`**: `{neutral}`
- **Dark `on-surface`**: `{white}`
- **Dark `on-surface-variant`**: `color-mix(in srgb, {neutral} 55%, white)`
- **Light `surface`**: `color-mix(in srgb, {neutral} 3%, white)`
- **Light `surface-container-low`**: `{white}`
- **Light `surface-container`**: `color-mix(in srgb, {neutral} 6%, white)`
- **Light `surface-container-high`**: `color-mix(in srgb, {neutral} 10%, white)`
- **Light `outline`**: `color-mix(in srgb, {neutral} 35%, white)`
- **Light `outline-variant`**: `color-mix(in srgb, {neutral} 16%, white)`
- **Light `on-surface`** (headings *and* body): `color-mix(in srgb, {neutral} 30%, black)`
- **Light `on-surface-variant`**: `{neutral}`

### Tonal containers — derived from each signal color

- **Container (light)**: `color-mix(in srgb, <signal> 14%, white)` · **On-container (light)**: `color-mix(in srgb, <signal> 65%, black)`
- **Container (dark)**: `color-mix(in srgb, <signal> 24%, black)` · **On-container (dark)**: `color-mix(in srgb, <signal> 70%, white)`

---

## 🔤 Typography

- **Primary**: brand primary font, stack `"<font>", system-ui, -apple-system, sans-serif`.
- **Monospace** (code, data, IDs): brand mono font, then `monospace`.
- **Hierarchy** (M3 type scale): headings 600/700 weight in the same `on-surface` color as body; body 400, line height 1.5–1.6; labels 500, slightly tighter tracking.

---

## 🗺️ UI Component Standards

1. **Cards**: `--shape-lg` radius, `surface-container-low` background, `outline-variant` border, elevation via shadow.
2. **Buttons & chips**: filled primary = `primary`, full-pill shape, M3 state layers. Status chips use the tonal container/on-container pattern — never a solid badge. Prefer a segmented button over two near-duplicate forms.
3. **Logos & brand files**: use only files listed in `brand/brand.md`'s manifest (logos, fonts, tokens, references) — pick the light- or dark-surface variant based on the surface the logo actually sits on. With template defaults there is no logo; use the project name as text.

---

## 🛠️ CSS Variables Reference (template defaults)

If `aiworkspace/brand/tokens/` holds supplied token files, treat them as the source and keep `brand/brand.md` in sync with them. Put tokens wherever `brand/brand.md` says the project keeps them (Tailwind theme, CSS variables file, design-token JSON, …). This is the plain-CSS form, filled with the defaults — swap in `brand/brand.md` values when Brand is `custom`:

```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {
  /* ---- Core colors (the only hand-entered hexes) ---- */
  --brand-neutral: #475569;
  --brand-primary: #2563EB;
  --brand-secondary: #0891B2;
  --brand-success: #16A34A;
  --brand-warning: #D97706;
  --brand-error: #DC2626;
  --brand-white: #FFFFFF;

  /* ---- Typography ---- */
  --font-default: 'IBM Plex Sans', system-ui, -apple-system, sans-serif;
  --font-mono: 'IBM Plex Mono', monospace;

  /* ---- M3 shape scale ---- */
  --shape-xs: 4px;
  --shape-sm: 8px;
  --shape-md: 12px;
  --shape-lg: 16px;
  --shape-xl: 28px;
  --shape-full: 999px;
}

:root[data-theme="dark"] {
  --md-surface: color-mix(in srgb, var(--brand-neutral) 18%, black);
  --md-surface-container-low: color-mix(in srgb, var(--brand-neutral) 26%, black);
  --md-surface-container: color-mix(in srgb, var(--brand-neutral) 34%, black);
  --md-surface-container-high: color-mix(in srgb, var(--brand-neutral) 44%, black);
  --md-outline: var(--brand-neutral);
  --md-on-surface: var(--brand-white);
  --md-on-surface-variant: color-mix(in srgb, var(--brand-neutral) 55%, white);
}

:root[data-theme="light"] {
  --md-surface: color-mix(in srgb, var(--brand-neutral) 3%, white);
  --md-surface-container-low: var(--brand-white);
  --md-surface-container: color-mix(in srgb, var(--brand-neutral) 6%, white);
  --md-surface-container-high: color-mix(in srgb, var(--brand-neutral) 10%, white);
  --md-outline: color-mix(in srgb, var(--brand-neutral) 35%, white);
  --md-on-surface: color-mix(in srgb, var(--brand-neutral) 30%, black);
  --md-on-surface-variant: var(--brand-neutral);
}

body {
  font-family: var(--font-default);
  background-color: var(--md-surface);
  color: var(--md-on-surface);
}
```
