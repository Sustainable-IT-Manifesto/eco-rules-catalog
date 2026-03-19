# ECO-NET-NET-007

**Name:** Excessive retry storms

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Aggressive retries amplify failures and increase waste.

## Impact

- **confidence:** 0.85
- **notes:** High propagation risk.
- **type:** reliability

## Detection

- **languages:**
  - infra
- **method:** trace

## Remediation

- **guidance:** Use exponential backoff + jitter; add circuit breakers; cap retries.
- **tradeoffs:** May reduce immediate success rate during blips.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
