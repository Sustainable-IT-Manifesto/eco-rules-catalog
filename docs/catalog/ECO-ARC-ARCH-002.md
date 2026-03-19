# ECO-ARC-ARCH-002

**Name:** Always-on low-traffic service

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Services running 24/7 with low utilization create baseline waste.

## Impact

- **confidence:** 0.6
- **notes:** High if many services are idle.
- **type:** carbon

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Evaluate scale-to-zero, serverless, or consolidation.
- **tradeoffs:** Cold starts / architecture changes.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
