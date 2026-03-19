# ECO-CMP-PY-004

**Name:** Blocking I/O inside async context

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Blocking calls inside async functions reduce concurrency and inflate latency.

## Impact

- **confidence:** 0.9
- **notes:** High propagation in async servers.
- **type:** latency

## Detection

- **languages:**
  - python
- **method:** ast

## Remediation

- **guidance:** Use async-compatible libraries (e.g., async DB/HTTP clients).
- **tradeoffs:** Library and code changes.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
