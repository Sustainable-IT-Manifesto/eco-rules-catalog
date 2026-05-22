# Network rules

**Code:** `network`

**Total rules:** 25

- [Back to Human Catalog](../index.md)

## Rules

### [ECO-CMP-JS-002 — Polling instead of events](../ECO-CMP-JS-002.md)

Polling increases unnecessary network traffic and compute.

- Category: **Computation**
- Family: **JavaScript**
- Layer: **network**

### [ECO-CMP-JS-006 — Over-fetching API responses](../ECO-CMP-JS-006.md)

Returning unused fields increases payload size and wasted processing.

- Category: **Computation**
- Family: **JavaScript**
- Layer: **network**

### [ECO-CMP-JS-007 — Missing HTTP caching headers (client-side)](../ECO-CMP-JS-007.md)

Missing cache headers causes repeated downloads and wasted bandwidth.

- Category: **Computation**
- Family: **JavaScript**
- Layer: **network**

### [ECO-CMP-JS-010 — Missing request timeout](../ECO-CMP-JS-010.md)

Requests without timeouts hang and create cascading latency.

- Category: **Computation**
- Family: **JavaScript**
- Layer: **network**

### [ECO-CMP-JS-012 — Redundant API calls in component lifecycle](../ECO-CMP-JS-012.md)

Repeated fetches on rerender waste network and CPU.

- Category: **Computation**
- Family: **JavaScript**
- Layer: **network**

### [ECO-CMP-JS-013 — Uncompressed static assets](../ECO-CMP-JS-013.md)

Serving assets without compression increases bandwidth and energy use.

- Category: **Computation**
- Family: **JavaScript**
- Layer: **network**

### [ECO-CMP-PY-006 — Missing network timeout](../ECO-CMP-PY-006.md)

Network calls without explicit timeouts can hang and cascade failures.

- Category: **Computation**
- Family: **Python**
- Layer: **network**

### [ECO-CMP-UI-002 — Excessive polling from client UI](../ECO-CMP-UI-002.md)

Frontend code polls APIs frequently when event-driven, cached, or user-triggered updates would be sufficient.

- Category: **Computation**
- Family: **Frontend/UI**
- Layer: **network**

### [ECO-NET-NET-001 — Missing HTTP caching headers](../ECO-NET-NET-001.md)

Missing cache headers causes repeated downloads and wasted work.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-002 — No gzip/brotli compression](../ECO-NET-NET-002.md)

Serving text assets without compression increases bandwidth and energy use.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-003 — Chatty microservice communication](../ECO-NET-NET-003.md)

Many small calls increase latency and cross-service overhead.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-004 — Redundant authentication calls](../ECO-NET-NET-004.md)

Repeated auth calls waste CPU and network and add latency.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-005 — Missing timeouts](../ECO-NET-NET-005.md)

Missing timeouts remove a critical reliability boundary for network calls.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-006 — No connection reuse (keep-alive disabled)](../ECO-NET-NET-006.md)

Disabling keep-alive increases handshake overhead and latency.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-007 — Excessive retry storms](../ECO-NET-NET-007.md)

Aggressive retries amplify failures and increase waste.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-008 — Over-fetching API fields](../ECO-NET-NET-008.md)

Returning unnecessary fields increases payload size and processing.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-009 — Under-fetching causing follow-up calls](../ECO-NET-NET-009.md)

Responses missing needed data cause extra round trips.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-010 — Large payloads without pagination](../ECO-NET-NET-010.md)

Large unpaginated responses increase memory and bandwidth waste.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-011 — No CDN usage for static content](../ECO-NET-NET-011.md)

Serving static content from origin increases latency and origin load.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-012 — No HTTP/2 or HTTP/3 where applicable](../ECO-NET-NET-012.md)

Older HTTP versions may reduce efficiency for multiplexed workloads.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-013 — Excessive polling intervals](../ECO-NET-NET-013.md)

Frequent polling increases load even when nothing changes.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-014 — Synchronous cross-region calls](../ECO-NET-NET-014.md)

Cross-region synchronous calls increase latency and cost.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-NET-NET-015 — Missing circuit breaker patterns](../ECO-NET-NET-015.md)

Without circuit breakers, failures propagate and waste resources.

- Category: **Networking**
- Family: **Network**
- Layer: **network**

### [ECO-OBS-TRACE-001 — Unsampled high-volume tracing](../ECO-OBS-TRACE-001.md)

Tracing is enabled for high-volume paths without sampling, retention limits, or cardinality controls.

- Category: **Observability & Telemetry**
- Family: **Tracing**
- Layer: **network**

### [ECO-OPS-SEC-001 — Repeated token introspection on hot path](../ECO-OPS-SEC-001.md)

Every request performs remote token introspection or identity lookup without safe caching or local validation.

- Category: **Operations**
- Family: **Identity & Security Efficiency**
- Layer: **network**
