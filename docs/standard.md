# Eco Rules Catalog Standard

The Eco Rules Catalog defines a shared language for software inefficiency.

## Key Concepts

- Canonical rule format
- Registry-driven values
- Validated IDs
- Generated catalog

## ID Format

ECO-{CATEGORY_CODE}-{FAMILY_CODE}-{SEQUENCE}

## Layers

- ai
- architecture
- code
- data
- network
- process

## Source of Truth

- catalog/rules/
- registry.json

catalog/master.json is generated.

## Categories vs Layers

The catalog separates **what kind of problem** from **where it appears**.

### Categories (what)

Categories describe the type of inefficiency:

- AIM — AI / ML
- CMP — Computation
- DAT — Data
- NET — Networking
- ORG — Organizational
- INF — Infrastructure

### Layers (where)

Layers describe where the inefficiency occurs:

- ai
- architecture
- code
- data
- network
- process

A rule belongs to:
- one **category**
- one **family**
- one or more **layers**

> Infrastructure is a category, not a layer.

Because waste is a bug.
