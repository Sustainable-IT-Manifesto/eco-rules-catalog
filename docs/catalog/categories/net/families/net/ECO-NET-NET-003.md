# ECO-NET-NET-003 — Chatty microservice communication

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 2
- **Severity:** warning
- **Tags:** microservices, latency
- **Legacy ID:** ECO-NET-003

## Summary

Many small calls increase latency and cross-service overhead.

## Rationale

Chattiness multiplies overhead and failure points.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Common with naive service decomposition.",
  "type": "latency"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Aggregate requests, introduce caching, or redesign boundaries.",
  "tradeoffs": "May reduce separation or increase payload size."
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
