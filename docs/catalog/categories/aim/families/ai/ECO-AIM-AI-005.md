# ECO-AIM-AI-005 — Always-on inference endpoints

- **Category:** AI/ML (AIM)
- **Family:** AI (AI)
- **Layer:** AI
- **Tier:** 3
- **Severity:** warning
- **Tags:** ai, scale-to-zero
- **Legacy ID:** ECO-AI-005

## Summary

Always-on endpoints waste baseline compute when idle.

## Rationale

Idle accelerators still burn power; scale needs boundaries.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "High for GPU-backed endpoints.",
  "type": "carbon"
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
  "guidance": "Autoscale; scale-to-zero where feasible; consolidate endpoints.",
  "tradeoffs": "Cold starts and scheduling complexity."
}
```

## Ontology

```json
{
  "system_layers": [
    "ai"
  ]
}
```
