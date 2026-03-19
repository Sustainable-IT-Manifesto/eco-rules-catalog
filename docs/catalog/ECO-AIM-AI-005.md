# ECO-AIM-AI-005

**Name:** Always-on inference endpoints

**Category:** AIM

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Always-on endpoints waste baseline compute when idle.

## Impact

- **confidence:** 0.6
- **notes:** High for GPU-backed endpoints.
- **type:** carbon

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Autoscale; scale-to-zero where feasible; consolidate endpoints.
- **tradeoffs:** Cold starts and scheduling complexity.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
