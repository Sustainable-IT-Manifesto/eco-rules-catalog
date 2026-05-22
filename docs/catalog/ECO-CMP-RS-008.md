# ECO-CMP-RS-008

**Name:** Inefficient string construction

**Category:** Computation

**Family:** Rust

**Primary layer:** `code`

**System layers:** `code`

## Description

Repeated format! or push_str patterns that allocate avoidably while building large strings.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `rust`
- **parser:** rust_ast_or_tree_sitter
- **notes:** Look for repeated format! in loops or string building without capacity planning.

## Remediation

- **guidance:** Use String::with_capacity, write!, buffered writers, or streaming serialization.
- **tradeoffs:** Capacity estimates can be wrong; avoid over-optimizing small strings.

## Cost Dimensions

- **compute:** medium
- **memory:** high
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

- CPU profiles
- allocation profiles
- request traces
- benchmark results

## Pattern examples

### Inefficient string construction

Repeated format! or push_str patterns that allocate avoidably while building large strings.

## Remediation examples

### Reduce avoidable work

Use String::with_capacity, write!, buffered writers, or streaming serialization.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Rust family](categories/cmp/families/rs/index.md)
- [Back to Rule Browser](../rule-browser.md)
