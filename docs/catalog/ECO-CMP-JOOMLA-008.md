# ECO-CMP-JOOMLA-008

**Name:** Verbose payload logging in extensions

**Category:** Computation

**Family:** Joomla

**Primary layer:** `code`

**System layers:** `code`

## Description

Joomla extensions log request bodies, query results, or debug details in production.

## Impact

- **type:** storage
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `php`
- **parser:** php-ast

## Remediation

- **guidance:** Gate debug logging, redact payloads, sample noisy events, and apply retention policies.
- **tradeoffs:** Framework conventions, readability, caching correctness, and deployment topology should be considered before changing behavior.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** low
- **storage:** medium
- **human_time:** medium
- **carbon:** medium
- **water:** low

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** Yes
- **scales_non_linearly:** No

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- request traces
- CPU profiles
- allocation profiles
- APM transaction timing

## Pattern examples

### Verbose payload logging in extensions

Joomla extensions log request bodies, query results, or debug details in production.

## Remediation examples

### Reduce repeated work

Gate debug logging, redact payloads, sample noisy events, and apply retention policies.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Joomla family](categories/cmp/families/joomla/index.md)
- [Back to Rule Browser](../rule-browser.md)
