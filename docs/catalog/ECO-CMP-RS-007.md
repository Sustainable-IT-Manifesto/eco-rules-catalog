# ECO-CMP-RS-007

**Name:** Large debug formatting in production paths

**Category:** Computation

**Family:** Rust

**Primary layer:** `code`

**System layers:** `code`

## Description

Using debug formatting or broad tracing of large structures in hot paths.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `rust`
- **parser:** rust_ast_or_tree_sitter
- **notes:** Detect format!, dbg!, tracing fields, or debug logs involving large collections or payloads.

## Remediation

- **guidance:** Use structured, sampled, bounded logs and avoid full payload formatting in routine paths.
- **tradeoffs:** Diagnostics still matter; preserve targeted details for failure investigation.

## Cost Dimensions

- **compute:** medium
- **memory:** high
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

- CPU profiles
- allocation profiles
- request traces
- benchmark results

## Pattern examples

### Large debug formatting in production paths

Using debug formatting or broad tracing of large structures in hot paths.

## Remediation examples

### Reduce avoidable work

Use structured, sampled, bounded logs and avoid full payload formatting in routine paths.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Rust family](categories/cmp/families/rs/index.md)
- [Back to Rule Browser](../rule-browser.md)
