# ECO-ARC-ARCH-005 — No resource limits in containers

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** kubernetes, limits
- **Legacy ID:** ECO-ARCH-005

## Summary

Missing CPU/memory limits causes noisy-neighbor waste and instability.

## Rationale

Limits are a boundary; without them, one workload can consume the cluster.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Also drives over-provisioning for safety.",
  "type": "reliability"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Set requests/limits; right-size with metrics.",
  "tradeoffs": "Requires tuning to avoid throttling."
}
```

## Ontology

```json
{
  "system_layers": [
    "architecture"
  ]
}
```
