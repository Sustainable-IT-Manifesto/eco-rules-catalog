# ECO-DAT-DATA-008

**Name:** Storing ephemeral data permanently

**Category:** Data

**Family:** Data

**Primary layer:** `data`

**System layers:** `data`

## Description

Ephemeral data kept forever becomes waste by default.

## Impact

- **confidence:** 0.7
- **notes:** Often caused by missing TTLs.
- **type:** storage

## Detection

- **languages:** `infra`
- **method:** config

## Remediation

- **guidance:** Add TTL/expiration and lifecycle policies.
- **tradeoffs:** Risk if used unexpectedly later.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Data category](categories/dat/index.md)
- [Back to Data family](categories/dat/families/data/index.md)
- [Back to Rule Browser](../rule-browser.md)
