# Backend Observability Lab

A progressively evolving backend engineering project designed to explore how a simple FastAPI application develops into a production-oriented, observable, scalable service.

The project is intentionally built in stages. Each stage introduces new infrastructure or engineering practices in response to a concrete problem, rather than adding technologies simply for the sake of complexity.

## Goals

This project is intended as a practical reference and learning environment for:

- FastAPI and REST API design
- Python application structure and dependency management
- SQLAlchemy and PostgreSQL
- Redis for caching, rate limiting, and asynchronous work
- Background workers and job processing
- Docker and containerized development
- Application and structured logging
- Metrics and monitoring
- Prometheus and Grafana
- Distributed tracing with OpenTelemetry
- Centralized log aggregation
- Load and performance testing
- Failure testing and resilience
- Capacity planning and bottleneck analysis
- Testing, type checking, linting, and CI/CD
- Production-oriented architecture and operational practices

## Philosophy

The project follows an **evolutionary approach to architecture**.

The initial application should be intentionally simple. As requirements and operational problems are introduced, the architecture evolves to address them.

For example:

```text
Simple API
    ↓
Application logging
    ↓
Database persistence
    ↓
Caching
    ↓
Asynchronous job processing
    ↓
Multiple workers
    ↓
Containerization
    ↓
Load testing
    ↓
Metrics
    ↓
Dashboards
    ↓
Distributed tracing
    ↓
Resilience and failure handling
```

The goal is not simply to learn how to configure these technologies, but to understand:

- **What problem does this solve?**
- **When is it useful?**
- **What are its trade-offs?**
- **How does it interact with the rest of the system?**
- **How can its behaviour be measured?**
- **What happens when it fails?**

## Learning Path

### Phase 1 — Application Fundamentals

- [ ] Create a basic FastAPI application
- [ ] Build REST endpoints
- [ ] Introduce request/response models
- [ ] Explore FastAPI dependency injection
- [ ] Start with simple `print()` debugging
- [ ] Replace `print()` with Python logging
- [ ] Configure log levels and handlers
- [ ] Introduce structured logging
- [ ] Add request IDs/correlation IDs

### Phase 2 — Persistence

- [ ] Introduce SQLAlchemy
- [ ] Model application data
- [ ] Introduce PostgreSQL
- [ ] Understand sessions and transactions
- [ ] Explore connection pooling
- [ ] Add database migrations
- [ ] Measure database query performance
- [ ] Investigate slow queries
- [ ] Demonstrate and fix N+1 queries

### Phase 3 — Redis

- [ ] Introduce Redis
- [ ] Implement caching
- [ ] Explore TTLs and cache invalidation
- [ ] Implement rate limiting
- [ ] Explore atomic Redis operations
- [ ] Use Redis for asynchronous job processing
- [ ] Explore queue depth and backpressure

### Phase 4 — Background Processing

- [ ] Separate API and worker processes
- [ ] Submit asynchronous jobs
- [ ] Track job state
- [ ] Implement multiple workers
- [ ] Handle failed jobs
- [ ] Implement retries
- [ ] Explore idempotency
- [ ] Introduce dead-letter handling
- [ ] Explore graceful worker shutdown

### Phase 5 — Docker

- [ ] Containerize the API
- [ ] Containerize workers
- [ ] Run PostgreSQL in Docker
- [ ] Run Redis in Docker
- [ ] Introduce Docker Compose
- [ ] Add health checks
- [ ] Explore service networking
- [ ] Add resource limits
- [ ] Investigate container failure and recovery

### Phase 6 — Load & Performance Testing

- [ ] Establish baseline performance
- [ ] Introduce a load-testing tool
- [ ] Measure requests per second
- [ ] Measure latency distributions
- [ ] Understand P50/P95/P99 latency
- [ ] Test increasing concurrency
- [ ] Find system bottlenecks
- [ ] Test database connection pool limits
- [ ] Test Redis under load
- [ ] Test worker scaling
- [ ] Establish approximate capacity limits

### Phase 7 — Metrics & Monitoring

- [ ] Introduce application metrics
- [ ] Track request count
- [ ] Track request latency
- [ ] Track error rates
- [ ] Track job processing
- [ ] Track queue depth
- [ ] Track database connection usage
- [ ] Introduce Prometheus
- [ ] Build Grafana dashboards
- [ ] Define useful operational metrics

### Phase 8 — Distributed Observability

- [ ] Introduce OpenTelemetry
- [ ] Add distributed traces
- [ ] Trace API requests
- [ ] Trace database operations
- [ ] Trace Redis operations
- [ ] Trace background jobs
- [ ] Correlate logs, metrics, and traces
- [ ] Introduce centralized log aggregation
- [ ] Investigate failures using telemetry rather than application logs alone

### Phase 9 — Resilience & Production Concepts

- [ ] Add request timeouts
- [ ] Add database/Redis failure handling
- [ ] Explore retry strategies
- [ ] Explore exponential backoff
- [ ] Introduce circuit breakers where appropriate
- [ ] Test partial system failures
- [ ] Test worker failures
- [ ] Test dependency outages
- [ ] Explore graceful degradation
- [ ] Perform capacity and failure experiments

## Experiments

The `experiments/` directory will contain small, focused experiments that demonstrate individual concepts.

Each experiment should document:

1. **Problem** — What are we trying to understand?
2. **Setup** — What was changed?
3. **Hypothesis** — What do we expect to happen?
4. **Experiment** — What did we measure?
5. **Results** — What actually happened?
6. **Explanation** — Why did it happen?
7. **Production implications** — What would matter in a real system?

Example experiments:

```text
experiments/
├── 01-print-vs-logging/
├── 02-structured-logging/
├── 03-request-correlation/
├── 04-sqlalchemy-query-performance/
├── 05-n-plus-one/
├── 06-connection-pool-exhaustion/
├── 07-redis-caching/
├── 08-rate-limiting/
├── 09-queue-backpressure/
├── 10-worker-scaling/
├── 11-load-testing/
├── 12-metrics/
├── 13-distributed-tracing/
└── 14-failure-testing/
```

The exact structure will evolve as the project develops.

## Project Structure

The initial structure is intentionally small:

```text
backend-observability-lab/
├── src/
│   └── backend_observability/
├── tests/
├── docs/
├── experiments/
├── .gitignore
├── Makefile
├── pyproject.toml
└── README.md
```

Additional infrastructure and application components will be introduced as they become necessary.

## Development

The project uses Python, FastAPI, SQLAlchemy, PostgreSQL, Redis, Docker, pytest, Ruff, mypy, and GitHub Actions as the system evolves.

Common development commands will be exposed through the `Makefile`, for example:

```bash
make test
make lint
make format
make typecheck
```

Additional commands will be added as new parts of the system are introduced.

## Key Principle

> **Don't add infrastructure until there is a problem worth solving.**

A technology should be introduced because an experiment, requirement, performance problem, reliability problem, or operational concern provides a reason to use it.

This keeps the project focused on understanding **why production systems are designed the way they are**, rather than simply reproducing a technology stack.

## Status

🚧 **Early development**

The project is intentionally being built from the ground up. The architecture, tooling, and infrastructure will evolve throughout the learning path.
