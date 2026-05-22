# ECO-CMP-JSFW-002

**Name:** Large client bundle from unused dependencies

**Category:** Computation

**Family:** JavaScript Frameworks

**Primary layer:** `code`

**System layers:** `code`

## Description

A JavaScript framework app ships large dependencies or unused code to most users.

## Impact

- **type:** network
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `javascript`, `typescript`
- **parser:** js-ast

## Remediation

- **guidance:** Analyze bundles, tree-shake, code-split, remove unused dependencies, and lazy-load route-specific code.
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

### Large client bundle from unused dependencies

A JavaScript framework app ships large dependencies or unused code to most users.

## Remediation examples

### Reduce repeated work

Analyze bundles, tree-shake, code-split, remove unused dependencies, and lazy-load route-specific code.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to JavaScript Frameworks family](categories/cmp/families/jsfw/index.md)
- [Back to Rule Browser](../rule-browser.md)
