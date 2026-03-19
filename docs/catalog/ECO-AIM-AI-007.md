# ECO-AIM-AI-007

**Name:** No model quantization

**Category:** AIM

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Failure to quantize when appropriate wastes inference compute.

## Impact

- **confidence:** 0.55
- **notes:** Model-dependent.
- **type:** cost

## Detection

- **languages:**
  - infra
- **method:** config

## Remediation

- **guidance:** Evaluate quantization for inference workloads.
- **tradeoffs:** Potential quality/compatibility changes.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
