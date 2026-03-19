# ECO-ARC-ARCH-019

**Name:** Overly aggressive autoscaling thresholds

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Aggressive scaling can cause thrash and wasted churn.

## Impact

- **confidence:** 0.5
- **notes:** Needs measurement.
- **type:** cost

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Add stabilization windows and sane thresholds.
- **tradeoffs:** Slower response to spikes.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
