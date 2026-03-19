# Network rules

**Total rules:** 22

- [Back to Human Catalog](../index.md)
- [Back to Rule Browser](../../rule-browser.md)

## Rules

### [ECO-CMP-JS-002 — Polling instead of events](../ECO-CMP-JS-002.md)

Polling increases unnecessary network traffic and compute.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-006 — Over-fetching API responses](../ECO-CMP-JS-006.md)

Returning unused fields increases payload size and wasted processing.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-007 — Missing HTTP caching headers (client-side)](../ECO-CMP-JS-007.md)

Missing cache headers causes repeated downloads and wasted bandwidth.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-010 — Missing request timeout](../ECO-CMP-JS-010.md)

Requests without timeouts hang and create cascading latency.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-012 — Redundant API calls in component lifecycle](../ECO-CMP-JS-012.md)

Repeated fetches on rerender waste network and CPU.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-013 — Uncompressed static assets](../ECO-CMP-JS-013.md)

Serving assets without compression increases bandwidth and energy use.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-PY-006 — Missing network timeout](../ECO-CMP-PY-006.md)

Network calls without explicit timeouts can hang and cascade failures.

- Category: **CMP**
- Family: **PY**

### [ECO-NET-NET-001 — Missing HTTP caching headers](../ECO-NET-NET-001.md)

Missing cache headers causes repeated downloads and wasted work.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-002 — No gzip/brotli compression](../ECO-NET-NET-002.md)

Serving text assets without compression increases bandwidth and energy use.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-003 — Chatty microservice communication](../ECO-NET-NET-003.md)

Many small calls increase latency and cross-service overhead.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-004 — Redundant authentication calls](../ECO-NET-NET-004.md)

Repeated auth calls waste CPU and network and add latency.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-005 — Missing timeouts](../ECO-NET-NET-005.md)

Missing timeouts remove a critical reliability boundary for network calls.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-006 — No connection reuse (keep-alive disabled)](../ECO-NET-NET-006.md)

Disabling keep-alive increases handshake overhead and latency.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-007 — Excessive retry storms](../ECO-NET-NET-007.md)

Aggressive retries amplify failures and increase waste.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-008 — Over-fetching API fields](../ECO-NET-NET-008.md)

Returning unnecessary fields increases payload size and processing.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-009 — Under-fetching causing follow-up calls](../ECO-NET-NET-009.md)

Responses missing needed data cause extra round trips.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-010 — Large payloads without pagination](../ECO-NET-NET-010.md)

Large unpaginated responses increase memory and bandwidth waste.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-011 — No CDN usage for static content](../ECO-NET-NET-011.md)

Serving static content from origin increases latency and origin load.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-012 — No HTTP/2 or HTTP/3 where applicable](../ECO-NET-NET-012.md)

Older HTTP versions may reduce efficiency for multiplexed workloads.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-013 — Excessive polling intervals](../ECO-NET-NET-013.md)

Frequent polling increases load even when nothing changes.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-014 — Synchronous cross-region calls](../ECO-NET-NET-014.md)

Cross-region synchronous calls increase latency and cost.

- Category: **NET**
- Family: **NET**

### [ECO-NET-NET-015 — Missing circuit breaker patterns](../ECO-NET-NET-015.md)

Without circuit breakers, failures propagate and waste resources.

- Category: **NET**
- Family: **NET**
