# ECO-CMP-PY-016

**Name:** No connection pooling

**Category:** CMP

**Family:** PY

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Lack of pooling increases connection churn, latency, and DB load.

## Impact

- **confidence:** 0.8
- **notes:** Especially important in serverless/short-lived contexts.
- **type:** latency

## Detection

- **languages:**
  - python
- **method:** config

## Remediation

- **guidance:** Enable and tune pooling; set max connections.
- **tradeoffs:** Tuning required to avoid saturation.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
