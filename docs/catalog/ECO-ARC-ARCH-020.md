# ECO-ARC-ARCH-020

**Name:** Underutilized GPU/accelerator resources

**Category:** Architecture

**Family:** Architecture

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Accelerators running idle waste significant power and cost.

## Impact

- **confidence:** 0.65
- **notes:** High in AI workloads.
- **type:** cost

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Consolidate workloads; enable autoscaling; batch inference.
- **tradeoffs:** Scheduling complexity.

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
