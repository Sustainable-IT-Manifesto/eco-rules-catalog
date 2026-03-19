# ECO-ARC-ARCH-005

**Name:** No resource limits in containers

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Missing CPU/memory limits causes noisy-neighbor waste and instability.

## Impact

- **confidence:** 0.75
- **notes:** Also drives over-provisioning for safety.
- **type:** reliability

## Detection

- **languages:**
  - infra
- **method:** config

## Remediation

- **guidance:** Set requests/limits; right-size with metrics.
- **tradeoffs:** Requires tuning to avoid throttling.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
