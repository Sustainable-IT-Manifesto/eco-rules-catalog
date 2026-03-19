# ECO-CMP-PY-017

**Name:** Large object retained in global scope

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Long-lived globals can cause persistent memory bloat.

## Impact

- **confidence:** 0.65
- **notes:** Often invisible until scale.
- **type:** memory

## Detection

- **languages:**
  - python
- **method:** hybrid

## Remediation

- **guidance:** Avoid storing large payloads globally; use caching with eviction.
- **tradeoffs:** May require new cache strategy.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
