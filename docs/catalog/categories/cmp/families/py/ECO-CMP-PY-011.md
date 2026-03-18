# ECO-CMP-PY-011 — Repeated JSON serialization cycles

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 1
- **Severity:** warning
- **Tags:** python, json, cpu
- **Legacy ID:** ECO-PY-011

## Summary

Serializing/deserializing repeatedly wastes CPU and increases latency.

## Rationale

Avoid churn converting structures when you can pass objects directly.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Often appears in middleware layers.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "python"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Avoid unnecessary encode/decode; serialize once at boundaries.",
  "tradeoffs": "May require interface changes."
}
```

## Ontology

```json
{
  "system_layers": [
    "code"
  ]
}
```
