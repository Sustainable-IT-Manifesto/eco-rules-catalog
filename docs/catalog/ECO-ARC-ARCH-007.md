# ECO-ARC-ARCH-007

**Name:** Batch jobs run too frequently

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Over-scheduling batch jobs wastes compute and increases cost.

## Impact

- **confidence:** 0.65
- **notes:** Good target for quick savings.
- **type:** cost

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Right-size schedules; trigger on events; add change-detection.
- **tradeoffs:** More complex orchestration.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
