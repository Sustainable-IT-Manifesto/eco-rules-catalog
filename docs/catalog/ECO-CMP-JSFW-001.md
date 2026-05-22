# ECO-CMP-JSFW-001

**Name:** Component re-renders caused by unstable props

**Category:** Computation

**Family:** JavaScript Frameworks

**Primary layer:** `code`

**System layers:** `code`

## Description

React, Vue, or similar components re-render frequently because props, callbacks, or objects are recreated on every render.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `javascript`, `typescript`
- **parser:** js-ast

## Remediation

- **guidance:** Stabilize props where useful, split components, memoize carefully, and measure with framework profiling tools.
- **tradeoffs:** Framework conventions, readability, caching correctness, and deployment topology should be considered before changing behavior.

## Cost Dimensions

- **compute:** medium
- **memory:** medium
- **network:** low
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

### Component re-renders caused by unstable props

React, Vue, or similar components re-render frequently because props, callbacks, or objects are recreated on every render.

## Remediation examples

### Reduce repeated work

Stabilize props where useful, split components, memoize carefully, and measure with framework profiling tools.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to JavaScript Frameworks family](categories/cmp/families/jsfw/index.md)
- [Back to Rule Browser](../rule-browser.md)
