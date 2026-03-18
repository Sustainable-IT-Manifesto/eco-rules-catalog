# ECO-NET-NET-010 — Large payloads without pagination

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 2
- **Severity:** warning
- **Tags:** pagination
- **Legacy ID:** ECO-NET-010

## Summary

Large unpaginated responses increase memory and bandwidth waste.

## Rationale

Huge responses create spikes and slow clients and servers.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Often hurts tail latency.",
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
  "guidance": "Introduce pagination, streaming, or filtering.",
  "tradeoffs": "API redesign effort."
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
