# ECO-CMP-JS-010

**Name:** Missing request timeout

**Category:** CMP

**Family:** JS

**Primary layer:** `network`

**System layers:** `network`

## Description

Requests without timeouts hang and create cascading latency.

## Impact

- **confidence:** 0.85
- **notes:** High propagation risk.
- **type:** reliability

## Detection

- **languages:**
  - javascript
- **method:** hybrid

## Remediation

- **guidance:** Use AbortController / client timeouts; set defaults.
- **tradeoffs:** Endpoint tuning.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
