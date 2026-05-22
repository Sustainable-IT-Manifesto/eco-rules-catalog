# ECO-AIM-AI-004

**Name:** No prompt caching

**Category:** AI/ML

**Family:** AI

**Primary layer:** `ai`

**System layers:** `ai`

## Description

Repeated prompts without caching waste tokens and compute.

## Impact

- **confidence:** 0.6
- **notes:** Strong for templated workflows.
- **type:** cost

## Detection

- **languages:** `org`, `infra`
- **method:** hybrid

## Remediation

- **guidance:** Cache deterministic responses with TTL and safe scoping.
- **tradeoffs:** Risk of staleness; privacy considerations.

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
