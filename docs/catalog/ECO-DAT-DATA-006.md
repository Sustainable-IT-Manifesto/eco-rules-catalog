# ECO-DAT-DATA-006

**Name:** Excessive replication factor

**Category:** Data

**Family:** Data

**Primary layer:** `data`

**System layers:** `data`

## Description

High replication increases storage and write amplification.

## Impact

- **confidence:** 0.55
- **notes:** Context-dependent; validate requirements.
- **type:** storage

## Detection

- **languages:** `infra`
- **method:** config

## Remediation

- **guidance:** Right-size replication; use tiered durability patterns.
- **tradeoffs:** Risk if requirements misunderstood.

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
