# ECO-NET-NET-004

**Name:** Redundant authentication calls

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Repeated auth calls waste CPU and network and add latency.

## Impact

- **confidence:** 0.6
- **notes:** High when per-request introspection is used.
- **type:** latency

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Cache tokens/keys; prefer local validation when safe.
- **tradeoffs:** Must respect revocation semantics.

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
