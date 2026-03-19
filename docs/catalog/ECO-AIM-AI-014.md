# ECO-AIM-AI-014

**Name:** Inefficient feature preprocessing pipelines

**Category:** AIM

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Preprocessing waste increases training and inference cost.

## Impact

- **confidence:** 0.55
- **notes:** Measure and optimize hotspots.
- **type:** cpu

## Detection

- **languages:**
  - python
- **method:** trace

## Remediation

- **guidance:** Cache features; vectorize; batch transforms.
- **tradeoffs:** Complexity.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
