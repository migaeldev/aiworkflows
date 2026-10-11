---
type: skill
name: sql-injection-audit
title: SQL & Query Injection Audit Skill
description: Audits source code, database access layers, and ORM queries for SQL and data store injection vulnerabilities. USE WHEN the user says "Check for SQL injection", "Audit database queries", "Review ORM security", or asks to check for unescaped database inputs.
status: finalized
tags: [security, sql-injection, sqli, bigquery, database-security, parameterization]
timestamp: 2026-09-16T16:01:29+02:00
---

# 🛡️ SQL & Query Injection Audit Skill

This skill defines the audit methodology for detecting unparameterized database queries, raw string concatenation in SQL/NoSQL queries, and data store injection risks.

---

## 📌 Objective

Systematically scan source code, BigQuery analytical models, and database access modules to identify unparameterized queries, unsafe ORM raw executions, and injection risks across relational, analytical, and NoSQL databases.

---

## 🎯 Core Directives

1. **Trace Taint Paths**:
   Map user-controlled inputs (HTTP params, request bodies, query params, headers) directly to database query execution sinks.
2. **Verify Parameterization**:
   Treat all dynamic string formatting or concatenation in database calls as critical vulnerabilities regardless of framework sanitization claims.

---

## 📋 Audit Checklist

- **Raw SQL Queries**: Scan for string formatting/concatenation (`f"SELECT..."`, `String.format()`, `+` operators, `%` formatting) inside `db.query()` or `bigquery_client.query()` calls.
- **BigQuery Parameterization**: Verify BigQuery queries use `ScalarQueryParameter`, `ArrayQueryParameter`, or parameterized QueryJobConfig objects.
- **Unsafe ORM Methods**: Check for unescaped raw methods (e.g., Sequelize `sequelize.query()`, TypeORM `qb.where("id = " + id)`, Prisma `$queryRawUnsafe`).
- **NoSQL Injection**: Audit MongoDB/Document store calls for unvalidated object inputs passed directly into filters (e.g., `db.collection.find(req.body)` allowing `$gt` operator injection).
- **Stored Procedures & Dynamic Building**: Inspect database migration scripts and stored procedures for `EXECUTE IMMEDIATE` or dynamic SQL building with unescaped variables.

---

## 📝 Output Formatting & Reporting Standard

Structure findings using the standardized finding format below:

**Finding Format:**
* **Severity**: `CRITICAL` | `HIGH` | `MEDIUM` | `LOW`
* **Finding**: Concise descriptive title
* **CWE Mapping**: CWE Reference (e.g., `CWE-89: SQL Injection`)
* **Location**: `path/to/file:line_number`
* **Evidence**: Code snippet demonstrating unparameterized query
* **Remediation**: Corrected code snippet using query parameters
