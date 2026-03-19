# Eco Rules Catalog

## A Standard for Identifying and Reducing Software Inefficiency

**Author:** Matt “Kelly” Williams
**Organization:** Sustainable IT Manifesto Foundation
**Version:** v0.2.1
**Date:** 18 March 2026

---

## Executive Summary

Waste is a bug.

In modern software systems, inefficiency is often treated as an acceptable side effect—something that “just happens” as systems scale and evolve. But inefficiency is not neutral. It carries real consequences: increased cost, degraded performance, higher energy consumption, and greater environmental impact.

The Eco Rules Catalog introduces a structured approach to identifying and addressing software inefficiency. It provides a shared language, a normalized rule model, and a growing catalog of inefficiency patterns across layers such as AI, architecture, code, data, network, and process.

This is not simply a documentation effort. It is the foundation of a standard—one that enables teams to recognize waste, reason about it, and reduce it in a consistent and actionable way.

---

## 1. Introduction

Software systems have become the backbone of modern life. Every organization is now, in some form, an IT organization. Every home is increasingly an IT environment.

And yet, inefficiency in software remains largely invisible.

Teams optimize for functionality and delivery. Systems that “work” are often accepted without deeper examination. Over time, small inefficiencies accumulate:

* unnecessary computation
* redundant data transfer
* inefficient architectural patterns
* excessive retries and polling
* over-provisioned infrastructure

Individually, these may appear insignificant. At scale, they are not.

The Eco Rules Catalog exists to make these patterns visible.

---

## 2. The Problem: Invisible Waste

One of the defining characteristics of software inefficiency is that it blends into the background.

This happens for several reasons:

### 2.1 Proximity dulls perception

When a pattern has always been present, it is rarely questioned. A loop that runs every second feels normal. A query that returns more data than needed feels acceptable.

### 2.2 Systems optimize for “working,” not “efficient”

If a system meets its functional requirements, inefficiency is often deprioritized. Performance tuning may occur later, if at all.

### 2.3 Lack of shared language

Teams frequently lack a consistent way to describe inefficiency. Without a shared vocabulary, patterns are difficult to communicate, compare, or track.

### 2.4 Fragmentation across layers

Inefficiency appears across multiple layers:

* AI (e.g., prompt design, inference patterns)
* architecture (e.g., service boundaries, coordination overhead)
* code (e.g., algorithms, memory usage)
* data (e.g., queries, storage patterns)
* network (e.g., payload size, retries)
* process (e.g., workflow inefficiencies)

Without a unifying model, these are treated as separate concerns.

---

## 3. A Core Insight

Performance, cost, and carbon are the same problem.

An inefficient system:

* uses more compute
* consumes more energy
* incurs higher cost
* produces greater environmental impact

These are not separate optimization domains. They are different expressions of the same underlying inefficiency.

By addressing inefficiency at the source, organizations can improve all three simultaneously.

---

## 4. The Eco Rules Catalog

The Eco Rules Catalog provides a structured way to describe inefficiency patterns.

Each rule captures:

* **Pattern** — what the inefficiency looks like
* **Impact** — why it matters (cost, latency, energy, etc.)
* **Detection** — how to identify it
* **Remediation** — how to reduce or eliminate it
* **Examples** — concrete illustrations of the pattern and its resolution

### 4.1 A normalized model

Rules are defined using a consistent schema, enabling:

* comparability across rules
* machine-readable analysis
* integration with tooling
* consistent documentation generation

### 4.2 Controlled vocabulary

The catalog uses a registry-based ontology to ensure consistent classification across:

* layers
* categories
* families

This prevents fragmentation and supports long-term standardization.

### 4.3 Deterministic generation

The catalog is generated deterministically from source rules, ensuring:

* reproducibility
* consistency across environments
* reliable versioning

---

## 5. Examples as a First-Class Concept

One of the most important recent additions to the catalog is support for examples.

Examples serve two purposes:

### 5.1 Recognition

They help practitioners recognize patterns in their own systems.

A description alone is often abstract. An example makes it concrete.

### 5.2 Action

They provide a starting point for remediation.

Seeing a “before” and “after” reduces friction and increases adoption.

Examples can be:

* structured summaries within rules
* detailed walkthroughs with code or architecture

This allows the catalog to support both quick reference and deeper learning.

---

## 6. Browsing and Discovery

The catalog supports multiple entry points:

* full catalog view
* browsing by layer
* examples index
* rule-specific navigation

This reflects a key design principle:

> People should be able to find what they need without knowing how the catalog is structured.

---

## 7. Use Cases

### 7.1 Software development teams

* identify inefficiencies early
* improve performance and cost
* reduce unnecessary complexity

### 7.2 Architects

* evaluate design tradeoffs
* reduce systemic inefficiency
* improve resilience and scalability

### 7.3 Organizations

* align engineering practices with sustainability goals
* reduce operational cost
* improve system reliability

### 7.4 Tool builders

* integrate rules into static analysis
* create automated detection pipelines
* build dashboards and scoring systems

---

## 8. Relationship to Sustainable IT

The Eco Rules Catalog aligns with the Sustainable IT Manifesto’s progression:

* **Aware** — recognizing that inefficiency exists
* **Conscious** — understanding its impact
* **Enabled** — having tools and frameworks to act
* **Empowered** — making better decisions consistently

The catalog plays a central role in moving from awareness to action.

---

## 9. Roadmap

The catalog is intentionally designed to evolve.

Near-term directions include:

* expanded rule coverage
* richer examples and walkthroughs
* category and family indexes
* integration with tooling (e.g., EcoAuditPro)
* alignment with certification programs

Longer-term goals include:

* broader community contribution
* formal standardization
* integration into education and training

---

## 10. Conclusion

Software inefficiency is not an unavoidable cost.

It is a pattern.

And patterns can be recognized, described, and changed.

The Eco Rules Catalog is a step toward making inefficiency visible—and actionable.

It provides a shared language, a structured model, and a growing body of knowledge that teams can use to build better systems.

Because waste is a bug.

---

## Appendix A: Access

Documentation:
[https://sustainable-it-manifesto.github.io/eco-rules-catalog/](https://sustainable-it-manifesto.github.io/eco-rules-catalog/)

Repository:
[https://github.com/sustainable-it-manifesto/eco-rules-catalog](https://github.com/sustainable-it-manifesto/eco-rules-catalog)
