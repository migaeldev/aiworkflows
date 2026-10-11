---
type: skill
name: mitm-prevention-audit
title: Man-in-the-Middle & Transport Security Audit Skill
description: Audit of network transport security, TLS/SSL configurations, HTTP client security, and encryption headers to prevent Man-in-the-Middle attacks. USE WHEN the user says "Check TLS security", "Audit MitM protections", "Review HTTP client security", "Check HSTS headers", or asks to verify transport encryption configs.
status: finalized
tags: [security, tls, ssl, mitm, transport-security, hsts]
timestamp: 2026-09-16T16:01:29+02:00
---

# 🛡️ Man-in-the-Middle (MitM) & Transport Security Audit Skill

This skill defines the audit methodology for evaluating transport security, TLS/SSL enforcement, HTTP client configurations, and encryption headers across application services.

---

## 📌 Objective

Identify weak transport security settings, insecure outbound HTTP clients, missing security headers, and unencrypted intra-service communication across application code, API integrations, and infrastructure manifests.

---

## 🎯 Core Directives

1. **Scan Backend Clients & Reverse Proxies**:
   Evaluate both inbound traffic (Nginx, API Gateways, Cloud Run ingress) and outbound HTTP clients (Requests, Axios, Fetch, gRPC, Google Cloud SDKs).
2. **Enforce Strict Certificate Validation**:
   Flag any setting or client flag that disables TLS verification or accepts invalid certificates.

---

## 📋 Audit Checklist

- **Disabled Certificate Validation**: Search for code explicitly disabling SSL verification (e.g., `rejectUnauthorized: false`, `verify=False`, `InsecureSkipVerify: true`).
- **Cleartext HTTP Usage**: Detect forced or fallback `http://` URLs for external endpoints, webhook deliveries, or internal microservices.
- **Security Headers Configuration**: Verify application or proxy configs enforce `Strict-Transport-Security` (HSTS) with `includeSubDomains` and `preload`.
- **Insecure TLS Versions & Cipher Suites**: Audit web server and gateway configs for outdated protocols (TLS 1.0, TLS 1.1) or weak ciphers (CBC mode, RC4, 3DES).
- **Certificate Pinning & Mutual TLS (mTLS)**: Check high-security APIs or service-to-service calls for missing mTLS enforcement or unverified upstream origins.

---

## 📝 Output Formatting & Reporting Standard

Structure findings using the standardized finding format below:

**Finding Format:**
* **Severity**: `CRITICAL` | `HIGH` | `MEDIUM` | `LOW`
* **Finding**: Concise descriptive title
* **CWE Mapping**: CWE Reference (e.g., `CWE-295: Improper Certificate Validation`)
* **Location**: `path/to/file:line_number`
* **Evidence**: Code snippet demonstrating vulnerability
* **Remediation**: Corrected code snippet with proper TLS validation
