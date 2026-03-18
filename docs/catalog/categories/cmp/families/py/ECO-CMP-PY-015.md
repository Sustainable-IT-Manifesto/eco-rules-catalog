# ECO-CMP-PY-015 — Recreating database connections per request

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 2
- **Severity:** error
- **Tags:** python, database, connections
- **Legacy ID:** ECO-PY-015

## Summary

Creating DB connections per request increases latency and resource churn.

## Rationale

Connection setup is expensive and can overwhelm DB under load.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "High propagation; often causes outages.",
  "type": "latency"
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
  "guidance": "Use connection pooling and reuse sessions/clients.",
  "tradeoffs": "Requires lifecycle management."
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
