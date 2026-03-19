# ECO-DAT-DATA-006

**Name:** Excessive replication factor

**Category:** DAT

**Family:** DATA

**Primary layer:** `data`

**System layers:** `data`

## Description

High replication increases storage and write amplification.

## Impact

- **confidence:** 0.55
- **notes:** Context-dependent; validate requirements.
- **type:** storage

## Detection

- **languages:**
  - infra
- **method:** config

## Remediation

- **guidance:** Right-size replication; use tiered durability patterns.
- **tradeoffs:** Risk if requirements misunderstood.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
