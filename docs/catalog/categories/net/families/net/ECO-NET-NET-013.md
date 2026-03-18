# ECO-NET-NET-013 — Excessive polling intervals

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 2
- **Severity:** warning
- **Tags:** polling
- **Legacy ID:** ECO-NET-013

## Summary

Frequent polling increases load even when nothing changes.

## Rationale

A million clients polling becomes a distributed denial-of-wallet.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Often large at scale.",
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
  "guidance": "Use push mechanisms; increase intervals; add caching and ETags.",
  "tradeoffs": "More event infrastructure."
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
