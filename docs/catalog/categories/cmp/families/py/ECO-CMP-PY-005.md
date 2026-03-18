# ECO-CMP-PY-005 — N+1 database query pattern

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** python, database, n+1
- **Legacy ID:** ECO-PY-005

## Summary

Queries executed inside iteration multiply round trips and load.

## Rationale

N+1 is a classic hidden multiplier for latency, cost, and carbon.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "Often severe at scale.",
  "type": "network"
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
  "guidance": "Use bulk queries, eager loading, or JOINs.",
  "tradeoffs": "May increase memory use; tune carefully."
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
