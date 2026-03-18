# ECO-CMP-JS-005 — Blocking crypto in event loop

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** javascript, crypto, latency
- **Legacy ID:** ECO-JS-005

## Summary

CPU-heavy crypto blocks the event loop and inflates latency.

## Rationale

Event loop stalls propagate to all concurrent requests.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Use workers for heavy CPU work.",
  "type": "latency"
}
```

## Detection

```json
{
  "languages": [
    "javascript"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Move CPU-heavy crypto to worker threads or native async APIs.",
  "tradeoffs": "Complexity increase."
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
