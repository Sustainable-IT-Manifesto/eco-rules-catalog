# ECO-NET-NET-006 — No connection reuse (keep-alive disabled)

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 2
- **Severity:** warning
- **Tags:** http, keep-alive
- **Legacy ID:** ECO-NET-006

## Summary

Disabling keep-alive increases handshake overhead and latency.

## Rationale

Connection reuse reduces repeated TLS and TCP setup.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Big in high QPS services.",
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
  "guidance": "Enable keep-alive; tune pools and idle timeouts.",
  "tradeoffs": "Requires proper pool sizing."
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
