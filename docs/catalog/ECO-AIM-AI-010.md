# ECO-AIM-AI-010

**Name:** Overly frequent fine-tuning cycles

**Category:** AIM

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Frequent tuning without clear value wastes compute.

## Impact

- **confidence:** 0.55
- **notes:** Depends on pipeline.
- **type:** cost

## Detection

- **languages:**
  - org
- **method:** trace

## Remediation

- **guidance:** Set tuning cadence based on outcomes and drift.
- **tradeoffs:** May delay improvements.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
