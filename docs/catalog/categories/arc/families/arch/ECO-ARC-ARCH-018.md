# ECO-ARC-ARCH-018 — No cold-start optimization

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 2
- **Severity:** note
- **Tags:** cold-start
- **Legacy ID:** ECO-ARCH-018

## Summary

Cold starts inflate latency and may force overprovisioning.

## Rationale

Poor cold starts often lead teams to keep things always-on.

## Impact

```json
{
  "confidence": 0.5,
  "notes": "Depends on platform.",
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
  "guidance": "Reduce init work; warm pools selectively; cache dependencies.",
  "tradeoffs": "More tuning."
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
