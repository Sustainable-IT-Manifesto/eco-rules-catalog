# ECO-CMP-JSFW-010

**Name:** Expensive computed selectors run every render

**Category:** Computation

**Family:** JavaScript Frameworks

**Primary layer:** `code`

**System layers:** `code`

## Description

Framework selectors, computed values, or pipes recompute expensive transformations unnecessarily.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `javascript`, `typescript`
- **parser:** js-ast

## Remediation

- **guidance:** Memoize bounded computations, precompute server-side when appropriate, and avoid heavy work in render paths.
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

### Expensive computed selectors run every render

Framework selectors, computed values, or pipes recompute expensive transformations unnecessarily.

## Remediation examples

### Reduce repeated work

Memoize bounded computations, precompute server-side when appropriate, and avoid heavy work in render paths.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to JavaScript Frameworks family](categories/cmp/families/jsfw/index.md)
- [Back to Rule Browser](../rule-browser.md)
