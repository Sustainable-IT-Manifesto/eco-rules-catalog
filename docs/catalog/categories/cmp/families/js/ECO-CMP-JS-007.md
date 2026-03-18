# ECO-CMP-JS-007 — Missing HTTP caching headers (client-side)

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Network
- **Tier:** 2
- **Severity:** warning
- **Tags:** javascript, caching
- **Legacy ID:** ECO-JS-007

## Summary

Missing cache headers causes repeated downloads and wasted bandwidth.

## Rationale

Caching prevents repeated work; missing caching forces it.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "High on static assets.",
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
  "guidance": "Set Cache-Control/ETag; use immutable assets with hashes.",
  "tradeoffs": "Requires proper build pipeline."
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
