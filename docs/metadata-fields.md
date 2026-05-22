# Eco Rules Catalog Metadata Fields

Version 0.4.0 formalizes optional systems-level metadata for richer sustainability, operational, and architectural analysis.

## `cost_dimensions`

Qualitative impact estimates across major cost and sustainability dimensions.

Allowed values: `none`, `low`, `medium`, `high`, `unknown`.

Supported keys:

- `compute`
- `memory`
- `network`
- `storage`
- `human_time`
- `carbon`
- `water`

Example:

```json
{
  "compute": "high",
  "memory": "medium",
  "network": "low",
  "storage": "low",
  "human_time": "medium",
  "carbon": "high",
  "water": "medium"
}
```

## `amplification`

Describes how a finding may grow as the system scales.

Supported keys:

- `scales_with_users`
- `scales_with_data_volume`
- `scales_non_linearly`

## `temporal_behavior`

Describes when the inefficiency appears or worsens.

Supported keys:

- `startup_only`
- `steady_state`
- `burst_sensitive`
- `time_degradation`

## `runtime_evidence`

A list of operational evidence sources useful for confirmation or prioritization. Examples include:

- cloud billing data
- CPU profiles
- memory snapshots
- database query plans
- distributed traces
- queue depth metrics
- carbon intensity data
- water stress data

## `sustainability_priority`

Optional reporting and prioritization dimensions.

Allowed values: `none`, `low`, `medium`, `high`, `unknown`.

Supported keys:

- `operational_cost`
- `carbon`
- `water`
- `developer_productivity`
- `reliability`
- `customer_impact`
- `scaling_risk`

## Compatibility

These fields are optional. Existing rules remain valid. The catalog still allows additional properties so experimental fields can mature before being formally adopted.
