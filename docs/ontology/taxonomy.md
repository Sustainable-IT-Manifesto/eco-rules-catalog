# Canonical vocabulary

This document defines the canonical controlled vocabulary used by the Eco Rules Catalog.

The machine-readable source of truth is:

- `catalog/registry.json`

## System layers

- ai
- architecture
- code
- data
- network
- process


# Categories

## Infrastructure (INF)

The INF category captures inefficiencies in the execution environment of software systems.

### Families

- DOCKER — container image construction and layering
- COMPOSE — multi-service local orchestration
- K8S — Kubernetes manifests, scheduling, scaling

### Examples

- oversized base images
- missing resource limits
- unnecessary sidecars
- unbounded scaling behavior
