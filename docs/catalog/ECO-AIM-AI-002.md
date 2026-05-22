# ECO-AIM-AI-002

**Name:** No inference batching

**Category:** AI/ML

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

No batching increases per-request overhead and lowers throughput.

## Impact

- **confidence:** 0.7
- **notes:** Often significant for GPU inference.
- **type:** cpu

## Detection

- **languages:** `python`, `infra`
- **method:** trace

## Remediation

- **guidance:** Introduce batching at gateway/inference server.
- **tradeoffs:** Added latency for low volume; needs tuning.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
