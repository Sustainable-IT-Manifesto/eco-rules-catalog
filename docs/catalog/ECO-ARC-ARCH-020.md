# ECO-ARC-ARCH-020

**Name:** Underutilized GPU/accelerator resources

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Accelerators running idle waste significant power and cost.

## Impact

- **confidence:** 0.65
- **notes:** High in AI workloads.
- **type:** cost

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Consolidate workloads; enable autoscaling; batch inference.
- **tradeoffs:** Scheduling complexity.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
