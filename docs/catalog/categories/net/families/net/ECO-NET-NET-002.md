# ECO-NET-NET-002 — No gzip/brotli compression

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 2
- **Severity:** warning
- **Tags:** http, compression
- **Legacy ID:** ECO-NET-002

## Summary

Serving text assets without compression increases bandwidth and energy use.

## Rationale

Compression is one of the simplest ways to reduce bytes transferred.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "High win for JSON/HTML/CSS/JS.",
  "type": "network"
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
  "guidance": "Enable gzip/brotli at CDN/load balancer/origin.",
  "tradeoffs": "Minimal; watch CPU on origin if no CDN."
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
