# ECO-NET-NET-007

**Name:** Excessive retry storms

**Category:** Networking

**Family:** Network

**Primary layer:** `network`

**System layers:** `network`

## Description

Aggressive retries amplify failures and increase waste.

## Impact

- **confidence:** 0.85
- **notes:** High propagation risk.
- **type:** reliability

## Detection

- **languages:** `infra`
- **method:** trace

## Remediation

- **guidance:** Use exponential backoff + jitter; add circuit breakers; cap retries.
- **tradeoffs:** May reduce immediate success rate during blips.

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
