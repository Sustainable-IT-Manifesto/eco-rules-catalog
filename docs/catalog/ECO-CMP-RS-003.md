# ECO-CMP-RS-003

**Name:** Blocking work inside async tasks

**Category:** Computation

**Family:** Rust

**Primary layer:** `code`

**System layers:** `code`

## Description

Running blocking file, network, CPU, or sleep operations inside async executors without isolation.

## Impact

- **type:** cpu
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `rust`
- **parser:** rust_ast_or_tree_sitter
- **notes:** Look for std::thread::sleep, blocking I/O, heavy CPU loops, or sync clients inside async functions.

## Remediation

- **guidance:** Use spawn_blocking, async-aware clients, bounded worker pools, or separate CPU pipelines.
- **tradeoffs:** Offloading has scheduling overhead; reserve it for work that can actually block or monopolize executor threads.

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

### Blocking work inside async tasks

Running blocking file, network, CPU, or sleep operations inside async executors without isolation.

## Remediation examples

### Reduce avoidable work

Use spawn_blocking, async-aware clients, bounded worker pools, or separate CPU pipelines.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Rust family](categories/cmp/families/rs/index.md)
- [Back to Rule Browser](../rule-browser.md)
