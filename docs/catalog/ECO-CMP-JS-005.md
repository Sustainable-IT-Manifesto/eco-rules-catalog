# ECO-CMP-JS-005

**Name:** Blocking crypto in event loop

**Category:** CMP

**Family:** JS

**Primary layer:** `code`

**System layers:** `code`

## Description

CPU-heavy crypto blocks the event loop and inflates latency.

## Impact

- **confidence:** 0.75
- **notes:** Use workers for heavy CPU work.
- **type:** latency

## Detection

- **languages:**
  - javascript
- **method:** hybrid

## Remediation

- **guidance:** Move CPU-heavy crypto to worker threads or native async APIs.
- **tradeoffs:** Complexity increase.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
