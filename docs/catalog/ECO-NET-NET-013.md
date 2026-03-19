# ECO-NET-NET-013

**Name:** Excessive polling intervals

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Frequent polling increases load even when nothing changes.

## Impact

- **confidence:** 0.75
- **notes:** Often large at scale.
- **type:** network

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Use push mechanisms; increase intervals; add caching and ETags.
- **tradeoffs:** More event infrastructure.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
