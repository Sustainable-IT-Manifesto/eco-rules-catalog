# ECO-CMP-PY-006 — Missing network timeout

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Network
- **Tier:** 2
- **Severity:** error
- **Tags:** python, network, timeouts
- **Legacy ID:** ECO-PY-006

## Summary

Network calls without explicit timeouts can hang and cascade failures.

## Rationale

Without timeouts, partial outages become thread exhaustion and retry storms.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "High propagation under dependency slowness.",
  "type": "reliability"
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
  "guidance": "Set explicit connect/read timeouts; prefer client defaults + overrides.",
  "tradeoffs": "Requires tuning per endpoint."
}
```

## Ontology

```json
{
  "system_layers": [
    "network"
  ]
}
```
