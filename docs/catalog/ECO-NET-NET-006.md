# ECO-NET-NET-006

**Name:** No connection reuse (keep-alive disabled)

**Category:** Networking

**Family:** Network

**Primary layer:** `network`

**System layers:** `network`

## Description

Disabling keep-alive increases handshake overhead and latency.

## Impact

- **confidence:** 0.7
- **notes:** Big in high QPS services.
- **type:** latency

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Enable keep-alive; tune pools and idle timeouts.
- **tradeoffs:** Requires proper pool sizing.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
