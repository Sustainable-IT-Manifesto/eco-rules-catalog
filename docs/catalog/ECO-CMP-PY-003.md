# ECO-CMP-PY-003

**Name:** Repeated invariant computation inside loop

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Recomputing values that do not change inside a loop wastes CPU cycles.

## Impact

- **confidence:** 0.6
- **notes:** Best targeted when loop counts are high.
- **type:** cpu

## Detection

- **languages:**
  - python
- **method:** ast

## Remediation

- **guidance:** Move invariant work outside the loop.
- **tradeoffs:** Minimal.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
