# ECO-CMP-PY-002 — Unbounded list growth

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** python, memory, streaming
- **Legacy ID:** ECO-PY-002

## Summary

Collections that grow without bounds increase memory pressure and GC churn.

## Rationale

Unbounded accumulation is a common cause of avoidable memory spikes and instability.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "Often shows up in ETL, batch jobs, API aggregation.",
  "type": "memory"
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
  "guidance": "Use generators, pagination, batching, or streaming APIs.",
  "tradeoffs": "May require refactoring call sites."
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
