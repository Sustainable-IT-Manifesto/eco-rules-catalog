# ECO-CMP-PY-010

**Name:** Inefficient data structure choice

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Using lists for membership tests instead of sets/dicts increases CPU time.

## Impact

- **confidence:** 0.7
- **notes:** High impact when lookups are frequent.
- **type:** cpu

## Detection

- **languages:**
  - python
- **method:** ast

## Remediation

- **guidance:** Use set/dict for membership-heavy operations.
- **tradeoffs:** Memory tradeoff for speed.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
