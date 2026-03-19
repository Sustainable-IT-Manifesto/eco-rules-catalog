# ECO-CMP-PY-008

**Name:** Excessive logging in hot path

**Category:** CMP

**Family:** PY

**Primary layer:** `code`

**System layers:** `code`

## Description

Logging in tight loops or request hot paths adds CPU and I/O overhead.

## Impact

- **confidence:** 0.6
- **notes:** Worse with synchronous handlers.
- **type:** io

## Detection

- **languages:**
  - python
- **method:** ast

## Remediation

- **guidance:** Reduce log volume; guard debug logs; sample where appropriate.
- **tradeoffs:** Less granular logs unless sampled.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
