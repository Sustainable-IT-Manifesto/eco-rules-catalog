# ECO-ORG-PROC-005

**Name:** Feature shipped without load testing

**Category:** ORG

**Family:** PROC

**Primary layer:** `process`

**System layers:** `process`

## Description

Skipping load tests creates risk and often forces wasteful overprovisioning.

## Impact

- **confidence:** 0.75
- **notes:** Systemic.
- **type:** reliability

## Detection

- **languages:**
  - org
- **method:** config

## Remediation

- **guidance:** Add load tests and regression gates tied to SLOs.
- **tradeoffs:** More pipeline time.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
