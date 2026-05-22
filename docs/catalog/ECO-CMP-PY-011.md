# ECO-CMP-PY-011

**Name:** Repeated JSON serialization cycles

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Serializing/deserializing repeatedly wastes CPU and increases latency.

## Impact

- **confidence:** 0.65
- **notes:** Often appears in middleware layers.
- **type:** cpu

## Detection

- **languages:** `python`
- **method:** hybrid

## Remediation

- **guidance:** Avoid unnecessary encode/decode; serialize once at boundaries.
- **tradeoffs:** May require interface changes.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
