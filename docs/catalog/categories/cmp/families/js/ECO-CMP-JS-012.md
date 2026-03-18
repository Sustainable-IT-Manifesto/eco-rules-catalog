# ECO-CMP-JS-012 — Redundant API calls in component lifecycle

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Network
- **Tier:** 2
- **Severity:** warning
- **Tags:** javascript, frontend, network
- **Legacy ID:** ECO-JS-012

## Summary

Repeated fetches on rerender waste network and CPU.

## Rationale

Chattiness often comes from accidental rerenders and missing caching.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Common in SPAs.",
  "type": "network"
}
```

## Detection

```json
{
  "languages": [
    "javascript"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Cache results; dedupe requests; stabilize dependencies.",
  "tradeoffs": "State management changes."
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
