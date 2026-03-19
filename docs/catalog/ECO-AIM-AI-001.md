# ECO-AIM-AI-001

**Name:** Oversized model selection

**Category:** AIM

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Using larger models than needed increases inference cost and emissions.

## Impact

- **confidence:** 0.6
- **notes:** Workload-dependent.
- **type:** carbon

## Detection

- **languages:**
  - python
  - infra
- **method:** config

## Remediation

- **guidance:** Benchmark smaller models and quantify tradeoffs before scaling.
- **tradeoffs:** May reduce marginal quality.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
