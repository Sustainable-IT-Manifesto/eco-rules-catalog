# ECO-CMP-PY-004 — Blocking I/O inside async context

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 2
- **Severity:** error
- **Tags:** python, async, latency
- **Legacy ID:** ECO-PY-004

## Summary

Blocking calls inside async functions reduce concurrency and inflate latency.

## Rationale

Blocking I/O defeats the purpose of async and can stall the entire event loop.

## Impact

```json
{
  "confidence": 0.9,
  "notes": "High propagation in async servers.",
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
  "guidance": "Use async-compatible libraries (e.g., async DB/HTTP clients).",
  "tradeoffs": "Library and code changes."
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
