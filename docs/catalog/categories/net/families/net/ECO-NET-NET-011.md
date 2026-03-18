# ECO-NET-NET-011 — No CDN usage for static content

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 3
- **Severity:** warning
- **Tags:** cdn, latency
- **Legacy ID:** ECO-NET-011

## Summary

Serving static content from origin increases latency and origin load.

## Rationale

CDNs reduce transfer distance and offload repeated work from origin.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "High for global audiences.",
  "type": "network"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Use a CDN for static assets and cacheable endpoints.",
  "tradeoffs": "Operational overhead and caching discipline."
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
