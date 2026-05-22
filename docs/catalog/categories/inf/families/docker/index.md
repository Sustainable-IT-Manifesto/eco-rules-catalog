# Docker (DOCKER)

- [Back to Infrastructure (INF)](../../index.md)

**Total rules:** 5

## Rules

### [ECO-INF-DOCKER-001 — Missing multi-stage builds](../../../../ECO-INF-DOCKER-001.md)

Single-stage Docker builds often ship build tooling and temporary artifacts into runtime images, increasing image size and transfer cost.

- Layer: **process**

### [ECO-INF-DOCKER-002 — Oversized base image](../../../../ECO-INF-DOCKER-002.md)

Heavy base images increase transfer, storage, and patching footprint without improving runtime value.

- Layer: **architecture**

### [ECO-INF-DOCKER-003 — Missing or too-permissive .dockerignore](../../../../ECO-INF-DOCKER-003.md)

Large build contexts increase build time, cache churn, and unnecessary transfer to the Docker daemon.

- Layer: **process**

### [ECO-INF-DOCKER-004 — Package manager caches left in image layers](../../../../ECO-INF-DOCKER-004.md)

Leaving package indexes and caches behind increases image size with no runtime benefit.

- Layer: **process**

### [ECO-INF-DOCKER-005 — Build tooling shipped in runtime image](../../../../ECO-INF-DOCKER-005.md)

Runtime images should not carry compilers, package managers, or build-only tooling that is not needed after build.

- Layer: **process**
