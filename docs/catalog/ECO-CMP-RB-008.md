# ECO-CMP-RB-008

**Name:** Excessive object allocation in hot paths

**Category:** Computation

**Family:** Ruby

**Primary layer:** `code`

**System layers:** `code`

## Description

Allocating short-lived hashes, arrays, strings, or objects in tight loops increases GC pressure.

## Impact

- **type:** memory
- **confidence:** 0.75
- **notes:** Impact increases in hot paths, large collections, high-traffic Rails actions, background jobs, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `ruby`
- **parser:** ruby_parser_or_prism

## Remediation

- **guidance:** Reuse immutable constants, reduce temporary object creation, prefer streaming transformations, and profile before micro-optimizing.
- **tradeoffs:** May require refactoring for readability, query shape, or framework conventions.

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
- **scales_with_data_volume:** Yes
- **scales_non_linearly:** No

## Temporal Behavior

- **startup_only:** No
- **steady_state:** Yes
- **burst_sensitive:** Yes
- **time_degradation:** No

## Runtime Evidence

- allocation profiles
- GC time
- ObjectSpace counts
- flamegraphs

## Pattern examples

No pattern examples provided.

## Remediation examples

No remediation examples provided.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Ruby family](categories/cmp/families/rb/index.md)
- [Back to Rule Browser](../rule-browser.md)
