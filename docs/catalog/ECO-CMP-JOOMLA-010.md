# ECO-CMP-JOOMLA-010

**Name:** Synchronous third-party widgets on render

**Category:** Computation

**Family:** Joomla

**Primary layer:** `code`

**System layers:** `code`

## Description

Templates or extensions block page rendering on third-party scripts or API calls.

## Impact

- **type:** latency
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `php`
- **parser:** php-ast

## Remediation

- **guidance:** Defer noncritical widgets, cache server-side enrichment, and use async loading patterns.
- **tradeoffs:** Framework conventions, readability, caching correctness, and deployment topology should be considered before changing behavior.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** medium
- **storage:** low
- **human_time:** medium
- **carbon:** medium
- **water:** low

## Amplification

- **scales_with_users:** Yes
- **scales_with_data_volume:** No
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

### Synchronous third-party widgets on render

Templates or extensions block page rendering on third-party scripts or API calls.

## Remediation examples

### Reduce repeated work

Defer noncritical widgets, cache server-side enrichment, and use async loading patterns.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Joomla family](categories/cmp/families/joomla/index.md)
- [Back to Rule Browser](../rule-browser.md)
