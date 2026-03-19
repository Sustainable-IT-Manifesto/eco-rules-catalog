# ECO-ORG-PROC-007

**Name:** No energy-aware CI/CD metrics

**Category:** ORG

**Family:** PROC

**Primary layer:** `process`

**System layers:** `process`

## Description

Build/test pipelines can waste large amounts of compute when unmeasured.

## Impact

- **confidence:** 0.7
- **notes:** Depends on org scale.
- **type:** cost

## Detection

- **languages:**
  - org
- **method:** config

## Remediation

- **guidance:** Measure build minutes, cache hits, and pipeline efficiency; reduce waste.
- **tradeoffs:** Instrumentation effort.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
