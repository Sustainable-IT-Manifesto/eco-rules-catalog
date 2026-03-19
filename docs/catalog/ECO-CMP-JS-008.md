# ECO-CMP-JS-008

**Name:** Excessive DOM reflow

**Category:** CMP

**Family:** JS

**Primary layer:** `code`

**System layers:** `code`

## Description

Layout thrashing increases CPU and drains battery.

## Impact

- **confidence:** 0.7
- **notes:** Common in complex UI interactions.
- **type:** cpu

## Detection

- **languages:**
  - javascript
- **method:** trace

## Remediation

- **guidance:** Batch DOM reads/writes; use requestAnimationFrame patterns.
- **tradeoffs:** Refactor UI code.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
