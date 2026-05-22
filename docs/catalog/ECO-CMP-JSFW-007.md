# ECO-CMP-JSFW-007

**Name:** Duplicate data fetching across components

**Category:** Computation

**Family:** JavaScript Frameworks

**Primary layer:** `code`

**System layers:** `code`

## Description

Multiple components independently fetch the same data during a single page lifecycle.

## Impact

- **type:** network
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `javascript`, `typescript`
- **parser:** js-ast

## Remediation

- **guidance:** Centralize data fetching, deduplicate requests, use shared query caches, and prefetch intentionally.
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

### Duplicate data fetching across components

Multiple components independently fetch the same data during a single page lifecycle.

## Remediation examples

### Reduce repeated work

Centralize data fetching, deduplicate requests, use shared query caches, and prefetch intentionally.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to JavaScript Frameworks family](categories/cmp/families/jsfw/index.md)
- [Back to Rule Browser](../rule-browser.md)
