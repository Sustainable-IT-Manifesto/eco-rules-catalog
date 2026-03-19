# ECO-AIM-AI-004

**Name:** No prompt caching

**Category:** AIM

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

- **languages:**
  - org
  - infra
- **method:** hybrid

## Remediation

- **guidance:** Cache deterministic responses with TTL and safe scoping.
- **tradeoffs:** Risk of staleness; privacy considerations.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
