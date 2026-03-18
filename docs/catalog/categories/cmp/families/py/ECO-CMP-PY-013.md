# ECO-CMP-PY-013 — Inefficient pandas row iteration

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 1
- **Severity:** warning
- **Tags:** python, pandas, cpu
- **Legacy ID:** ECO-PY-013

## Summary

Row-wise pandas iteration is slow compared to vectorized operations.

## Rationale

Vectorization reduces Python-level overhead dramatically.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "High in analytics/ETL.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "python"
  ],
  "method": "ast"
}
```

## Remediation

```json
{
  "guidance": "Use vectorized ops or apply carefully; avoid iterrows in hot paths.",
  "tradeoffs": "Learning curve / refactor time."
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
