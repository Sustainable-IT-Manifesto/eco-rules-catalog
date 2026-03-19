# ECO-DAT-DATA-008

**Name:** Storing ephemeral data permanently

**Category:** DAT

**Family:** DATA

**Primary layer:** `data`

**System layers:** `data`

## Description

Ephemeral data kept forever becomes waste by default.

## Impact

- **confidence:** 0.7
- **notes:** Often caused by missing TTLs.
- **type:** storage

## Detection

- **languages:**
  - infra
- **method:** config

## Remediation

- **guidance:** Add TTL/expiration and lifecycle policies.
- **tradeoffs:** Risk if used unexpectedly later.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
