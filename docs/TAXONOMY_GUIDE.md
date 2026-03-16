# Eco Rules Catalog — Taxonomy Guide

This document explains how rules are organized within the catalog.

The catalog taxonomy provides a structured way to reason about
software inefficiency patterns.

The taxonomy hierarchy is:

Category → Family → Rule
````

---

## Categories

Categories represent **major domains of inefficiency**.

Examples:

| Category       | Code | Description                             |
| -------------- | ---- | --------------------------------------- |
| Computation    | CMP  | inefficient algorithms and CPU usage    |
| Data           | DAT  | inefficient data structures and queries |
| Networking     | NET  | inefficient communication patterns      |
| Infrastructure | INF  | inefficient infrastructure usage        |
| AI/ML          | AIM  | inefficient AI model usage              |
| Organizational | ORG  | governance and process inefficiencies   |

Categories should remain **stable and few in number**.

Adding a category requires strong justification.

---

## Families

Families group related inefficiency patterns.

Example:

```
Category: Computation

Families:
   Python
   JavaScript
   Java
   Algorithms
```

Example:

```
Category: Infrastructure

Families:
   Kubernetes
   Containers
   Cloud
```

Families are expected to evolve more frequently than categories.

---

## Rules

Rules describe **specific inefficiency patterns**.

Example:

```
Category: Computation
Family: Python

Rule:
ECO-CMP-PY-010
Repeated string concatenation in loops
```

Rules should be:

* precise
* actionable
* detectable

---

## Naming Principles

Taxonomy elements should be:

* clear
* concise
* broadly understandable
* stable over time

Avoid:

* vendor-specific terminology
* temporary technology trends
* marketing language

---

## When to Add a New Category

Adding a category requires demonstrating:

1. the inefficiency domain is distinct
2. multiple families will exist within it
3. the domain is likely to persist

---

## When to Add a Family

Add a family when:

* multiple rules share a common domain
* grouping improves discoverability
* detection strategies are similar

---

## When Not to Add a Family

Do not add a family when:

* only one rule would exist
* the distinction is purely stylistic
* the difference is implementation-specific

---

## Taxonomy Stability

The taxonomy should evolve slowly.

Breaking changes to category codes are **major version changes**.

