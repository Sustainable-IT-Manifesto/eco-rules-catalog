# ECO-NET-NET-009

**Name:** Under-fetching causing follow-up calls

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Responses missing needed data cause extra round trips.

## Impact

- **confidence:** 0.55
- **notes:** Context-dependent.
- **type:** network

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Batch endpoints; design responses around common usage.
- **tradeoffs:** Bigger payloads in some cases.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
