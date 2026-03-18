# ECO-ARC-ARCH-020 — Underutilized GPU/accelerator resources

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** gpu, ai
- **Legacy ID:** ECO-ARCH-020

## Summary

Accelerators running idle waste significant power and cost.

## Rationale

GPU idle burn is expensive; schedule and batch workloads.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "High in AI workloads.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Consolidate workloads; enable autoscaling; batch inference.",
  "tradeoffs": "Scheduling complexity."
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
