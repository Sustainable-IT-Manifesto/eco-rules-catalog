# ECO-CMP-JS-009

**Name:** Unbounded promise chains

**Category:** CMP

**Family:** JS

**Primary layer:** `code`

**System layers:** `code`

## Description

Long or recursive promise chains can leak work and increase memory usage.

## Impact

- **confidence:** 0.55
- **notes:** Depends on implementation.
- **type:** memory

## Detection

- **languages:**
  - javascript
- **method:** hybrid

## Remediation

- **guidance:** Bound retries; avoid recursion; use iterative loops with limits.
- **tradeoffs:** Logic changes.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
