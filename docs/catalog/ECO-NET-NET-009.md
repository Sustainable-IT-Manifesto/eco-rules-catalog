# ECO-NET-NET-009

**Name:** Under-fetching causing follow-up calls

**Category:** Networking

**Family:** Network

**Primary layer:** `network`

**System layers:** `network`

## Description

Responses missing needed data cause extra round trips.

## Impact

- **confidence:** 0.55
- **notes:** Context-dependent.
- **type:** network

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Batch endpoints; design responses around common usage.
- **tradeoffs:** Bigger payloads in some cases.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Networking category](categories/net/index.md)
- [Back to Network family](categories/net/families/net/index.md)
- [Back to Rule Browser](../rule-browser.md)
