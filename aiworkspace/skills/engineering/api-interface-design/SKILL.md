---
type: skill
name: api-interface-design
title: API & Interface Design
description: Contract-first design for anything consumed by code outside your direct control — public APIs, libraries, shared internal services. Covers Hyrum's Law, the One-Version Rule, error semantics, and boundary validation. Use when designing or changing an API endpoint, a library's public interface, or any contract another team or codebase depends on.
tags: [skill, engineering, api, interface, contracts, versioning]
timestamp: 2026-10-11T00:00:00+02:00
---

# API & Interface Design

Distinct from [`engineering/codebase-design`](../codebase-design/SKILL.md): that skill is about internal module seams you control on both ends. This one is about contracts where you don't control the caller — a public API, a published library, a service other teams depend on. The cost of being wrong is paid by someone you can't see.

## Trigger
Use when designing or changing an API endpoint, a library's public interface, a shared internal service's contract, or anything else consumed by code you can't simultaneously edit.

## Rationalizations
| Excuse | Why it's wrong | Do this instead |
| :--- | :--- | :--- |
| "It's not in the documented contract, so changing it isn't breaking" | Hyrum's Law: with enough callers, every observable behavior becomes a dependency, documented or not | Treat observed behavior as part of the contract; check for real callers before changing it, not just the docs |
| "I'll just add a v2 and keep v1 around" | Every parallel version is a version you now maintain and test forever | Prefer the One-Version Rule: migrate callers forward, give v1 a sunset date, don't let versions accumulate indefinitely |
| "The error message is just for debugging, format doesn't matter" | Callers parse error messages and codes whether you intended them to or not — inconsistent error shape breaks their handling same as a behavior change | Define one error shape up front and keep it consistent across every endpoint/method |
| "The caller should validate their own input" | True for internal call sites you control; false at a boundary — you can't trust what you don't control | Validate at the boundary; trust only what's already been validated inside it |

## Core Principles

### Contract-first design
Write down the interface — request/response shape, method signature, error cases — before implementing it, and get it reviewed before the implementation locks it in by accident. Changing an interface after callers exist is an order of magnitude more expensive than changing a plan.

### Hyrum's Law
> "With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody."

Treat this as literal, not cautionary. Before changing *any* observable behavior — timing, ordering, error text, undocumented field presence — check for real callers, not just whether the docs mentioned it. If you can't check, assume someone depends on it and version the change instead of shipping it silently.

### The One-Version Rule
Prefer one supported version of a contract at a time. Each additional parallel version is permanent maintenance and test burden, not a one-time cost. When a breaking change is unavoidable: publish the new version, give the old one an explicit sunset date, migrate callers actively (don't wait for them to notice) — see [`engineering/deprecation-migration`](../deprecation-migration/SKILL.md) for the mechanics.

### Error semantics
Define one error shape for the whole surface (consistent fields: code, message, maybe a retryable flag) and use it everywhere — a caller that has to special-case error handling per endpoint is a caller whose code breaks every time you add an endpoint. Error codes/types are part of the contract: changing what an error means for an existing code is a breaking change even if the HTTP status stays the same. Never leak internal implementation details (stack traces, internal type names, raw DB errors) across the boundary.

### Boundary validation
Validate every input at the boundary — the first point where external data enters your system. Code on the far side of that boundary can trust the data; code on the near side (including the validation itself) must not. Don't push validation to the caller ("they should send good data") and don't re-validate redundantly deep inside the system once the boundary has already done it.

## Checklist
- [ ] The contract (shape, errors, versioning) is written down before implementation, not inferred from the final code
- [ ] Every behavior change was checked against Hyrum's Law — real callers, not just the docs
- [ ] No new parallel version was introduced without a sunset plan for the one it replaces
- [ ] Error shape is consistent with the rest of the surface; no internal details leak across the boundary
- [ ] Input is validated once, at the boundary — not trusted past it, not re-validated redundantly inside it
