# ECO-CMP-JAVA-005

**Name:** N+1 ORM query pattern

**Category:** CMP

**Family:** JAVA

**Primary layer:** `code`

**System layers:** `code`

## Description

ORM queries inside loops multiply DB calls.

## Impact

- **confidence:** 0.8
- **notes:** Often severe at scale.
- **type:** network

## Detection

- **languages:**
  - java
- **method:** hybrid

## Remediation

- **guidance:** Use eager fetching, joins, or batch queries.
- **tradeoffs:** Tune memory and query plans.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
