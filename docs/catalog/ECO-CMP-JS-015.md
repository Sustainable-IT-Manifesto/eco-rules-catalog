# ECO-CMP-JS-015

**Name:** Recreating large objects per render

**Category:** CMP

**Family:** JS

**Primary layer:** `code`

**System layers:** `code`

## Description

Allocating large objects repeatedly increases GC churn and CPU.

## Impact

- **confidence:** 0.55
- **notes:** Depends on render frequency.
- **type:** cpu

## Detection

- **languages:**
  - javascript
- **method:** hybrid

## Remediation

- **guidance:** Memoize stable objects; move creation outside render paths.
- **tradeoffs:** Potential for stale data if misused.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
