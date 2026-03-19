# ECO-CMP-PY-006

**Name:** Missing network timeout

**Category:** CMP

**Family:** PY

**Primary layer:** `network`

**System layers:** `network`

## Description

Network calls without explicit timeouts can hang and cascade failures.

## Impact

- **confidence:** 0.85
- **notes:** High propagation under dependency slowness.
- **type:** reliability

## Detection

- **languages:**
  - python
- **method:** ast

## Remediation

- **guidance:** Set explicit connect/read timeouts; prefer client defaults + overrides.
- **tradeoffs:** Requires tuning per endpoint.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
