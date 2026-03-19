# ECO-NET-NET-015

**Name:** Missing circuit breaker patterns

**Category:** NET

**Family:** NET

**Primary layer:** `network`

**System layers:** `network`

## Description

Without circuit breakers, failures propagate and waste resources.

## Impact

- **confidence:** 0.75
- **notes:** High in distributed systems.
- **type:** reliability

## Detection

- **languages:**
  - infra
  - org
- **method:** config

## Remediation

- **guidance:** Implement circuit breakers; define fallbacks and budgets.
- **tradeoffs:** Requires clear SLO thinking.

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Rule Browser](../rule-browser.md)
