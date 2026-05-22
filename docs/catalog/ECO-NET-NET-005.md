# ECO-NET-NET-005

**Name:** Missing timeouts

**Category:** Networking

**Family:** Network

**Primary layer:** `network`

**System layers:** `network`

## Description

Missing timeouts remove a critical reliability boundary for network calls.

## Impact

- **confidence:** 0.85
- **notes:** High propagation during partial outages.
- **type:** reliability

## Detection

- **languages:** `python`, `javascript`, `java`, `infra`
- **method:** hybrid

## Remediation

- **guidance:** Set explicit connect/read timeouts; standardize defaults.
- **tradeoffs:** Endpoint tuning required.

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
