# ECO-ARC-ARCH-014

**Name:** Stateful services blocking scaling

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Stateful designs make scaling expensive and fragile.

## Impact

- **confidence:** 0.6
- **notes:** Often structural.
- **type:** cost

## Detection

- **languages:**
  - infra
- **method:** hybrid

## Remediation

- **guidance:** Externalize state; use managed stores; reduce coupling.
- **tradeoffs:** Migration cost.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
