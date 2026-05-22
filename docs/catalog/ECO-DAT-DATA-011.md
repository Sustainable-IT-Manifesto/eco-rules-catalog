# ECO-DAT-DATA-011

**Name:** Lack of compression in object storage

**Category:** Data

**Family:** Data

**Primary layer:** `data`

**System layers:** `data`

## Description

Uncompressed objects waste storage and bandwidth.

## Impact

- **confidence:** 0.7
- **notes:** Especially strong for text/structured data.
- **type:** storage

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Compress at write; enforce content-encoding where appropriate.
- **tradeoffs:** CPU overhead at read/write.

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
