---
type: skill
name: dos-resilience-audit
title: Application DoS & Resource Exhaustion Audit Skill
description: Systematic review of application-level Denial of Service (DoS) vectors including ReDoS, unbounded database queries, missing payload limits, and missing rate limiters. USE WHEN the user says "Audit for DoS vulnerabilities", "Check rate limiting", "Review ReDoS risks", "Audit resource consumption", or asks to evaluate application stability.
status: finalized
tags: [security, dos, redos, rate-limiting, resource-exhaustion]
timestamp: 2026-09-16T16:01:29+02:00
---

# 🛡️ Application DoS & Resource Exhaustion Audit Skill

This skill defines the systematic audit methodology for evaluating application resilience against application-level Denial of Service (DoS) attacks and resource exhaustion vectors.

---

## 📌 Objective

Detect application-level design flaws and algorithmic weaknesses that allow malicious actors to exhaust CPU, memory, database connections, bandwidth, or downstream LLM/API quotas.

---

## 🎯 Core Directives

1. **Focus on Asymmetric Workloads**:
   Identify small client requests that trigger disproportionately heavy server-side processing, uncontrolled query execution, or expensive LLM API invocations.
2. **Resource Boundary Enforcement**:
   Verify strict upper bounds for payload sizes, database queries, memory buffers, and rate limits across all exposed routes.

---

## 📋 Audit Checklist

- **Regular Expression DoS (ReDoS)**: Scan regex patterns for catastrophic backtracking risks (e.g., nested quantifiers `(a+)+` or overlapping clauses matched against user inputs).
- **Unbounded Database Pagination**: Check queries handling collections for missing `LIMIT` clauses or default pagination limits, preventing queries from loading massive datasets into RAM.
- **Uncapped Request Payloads & File Uploads**: Ensure HTTP server routes enforce strict body size limits (e.g., `Flask.config['MAX_CONTENT_LENGTH']`, `express.json({ limit: '100kb' })`) and stream large file uploads rather than buffering them into memory.
- **Unthrottled High-Cost Operations**: Verify that computationally expensive endpoints (password hashing, PDF generation, complex search queries, LLM synthesis triggers) are protected by rate limiters or queue mechanisms.
- **Zip Bombs / Recursive Parsing**: Audit file extractors, XML parsers, and JSON/YAML parsers for entity expansion or recursive nesting protections.

---

## 📝 Output Formatting & Reporting Standard

Structure findings using the standardized finding format below:

**Finding Format:**
* **Severity**: `CRITICAL` | `HIGH` | `MEDIUM` | `LOW`
* **Finding**: Concise descriptive title
* **CWE Mapping**: CWE Reference (e.g., `CWE-400: Uncontrolled Resource Consumption`)
* **Location**: `path/to/file:line_number`
* **Evidence**: Code snippet demonstrating vulnerability
* **Remediation**: Corrected code snippet with bound limits or rate control
