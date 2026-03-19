# ECO-NET-NET-014

**Name:** Synchronous cross-region calls

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Cross-region synchronous calls increase latency and cost.

## Impact

- **confidence:** 0.7
- **notes:** Often a structural design issue.
- **type:** latency

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Co-locate dependencies; async replicate; cache at edges.
- **tradeoffs:** Consistency tradeoffs.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
