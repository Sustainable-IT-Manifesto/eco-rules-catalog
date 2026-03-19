# ECO-NET-NET-005

**Name:** Missing timeouts

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Missing timeouts remove a critical reliability boundary for network calls.

## Impact

- **confidence:** 0.85
- **notes:** High propagation during partial outages.
- **type:** reliability

## Detection

- **languages:**
  - python
  - javascript
  - java
  - infra
- **method:** hybrid

## Remediation

- **guidance:** Set explicit connect/read timeouts; standardize defaults.
- **tradeoffs:** Endpoint tuning required.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
