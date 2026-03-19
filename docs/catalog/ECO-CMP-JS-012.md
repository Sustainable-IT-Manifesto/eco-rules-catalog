# ECO-CMP-JS-012

**Name:** Redundant API calls in component lifecycle

**Category:** CMP

**Family:** JS

**Primary layer:** `network`

**System layers:** `network`

## Description

Repeated fetches on rerender waste network and CPU.

## Impact

- **confidence:** 0.7
- **notes:** Common in SPAs.
- **type:** network

## Detection

- **languages:**
  - javascript
- **method:** trace

## Remediation

- **guidance:** Cache results; dedupe requests; stabilize dependencies.
- **tradeoffs:** State management changes.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
