# ECO-ARC-ARCH-017 — Inefficient container image size

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 2
- **Severity:** note
- **Tags:** containers, images
- **Legacy ID:** ECO-ARCH-017

## Summary

Large images increase pull time and wasted storage/transfer.

## Rationale

Slim images reduce bandwidth and speed deploys.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Often quick win.",
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
  "guidance": "Use multi-stage builds and minimal base images.",
  "tradeoffs": "Build refactor."
}
```

## Ontology

```json
{
  "system_layers": [
    "architecture"
  ]
}
```
