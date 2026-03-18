# ECO-NET-NET-004 — Redundant authentication calls

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 2
- **Severity:** note
- **Tags:** auth, caching
- **Legacy ID:** ECO-NET-004

## Summary

Repeated auth calls waste CPU and network and add latency.

## Rationale

Token validation and introspection can become a hidden multiplier.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "High when per-request introspection is used.",
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
  "guidance": "Cache tokens/keys; prefer local validation when safe.",
  "tradeoffs": "Must respect revocation semantics."
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
