---
type: skill
name: observability
title: Observability & Instrumentation
description: Structured logging, RED metrics (Rate/Errors/Duration), tracing, and symptom-based alerting — instrument code as you build it, not after an incident forces you to. Use when adding a new service, endpoint, background job, or any code path you'll need to debug in production without a repro.
tags: [skill, engineering, observability, logging, metrics, tracing, alerting]
timestamp: 2026-10-11T00:00:00+02:00
---

# Observability & Instrumentation

## Trigger
Use when adding a new service, endpoint, background job, queue consumer, or any code path that will run in production where you can't attach a debugger when it breaks. Instrument while writing the code, not as a follow-up task — by the time you need the data, it's too late to add it retroactively.

## Rationalizations
| Excuse | Why it's wrong | Do this instead |
| :--- | :--- | :--- |
| "I'll add logging if it turns out we need it" | By the time a production incident proves you need it, the data from the incident is already gone | Instrument the code path now, while you still know what matters about it |
| "A print/console.log is fine for now" | Unstructured logs can't be queried, filtered, or correlated across requests later | Use the project's structured logging convention from the first line, not a retrofit |
| "We'll alert on CPU/memory, that covers it" | A symptom a user feels (errors, latency) doesn't always correlate with a resource metric | Alert on user-visible symptoms directly (error rate, latency), not just infrastructure proxies |

## Core Practices

### Structured logging
Every log line should be queryable: consistent fields (not free-text interpolation), a correlation/request ID that ties related log lines together across a request's lifetime, and a log level that matches real severity (not everything is `error`). Follow whatever structured-logging convention `aiworkspace/codebase-map.md` or `project.md` already establishes for this codebase; if none exists, that's a gap worth flagging before adding more unstructured logs to it.

### RED metrics
For any service or endpoint, track the three numbers that answer "is this healthy right now":
- **Rate** — requests/events per unit time.
- **Errors** — the fraction failing, broken out by error type where it's cheap to do so.
- **Duration** — latency distribution (p50/p95/p99, not just an average — an average hides the tail that users actually feel).

### Tracing
Propagate a trace/correlation ID across every boundary a request crosses — service calls, queue hops, async jobs — so a slow or failed request can be followed end-to-end instead of reconstructed from timestamps across disconnected logs. This matters most exactly where locality is already low (see [`engineering/codebase-design`](../codebase-design/SKILL.md)): async and cross-service boundaries are where "what actually happened" is hardest to reconstruct after the fact without a trace.

### Symptom-based alerting
Alert on what a user would notice — elevated error rate, latency past a threshold, a critical flow failing — not on internal causes (CPU, queue depth) unless that cause maps directly to a symptom. A symptom-based alert tells you something is actually wrong; a cause-based alert pages you for things that may not matter yet, training people to ignore pages.

## Checklist
- [ ] New logs are structured (consistent fields, correlation ID, calibrated level) following the project's existing convention
- [ ] A new service/endpoint has Rate/Errors/Duration visibility, not just happy-path logging
- [ ] A trace/correlation ID crosses every boundary this change adds (service call, queue, async job)
- [ ] Any new alert is symptom-based (what a user feels), not a raw infrastructure threshold with no proven link to user impact
