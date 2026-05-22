# ECO-CMP-RS-001

**Name:** Unnecessary clone in hot paths

**Category:** Computation

**Family:** Rust

**Primary layer:** `code`

**System layers:** `code`

## Description

Calling clone() where borrowing, moving, or Copy semantics would avoid allocation and memory traffic.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `rust`
- **parser:** rust_ast_or_tree_sitter
- **notes:** Look for clone(), to_owned(), or collect() near loops, request paths, or large structures.

## Remediation

- **guidance:** Prefer borrowing, moving, Copy types, Arc sharing, or Cow where ownership boundaries require flexibility.
- **tradeoffs:** Borrowing may require lifetime or API changes; clarity should win over clever lifetime gymnastics.

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

### Unnecessary clone in hot paths

Calling clone() where borrowing, moving, or Copy semantics would avoid allocation and memory traffic.

## Remediation examples

### Reduce avoidable work

Prefer borrowing, moving, Copy types, Arc sharing, or Cow where ownership boundaries require flexibility.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Rust family](categories/cmp/families/rs/index.md)
- [Back to Rule Browser](../rule-browser.md)
