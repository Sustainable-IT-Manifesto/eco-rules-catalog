# ECO-CMP-RS-004

**Name:** Unbounded channel growth

**Category:** Computation

**Family:** Rust

**Primary layer:** `code`

**System layers:** `code`

## Description

Using unbounded channels where producer speed can exceed consumer capacity.

## Impact

- **type:** memory
- **confidence:** 0.72
- **notes:** Impact increases in hot paths, large inputs, high-concurrency services, build pipelines, or repeated request paths.

## Detection

- **method:** ast
- **languages:** `rust`
- **parser:** rust_ast_or_tree_sitter
- **notes:** Detect unbounded_channel or unbounded MPSC patterns in service paths.

## Remediation

- **guidance:** Use bounded channels, explicit backpressure, dropping policies, or admission control.
- **tradeoffs:** Bounded queues force product decisions about loss, latency, or rejection behavior.

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

### Unbounded channel growth

Using unbounded channels where producer speed can exceed consumer capacity.

## Remediation examples

### Reduce avoidable work

Use bounded channels, explicit backpressure, dropping policies, or admission control.

## Metadata

- **catalog_version:** 0.4.0

## Navigation

- [Back to Human Catalog](index.md)
- [Back to Computation category](categories/cmp/index.md)
- [Back to Rust family](categories/cmp/families/rs/index.md)
- [Back to Rule Browser](../rule-browser.md)
