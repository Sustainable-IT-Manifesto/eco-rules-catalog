# ECO-CMP-JS-013 — Uncompressed static assets

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Network
- **Tier:** 2
- **Severity:** warning
- **Tags:** javascript, assets, compression
- **Legacy ID:** ECO-JS-013

## Summary

Serving assets without compression increases bandwidth and energy use.

## Rationale

Compression is one of the simplest bandwidth reductions.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "Big win for text assets.",
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
  "guidance": "Enable gzip/brotli; ensure proper caching.",
  "tradeoffs": "Server/CDN config changes."
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
