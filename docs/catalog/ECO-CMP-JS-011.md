# ECO-CMP-JS-011

**Name:** Inefficient array transformations (multi-pass)

**Category:** CMP

**Family:** JS

**Primary layer:** `code`

**System layers:** `code`

## Description

Multiple passes over arrays increases CPU and GC overhead.

## Impact

- **confidence:** 0.55
- **notes:** Context-dependent.
- **type:** cpu

## Detection

- **languages:**
  - javascript
- **method:** ast

## Remediation

- **guidance:** Combine passes in hot paths; keep readability elsewhere.
- **tradeoffs:** Potential readability loss.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
