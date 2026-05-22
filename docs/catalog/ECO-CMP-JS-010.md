# ECO-CMP-JS-010

**Name:** Missing request timeout

**Category:** Computation

**Family:** JavaScript

**Primary layer:** `network`

**System layers:** `network`

## Description

Requests without timeouts hang and create cascading latency.

## Impact

- **confidence:** 0.85
- **notes:** High propagation risk.
- **type:** reliability

## Detection

- **languages:** `javascript`
- **method:** hybrid

## Remediation

- **guidance:** Use AbortController / client timeouts; set defaults.
- **tradeoffs:** Endpoint tuning.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to JavaScript family](categories/cmp/families/js/index.md)
- [Back to Rule Browser](../rule-browser.md)
