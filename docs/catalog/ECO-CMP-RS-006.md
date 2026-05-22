# ECO-CMP-RS-006

**Name:** Repeated regex compilation

**Category:** Computation

**Family:** Rust

**Primary layer:** `code`

**System layers:** `code`

## Description

Compiling regular expressions repeatedly instead of reusing compiled patterns.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `rust`
- **parser:** rust_ast_or_tree_sitter
- **notes:** Find Regex::new inside loops, handlers, parsers, or frequently called functions.

## Remediation

- **guidance:** Hoist regex construction into LazyLock, once_cell, lazy_static, or initialization code.
- **tradeoffs:** Dynamic patterns may require a bounded cache or explicit validation.

## Cost Dimensions

- **compute:** high
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

- CPU profiles
- allocation profiles
- request traces
- benchmark results

## Pattern examples

### Repeated regex compilation

Compiling regular expressions repeatedly instead of reusing compiled patterns.

## Remediation examples

### Reduce avoidable work

Hoist regex construction into LazyLock, once_cell, lazy_static, or initialization code.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Rust family](categories/cmp/families/rs/index.md)
- [Back to Rule Browser](../rule-browser.md)
