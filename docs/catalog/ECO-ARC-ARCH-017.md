# ECO-ARC-ARCH-017

**Name:** Inefficient container image size

**Category:** ARC

**Family:** ARCH

**Primary layer:** `architecture`

**System layers:** `architecture`

## Description

Large images increase pull time and wasted storage/transfer.

## Impact

- **confidence:** 0.55
- **notes:** Often quick win.
- **type:** network

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Use multi-stage builds and minimal base images.
- **tradeoffs:** Build refactor.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
