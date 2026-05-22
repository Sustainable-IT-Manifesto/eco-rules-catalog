# ECO-AIM-AI-006

**Name:** Unbounded context window usage

**Category:** AI/ML

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Excessive context increases token cost and latency.

## Impact

- **confidence:** 0.75
- **notes:** Often the biggest controllable factor.
- **type:** cost

## Detection

- **languages:** `org`, `infra`
- **method:** trace

## Remediation

- **guidance:** Summarize, retrieve selectively, and cap context intentionally.
- **tradeoffs:** Requires prompt/pipeline design.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to AI/ML category](categories/aim/index.md)
- [Back to AI family](categories/aim/families/ai/index.md)
- [Back to Rule Browser](../rule-browser.md)
