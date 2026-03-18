# ECO-ARC-ARCH-019 — Overly aggressive autoscaling thresholds

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** note
- **Tags:** autoscaling
- **Legacy ID:** ECO-ARCH-019

## Summary

Aggressive scaling can cause thrash and wasted churn.

## Rationale

Thrash wastes compute and destabilizes latency.

## Impact

```json
{
  "confidence": 0.5,
  "notes": "Needs measurement.",
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
  "guidance": "Add stabilization windows and sane thresholds.",
  "tradeoffs": "Slower response to spikes."
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
