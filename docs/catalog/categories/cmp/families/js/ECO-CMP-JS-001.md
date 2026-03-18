# ECO-CMP-JS-001 — Synchronous filesystem calls in request path

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Code
- **Tier:** 2
- **Severity:** error
- **Tags:** javascript, node, blocking
- **Legacy ID:** ECO-JS-001

## Summary

Sync FS calls block the event loop and reduce concurrency.

## Rationale

One blocking FS call can stall all concurrent requests in the same process.

## Impact

```json
{
  "confidence": 0.9,
  "notes": "High propagation in Node services.",
  "type": "latency"
}
```

## Detection

```json
{
  "languages": [
    "javascript"
  ],
  "method": "ast"
}
```

## Remediation

```json
{
  "guidance": "Use async fs APIs (promises/callbacks).",
  "tradeoffs": "Refactor required."
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
