# ECO-DAT-DATA-011

**Name:** Lack of compression in object storage

**Category:** DAT

**Family:** DATA

**Primary layer:** `data`

**System layers:** `data`

## Description

Uncompressed objects waste storage and bandwidth.

## Impact

- **confidence:** 0.7
- **notes:** Especially strong for text/structured data.
- **type:** storage

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Compress at write; enforce content-encoding where appropriate.
- **tradeoffs:** CPU overhead at read/write.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
