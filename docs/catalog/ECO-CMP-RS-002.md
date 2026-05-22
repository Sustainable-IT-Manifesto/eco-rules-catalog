# ECO-CMP-RS-002

**Name:** Collecting iterators before immediate iteration

**Category:** Computation

**Family:** Rust

**Primary layer:** `code`

**System layers:** `code`

## Description

Using collect() to materialize an intermediate Vec when the iterator could be consumed lazily.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `rust`
- **parser:** rust_ast_or_tree_sitter
- **notes:** Detect collect() followed by immediate iteration, map, filter, count, or fold.

## Remediation

- **guidance:** Keep operations lazy with iterator chains, fold, for_each, or streaming adapters.
- **tradeoffs:** Materialization can be appropriate when reuse, sorting, indexing, or ownership isolation is required.

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

### Collecting iterators before immediate iteration

Using collect() to materialize an intermediate Vec when the iterator could be consumed lazily.

## Remediation examples

### Reduce avoidable work

Keep operations lazy with iterator chains, fold, for_each, or streaming adapters.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Rust family](categories/cmp/families/rs/index.md)
- [Back to Rule Browser](../rule-browser.md)
