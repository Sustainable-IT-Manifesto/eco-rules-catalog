# ECO-CMP-PY-019

**Name:** Excessive thread spawning

**Category:** Computation

**Family:** Python

**Primary layer:** `code`

**System layers:** `code`

## Description

Creating many threads increases overhead and contention.

## Impact

- **confidence:** 0.65
- **notes:** Often misused for I/O that could be async.
- **type:** cpu

## Detection

- **languages:** `python`
- **method:** hybrid

## Remediation

- **guidance:** Use thread pools, async I/O, or bounded concurrency.
- **tradeoffs:** Requires concurrency redesign.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
