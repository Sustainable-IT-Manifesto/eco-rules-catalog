# ECO-CMP-PY-008 — Excessive logging in hot path

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 1
- **Severity:** note
- **Tags:** python, logging, io
- **Legacy ID:** ECO-PY-008

## Summary

Logging in tight loops or request hot paths adds CPU and I/O overhead.

## Rationale

Hot-path logging is a quiet tax on throughput and latency.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Worse with synchronous handlers.",
  "type": "io"
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
  "guidance": "Reduce log volume; guard debug logs; sample where appropriate.",
  "tradeoffs": "Less granular logs unless sampled."
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
