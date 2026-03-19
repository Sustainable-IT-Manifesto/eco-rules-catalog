# ECO-CMP-PY-005

**Name:** N+1 database query pattern

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Queries executed inside iteration multiply round trips and load.

## Impact

- **confidence:** 0.8
- **notes:** Often severe at scale.
- **type:** network

## Detection

- **languages:**
  - python
- **method:** hybrid

## Remediation

- **guidance:** Use bulk queries, eager loading, or JOINs.
- **tradeoffs:** May increase memory use; tune carefully.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
