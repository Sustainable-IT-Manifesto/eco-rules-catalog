# ECO-ARC-ARCH-002

**Name:** Always-on low-traffic service

**Category:** Architecture

**Family:** Architecture

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Services running 24/7 with low utilization create baseline waste.

## Impact

- **confidence:** 0.6
- **notes:** High if many services are idle.
- **type:** carbon

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Evaluate scale-to-zero, serverless, or consolidation.
- **tradeoffs:** Cold starts / architecture changes.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Architecture category](categories/arc/index.md)
- [Back to Architecture family](categories/arc/families/arch/index.md)
- [Back to Rule Browser](../rule-browser.md)
