# ECO-NET-NET-012 — No HTTP/2 or HTTP/3 where applicable

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 2
- **Severity:** note
- **Tags:** http2, http3
- **Legacy ID:** ECO-NET-012

## Summary

Older HTTP versions may reduce efficiency for multiplexed workloads.

## Rationale

Multiplexing and improved transport can reduce overhead and latency.

## Impact

```json
{
  "confidence": 0.5,
  "notes": "Depends on traffic patterns and client support.",
  "type": "latency"
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
  "guidance": "Enable HTTP/2+ on TLS endpoints; evaluate HTTP/3 at edge.",
  "tradeoffs": "Operational complexity."
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
