# ECO-NET-NET-001 — Missing HTTP caching headers

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 2
- **Severity:** warning
- **Tags:** http, caching
- **Legacy ID:** ECO-NET-001

## Summary

Missing cache headers causes repeated downloads and wasted work.

## Rationale

Caching prevents repeated network transfer and repeated compute.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Large impact for static and semi-static responses.",
  "type": "network"
}
```

## Detection

```json
{
  "languages": [
    "infra",
    "org"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Add Cache-Control/ETag; use immutable asset hashing where possible.",
  "tradeoffs": "Requires cache invalidation discipline."
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
