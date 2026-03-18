# ECO-CMP-PY-016 — No connection pooling

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Architecture
- **Tier:** 2
- **Severity:** warning
- **Tags:** python, db, pooling
- **Legacy ID:** ECO-PY-016

## Summary

Lack of pooling increases connection churn, latency, and DB load.

## Rationale

Pooling stabilizes performance and reduces wasted setup cost.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "Especially important in serverless/short-lived contexts.",
  "type": "latency"
}
```

## Detection

```json
{
  "languages": [
    "python"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Enable and tune pooling; set max connections.",
  "tradeoffs": "Tuning required to avoid saturation."
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
