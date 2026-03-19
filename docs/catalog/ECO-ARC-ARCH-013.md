# ECO-ARC-ARCH-013

**Name:** No caching layer for high-read workloads

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

High-read systems without caching waste CPU and DB capacity.

## Impact

- **confidence:** 0.65
- **notes:** Be careful with invalidation.
- **type:** cpu

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Introduce caching at appropriate boundaries.
- **tradeoffs:** Invalidation complexity.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
