# ECO-CMP-PY-009

**Name:** Repeated regex compilation

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Compiling regex repeatedly wastes CPU; compile once and reuse.

## Impact

- **confidence:** 0.65
- **notes:** Common in parsing pipelines.
- **type:** cpu

## Detection

- **languages:** `python`
- **method:** ast

## Remediation

- **guidance:** Precompile regex at module init or reuse compiled patterns.
- **tradeoffs:** Minimal.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
