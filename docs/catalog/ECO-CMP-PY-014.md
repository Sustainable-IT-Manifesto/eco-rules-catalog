# ECO-CMP-PY-014

**Name:** Redundant environment variable lookups

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Repeated env lookups in hot code paths add overhead and noise.

## Impact

- **confidence:** 0.5
- **notes:** Small individually; measurable in hot loops.
- **type:** cpu

## Detection

- **languages:** `python`
- **method:** ast

## Remediation

- **guidance:** Read env/config once during startup; pass config explicitly.
- **tradeoffs:** Slight architecture changes.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Python family](categories/cmp/families/py/index.md)
- [Back to Rule Browser](../rule-browser.md)
