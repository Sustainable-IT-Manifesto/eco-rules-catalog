# ECO-AIM-AI-008

**Name:** Re-training without drift detection

**Category:** AIM

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Training without drift checks wastes compute and introduces risk.

## Impact

- **confidence:** 0.6
- **notes:** High compute waste risk.
- **type:** cost

## Detection

- **languages:**
  - org
- **method:** config

## Remediation

- **guidance:** Add drift detection and training triggers.
- **tradeoffs:** Monitoring complexity.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
