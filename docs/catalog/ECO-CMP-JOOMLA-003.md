# ECO-CMP-JOOMLA-003

**Name:** Template loads unbundled duplicate assets

**Category:** Computation

**Family:** Joomla

**Primary layer:** `code`

**System layers:** `code`

## Description

A Joomla template or extension loads duplicate JavaScript/CSS assets across modules.

## Impact

- **type:** network
- **confidence:** 0.72
- **notes:** Impact increases on high-traffic routes, large datasets, frequently rendered pages, or repeated background work.

## Detection

- **method:** ast
- **languages:** `php`
- **parser:** php-ast

## Remediation

- **guidance:** Use Joomla asset management, deduplicate dependencies, bundle where appropriate, and load assets conditionally.
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

### Template loads unbundled duplicate assets

A Joomla template or extension loads duplicate JavaScript/CSS assets across modules.

## Remediation examples

### Reduce repeated work

Use Joomla asset management, deduplicate dependencies, bundle where appropriate, and load assets conditionally.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Joomla family](categories/cmp/families/joomla/index.md)
- [Back to Rule Browser](../rule-browser.md)
