---
type: skill
name: ci-cd-security-review
title: CI/CD Security Review
description: Systematic security review of CI/CD pipeline configurations (GitHub Actions, GitLab CI, Cloud Build, Jenkins) mapped to the OWASP Top 10 CI/CD Security Risks. Use when auditing CI/CD pipelines, reviewing deployment workflows, checking GitHub Actions, or verifying build security.
tags: [skill, security, ci-cd, owasp, devsecops]
timestamp: 2026-09-16T15:01:13+02:00
---

# CI/CD Security Review

## Trigger
Use when reviewing CI/CD pipeline configurations, workflow scripts (e.g. `.github/workflows/*.yml`, `.gitlab-ci.yml`, `cloudbuild.yaml`, `deploy.sh`), runner environments, or deployment automation.

## Mindset
Act as a DevSecOps engineer performing a security audit under an **Assume Breach** model. Assume developer accounts could be compromised, PRs may contain malicious inputs, or untrusted third-party actions/dependencies could be poisoned.

## Review Checklist (OWASP Top 10 CI/CD Security Risks)

### 1. Poisoned Pipeline Execution (CICD-SEC-04)
- Untrusted inputs (PR titles, issue comments, branch names) passed directly into shell run steps or `eval`.
- Dangerous triggers like `pull_request_target` checking out untrusted code without strict validation.
- Insecure script invocations (`curl | bash`).

### 2. Inadequate Identity & Access Management (CICD-SEC-03)
- Excessive permissions on default job tokens (e.g. `GITHUB_TOKEN` having implicit write access instead of explicit `permissions: { contents: read }`).
- Containers or pipeline execution steps running unnecessarily as `root`.
- Overly permissive GCP/AWS/Azure IAM service accounts tied to CI runners.

### 3. Insufficient Credential Hygiene (CICD-SEC-06)
- Hardcoded secrets, API keys, or long-lived service account keys in workflow files or repository code.
- Unmasked secrets logged to stdout/stderr.
- Global environment export of secrets where untrusted scripts or dependencies can exfiltrate them.

### 4. Dependency & Artifact Integrity (CICD-SEC-07)
- Use of unpinned third-party dependencies or actions (e.g. using `@v1` or `:latest` instead of pinning to an immutable commit SHA digest).
- Missing artifact signing (e.g. via Cosign/Sigstore) or checksum verification prior to deployment.
- Unauthenticated or insecure container image pushes/pulls.

## Output Format

Structure all security review reports as follows:

```markdown
# CI/CD Security Review Report

## Executive Summary
[Brief high-level summary of pipeline security posture and total issue counts]

## Vulnerability Findings

### 1. [Finding Title]
- **Severity**: CRITICAL | HIGH | MEDIUM | LOW
- **OWASP Ref**: [e.g., CICD-SEC-04: Poisoned Pipeline Execution]
- **Location**: `[file_path]:[line_number]`
- **Impact**: [What an attacker can achieve]
- **Evidence**:
  ```yaml
  # Insecure snippet
  ```
- **Remediation**:
  ```yaml
  # Secure code (Binding to an environment variable safely)
  env:
  PR_TITLE: ${{ github.event.pull_request.title }}
  run: echo "Compiling branch $PR_TITLE"
  ```

## Security Best Practices & Recommendations
[General pipeline hardening advice]
```
