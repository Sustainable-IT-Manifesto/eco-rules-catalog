# ECO-DAT-DATA-004

**Name:** Logs stored indefinitely

**Category:** DAT

**Family:** DATA

**Primary layer:** `data`

**System layers:** `data`

## Description

Indefinite log retention increases storage and cost without clear value.

## Impact

- **confidence:** 0.8
- **notes:** Often a top cost line item.
- **type:** storage

## Detection

- **languages:**
  - infra
- **method:** config

## Remediation

- **guidance:** Set retention and tiering; sample where appropriate.
- **tradeoffs:** Less historical detail unless archived.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
