# ECO-AIM-AI-009

**Name:** No evaluation before scaling model

**Category:** AIM

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Scaling without evaluation wastes resources and can degrade outcomes.

## Impact

- **confidence:** 0.7
- **notes:** Common governance gap.
- **type:** cost

## Detection

- **languages:**
  - org
- **method:** config

## Remediation

- **guidance:** Require eval gates before scaling model size/traffic.
- **tradeoffs:** Slower rollout.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
