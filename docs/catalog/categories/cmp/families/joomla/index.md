# Joomla (JOOMLA)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 10

## Rules

### [ECO-CMP-JOOMLA-001 — Extension query inside item loop](../../../../ECO-CMP-JOOMLA-001.md)

A Joomla component, module, or plugin queries the database inside a loop over content items.

- Layer: **code**

### [ECO-CMP-JOOMLA-002 — Plugin runs heavy logic on broad events](../../../../ECO-CMP-JOOMLA-002.md)

A Joomla plugin performs expensive work on global events that fire across many page requests.

- Layer: **code**

### [ECO-CMP-JOOMLA-003 — Template loads unbundled duplicate assets](../../../../ECO-CMP-JOOMLA-003.md)

A Joomla template or extension loads duplicate JavaScript/CSS assets across modules.

- Layer: **code**

### [ECO-CMP-JOOMLA-004 — Disabled or bypassed Joomla cache](../../../../ECO-CMP-JOOMLA-004.md)

Extension or template code bypasses cacheable Joomla content paths for stable output.

- Layer: **code**

### [ECO-CMP-JOOMLA-005 — Large media served without optimization](../../../../ECO-CMP-JOOMLA-005.md)

Joomla templates or content fields serve oversized images or unoptimized media variants.

- Layer: **code**

### [ECO-CMP-JOOMLA-006 — Manifest or update checks in request path](../../../../ECO-CMP-JOOMLA-006.md)

Extension code performs remote update checks or manifest reads during normal page rendering.

- Layer: **code**

### [ECO-CMP-JOOMLA-007 — Unbounded module rendering on every page](../../../../ECO-CMP-JOOMLA-007.md)

Modules render expensive queries or transformations site-wide regardless of page context.

- Layer: **code**

### [ECO-CMP-JOOMLA-008 — Verbose payload logging in extensions](../../../../ECO-CMP-JOOMLA-008.md)

Joomla extensions log request bodies, query results, or debug details in production.

- Layer: **code**

### [ECO-CMP-JOOMLA-009 — Inefficient ACL checks repeated per item](../../../../ECO-CMP-JOOMLA-009.md)

Extension code repeats authorization checks individually across large item lists.

- Layer: **code**

### [ECO-CMP-JOOMLA-010 — Synchronous third-party widgets on render](../../../../ECO-CMP-JOOMLA-010.md)

Templates or extensions block page rendering on third-party scripts or API calls.

- Layer: **code**
