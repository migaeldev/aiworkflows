---
type: skill
name: security-code-audit
title: Security Code Audit
description: Systematic audit of core application security mechanisms (Authentication, Authorization, Cryptography, Session Management, and Input Validation) across a codebase. Use when auditing security controls, reviewing authentication code, checking access control implementation, or evaluating cryptography.
tags: [skill, security, audit, appsec, owasp]
timestamp: 2026-09-16T15:01:13+02:00
---

# Codebase Security Mechanism Audit

## Trigger
Use when auditing security controls, reviewing authentication/authorization logic, checking access control implementation, or evaluating cryptographic usage.

## Mindset
Act as a senior application security engineer evaluating defensive controls within the codebase using the OWASP Application Security Verification Standard (ASVS) framework.

## Review Checklist

### 1. Authentication & Session Management (ASVS V2 & V3)
- **Credential Storage:** Verify passwords/keys are hashed using memory-hard algorithms (Argon2id, bcrypt, PBKDF2) with proper work factors and salts.
- **Session Lifecycles:** Audit session tokens (JWTs, cookies) for secure attributes (`Secure`, `HttpOnly`, `SameSite=Strict/Lax`), reasonable expiration timeframes, and explicit revocation logic on logout/password reset.
- **MFA & Recovery:** Ensure step-up authentication or password reset flows cannot be bypassed via direct object references or missing verification steps.

### 2. Access Control & Authorization (ASVS V4)
- **Enforcement Pattern:** Check whether access controls are enforced server-side at a centralized middleware/gateway layer rather than relying on client-side logic or ad-hoc controller checks.
- **IDOR / BOLA:** Verify that every data access endpoint validates ownership or explicit tenant boundaries (e.g., checking `WHERE user_id = current_user.id` rather than trusting user-supplied parameters).
- **Role Alignment:** Ensure RBAC/ABAC logic correctly handles default-deny configurations and handles edge cases (e.g., role escalation via API payload manipulation).

### 3. Cryptography & Data Protection (ASVS V6 & V7)
- **Algorithm Selection:** Scan for weak or deprecated algorithms (MD5, SHA1, DES, RC4, ECB mode for AES).
- **Key Management:** Ensure cryptographic keys, initialization vectors (IVs), and salts are generated using cryptographically secure pseudorandom number generators (CSPRNG) and are not hardcoded in source files.

### 4. Input Validation & Encoding Frameworks (ASVS V5)
- **Centralized Validation:** Check for type-safe validation schemas (e.g., Zod, Pydantic, Bean Validation) applied at input boundaries.
- **Context-Aware Output Encoding:** Ensure dynamic data passed to template engines, database queries, or system calls uses parameterized queries or context-aware encoding.

### 5. Resiliency & Audit Logging (ASVS V8 & V13)
- **Anti-Abuse Controls:** Verify rate-limiting mechanisms exist on sensitive endpoints (login, password reset, payment processing, file uploads).
- **Security Audit Logs:** Ensure security-relevant events (authentication failures, access denials, privilege changes) are logged with context without recording sensitive data (PII, passwords, full tokens).

## Output Format

```markdown
# Security Mechanism Audit Report

## Executive Summary
[High-level summary of security control evaluation]

## Vulnerability Findings

### 1. [Finding Title]
- **Severity**: CRITICAL | HIGH | MEDIUM | LOW
- **ASVS Mapping**: [e.g., V4.1.1 - Access Control Architecture]
- **Location**: `[file_path]:[line_number]`
- **Impact**: [What an attacker can achieve]
- **Evidence**:
  ```javascript
  // Insecure code
  ```
- **Remediation**:
  ```javascript
  app.post('/api/user/update', authenticate, async (req, res) => {
    // Enforcement tied directly to authenticated session context
    await User.update(req.user.id, req.body.data);
  });
  ```

