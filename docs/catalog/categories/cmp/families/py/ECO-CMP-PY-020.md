# ECO-CMP-PY-020 — Synchronous subprocess invocation in hot path

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** python, subprocess, latency
- **Legacy ID:** ECO-PY-020

## Summary

Blocking subprocess calls increase latency and consume resources.

## Rationale

External process calls are expensive and unpredictable under load.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "High variance; often spikes p99.",
  "type": "latency"
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
  "guidance": "Avoid subprocess in request paths; cache results or move to background jobs.",
  "tradeoffs": "Added system complexity."
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
