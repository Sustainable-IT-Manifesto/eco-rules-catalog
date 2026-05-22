# JavaScript Frameworks (JSFW)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 10

## Rules

### [ECO-CMP-JSFW-001 — Component re-renders caused by unstable props](../../../../ECO-CMP-JSFW-001.md)

React, Vue, or similar components re-render frequently because props, callbacks, or objects are recreated on every render.

- Layer: **code**

### [ECO-CMP-JSFW-002 — Large client bundle from unused dependencies](../../../../ECO-CMP-JSFW-002.md)

A JavaScript framework app ships large dependencies or unused code to most users.

- Layer: **code**

### [ECO-CMP-JSFW-003 — Excessive hydration for mostly static pages](../../../../ECO-CMP-JSFW-003.md)

Framework pages hydrate large component trees even when most content is static.

- Layer: **code**

### [ECO-CMP-JSFW-004 — Polling loop without visibility or lifecycle controls](../../../../ECO-CMP-JSFW-004.md)

Frontend framework code polls APIs continuously even when the tab is hidden or data is unchanged.

- Layer: **code**

### [ECO-CMP-JSFW-005 — State store retains unbounded data](../../../../ECO-CMP-JSFW-005.md)

Client state stores accumulate records, histories, or cache entries without eviction.

- Layer: **code**

### [ECO-CMP-JSFW-006 — Rendering large lists without virtualization](../../../../ECO-CMP-JSFW-006.md)

A framework app renders large lists or tables fully in the DOM.

- Layer: **code**

### [ECO-CMP-JSFW-007 — Duplicate data fetching across components](../../../../ECO-CMP-JSFW-007.md)

Multiple components independently fetch the same data during a single page lifecycle.

- Layer: **code**

### [ECO-CMP-JSFW-008 — Image assets lack responsive delivery](../../../../ECO-CMP-JSFW-008.md)

Framework pages serve large images without responsive sizes, modern formats, or lazy loading.

- Layer: **code**

### [ECO-CMP-JSFW-009 — Route-level code split missing](../../../../ECO-CMP-JSFW-009.md)

Single-page apps load admin, dashboard, or rarely used route code in the initial bundle.

- Layer: **code**

### [ECO-CMP-JSFW-010 — Expensive computed selectors run every render](../../../../ECO-CMP-JSFW-010.md)

Framework selectors, computed values, or pipes recompute expensive transformations unnecessarily.

- Layer: **code**
