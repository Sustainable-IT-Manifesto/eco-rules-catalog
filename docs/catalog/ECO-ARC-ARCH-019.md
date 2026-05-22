# ECO-ARC-ARCH-019

**Name:** Overly aggressive autoscaling thresholds

**Category:** Architecture

**Family:** Architecture

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Aggressive scaling can cause thrash and wasted churn.

## Impact

- **confidence:** 0.5
- **notes:** Needs measurement.
- **type:** cost

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Add stabilization windows and sane thresholds.
- **tradeoffs:** Slower response to spikes.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
