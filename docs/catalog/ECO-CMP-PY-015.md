# ECO-CMP-PY-015

**Name:** Recreating database connections per request

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Creating DB connections per request increases latency and resource churn.

## Impact

- **confidence:** 0.85
- **notes:** High propagation; often causes outages.
- **type:** latency

## Detection

- **languages:** `python`
- **method:** hybrid

## Remediation

- **guidance:** Use connection pooling and reuse sessions/clients.
- **tradeoffs:** Requires lifecycle management.

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
