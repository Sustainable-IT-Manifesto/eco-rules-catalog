# ECO-NET-NET-006

**Name:** No connection reuse (keep-alive disabled)

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Disabling keep-alive increases handshake overhead and latency.

## Impact

- **confidence:** 0.7
- **notes:** Big in high QPS services.
- **type:** latency

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Enable keep-alive; tune pools and idle timeouts.
- **tradeoffs:** Requires proper pool sizing.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
