# ECO-CMP-PY-014

**Name:** Redundant environment variable lookups

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Repeated env lookups in hot code paths add overhead and noise.

## Impact

- **confidence:** 0.5
- **notes:** Small individually; measurable in hot loops.
- **type:** cpu

## Detection

- **languages:**
  - python
- **method:** ast

## Remediation

- **guidance:** Read env/config once during startup; pass config explicitly.
- **tradeoffs:** Slight architecture changes.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
