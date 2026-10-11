---
type: skill
name: web-performance-audit
title: Web Performance Audit Skill
description: Audits frontend code for Core Web Vitals regressions, bundle bloat, render-blocking resources, and wasteful client-side fetching. USE WHEN the user says "check performance", "audit bundle size", "why is this slow", "review Core Web Vitals", or asks about render blocking, re-renders, or load time.
status: finalized
tags: [engineering, performance, web-vitals, frontend, bundle-size]
timestamp: 2026-10-11T00:00:00+02:00
---

# 🚀 Web Performance Audit Skill

This skill defines the audit methodology for detecting frontend performance regressions: Core Web Vitals risks, bundle/code-splitting issues, render-blocking resources, and client-side fetch waste.

---

## 📌 Objective

Systematically scan frontend source, build configuration, and network/render behavior to identify what will slow down load time, interaction responsiveness, or visual stability for real users — not just what looks inefficient in isolation.

---

## 🎯 Core Directives

1. **Measure before guessing**: prefer a profiler, Lighthouse/PageSpeed run, bundle analyzer output, or `performance.now()` timing over reading code and assuming impact. If no measurement is available, say so and treat findings as hypotheses, not verified regressions.
2. **User-facing impact first**: rank findings by what a real user on a real connection experiences (LCP/CLS/INP), not by what's architecturally untidy.

---

## 📋 Audit Checklist

- **Core Web Vitals**: Largest Contentful Paint (unoptimized hero images/fonts, slow server response, render-blocking CSS/JS before the LCP element), Cumulative Layout Shift (images/ads/embeds without reserved dimensions, late-injected content above existing content, FOUT/FOIT from web fonts), Interaction to Next Paint (long tasks on the main thread, unthrottled event handlers, heavy synchronous work in click/input handlers).
- **Bundle Size & Code-Splitting**: unsplit routes/components that pull the whole app into one chunk, large dependencies imported for a single utility function (check for a lighter alternative or tree-shakeable import), duplicate dependencies across chunks, missing dynamic `import()` for below-the-fold or rarely-used code.
- **Render-Blocking Resources**: synchronous `<script>` tags in `<head>` without `defer`/`async`/`type="module"`, blocking `@import` CSS chains, web fonts without `font-display: swap`/`optional` or `<link rel="preload">`.
- **Image & Font Loading**: missing `width`/`height` or `aspect-ratio` (CLS risk), images not served in modern formats (WebP/AVIF) or not responsive (`srcset`/`sizes`), missing `loading="lazy"` on below-the-fold images, un-subset or too many font weights/families loaded.
- **Unnecessary Re-renders**: expensive computations or component trees re-rendering on every parent update without memoization, state subscriptions broader than the component actually needs, missing keys causing full list re-mounts.
- **Client-Side Fetch Waste**: N+1 fetches (a list loaded, then one request per item), missing request deduplication/caching for data fetched in multiple components, waterfalled requests that could run in parallel, over-fetching (requesting fields/pages that aren't rendered).

---

## 📝 Output Formatting & Reporting Standard

Structure findings using the standardized finding format below:

**Finding Format:**
* **Severity**: `CRITICAL` | `HIGH` | `MEDIUM` | `LOW`
* **Finding**: Concise descriptive title
* **Metric Affected**: `LCP` | `CLS` | `INP` | `Bundle Size` | `TTFB` | `Network`
* **Location**: `path/to/file:line_number`
* **Evidence**: Measurement (profiler trace, Lighthouse score, bundle analyzer output, timing) or, if unmeasured, the code pattern that predicts the regression — labeled as a hypothesis
* **Remediation**: Corrected code/config snippet or concrete next step
