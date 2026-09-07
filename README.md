# Backend Observability Lab

A small FastAPI backend built to explore backend observability, performance, and software engineering practices through incremental development.

Rather than adding logging, metrics, profiling, and tracing all at once, this project intentionally evolves from a simple API into a system with increasingly realistic traffic, latency, failure, and performance scenarios.

Each stage is used to identify what information is missing, what problems emerge, and what engineering techniques can address them.

## Goals

The project is designed to develop a practical understanding of:

- API design and validation
- Automated API testing
- Application logging
- Structured logging
- Request correlation
- Simulated traffic and failures
- Performance and latency measurement
- Metrics
- Load testing
- Profiling and performance analysis
- Distributed tracing
- The relationship between logs, metrics, and traces
- Using measurements, metrics, and profiling to identify areas for code improvement
- Iteratively improving the system based on evidence rather than assumptions

The emphasis is on understanding **why** each technique is useful rather than simply learning how to configure individual tools.

---

## Current Project

The application is currently a small CRUD API for managing jobs.

### API

| Method   | Endpoint         | Purpose                 |
| -------- | ---------------- | ----------------------- |
| `GET`    | `/jobs`          | Retrieve all jobs       |
| `GET`    | `/jobs/{job_id}` | Retrieve a specific job |
| `POST`   | `/jobs`          | Create a job            |
| `PUT`    | `/jobs/{job_id}` | Update a job            |
| `DELETE` | `/jobs/{job_id}` | Delete a job            |

The API currently uses an in-memory list of `Job` objects rather than a database. This keeps the application deliberately small so that the focus can remain on application behaviour, testing, observability, and performance.

### Validation

Request validation is handled at the API boundary using Pydantic.

`Job` currently validates that:

- `job_id` is not empty
- `job_type` is not empty
- `job_message` is not empty
- string values cannot consist entirely of whitespace

Invalid request bodies are rejected by FastAPI with a `422 Unprocessable Entity` response.

---

## Testing

The API has contract tests covering the main behaviour of each endpoint.

The current test suite verifies:

- successful retrieval of all jobs
- empty job collections
- successful retrieval of an individual job
- nonexistent jobs returning `404`
- successful job creation
- invalid job requests returning `422`
- successful deletion
- nonexistent jobs returning `404`
- successful updates
- nonexistent update targets returning `404`

The tests use FastAPI's `TestClient` and pytest.

The tests are intended to verify the **API contract and observable behaviour**, rather than testing FastAPI or Pydantic internals.

---

## Observability and Performance Evolution

The project is being developed incrementally. Each stage introduces a new problem or source of complexity and uses that experience to motivate the next improvement.

### 1. Basic API

The project began with a deliberately simple FastAPI CRUD application.

The initial implementation provides a small system that can be exercised without introducing unnecessary infrastructure.

### 2. Observability Baseline

Basic `print()` statements were added to the endpoints to establish an initial view of application behaviour.

A simple client script was then used to exercise the API and observe the resulting output.

This established a baseline before introducing a dedicated logging system.

Detailed observations from this stage are documented in:

[`docs/logs/observability_baseline.md`](docs/logs/observability_baseline.md)

### 3. Simulated Traffic

The client is being extended to generate more realistic API traffic.

Instead of manually making individual requests, the simulator will generate combinations of:

- successful requests
- unsuccessful requests
- different endpoints
- different job IDs
- valid and invalid input
- variable delays between requests
- multiple simulated users

The purpose is to create enough activity that limitations in the initial `print()`-based logging become apparent.

### 4. Application Logging

The `print()` statements will be replaced with a proper logging system.

This will provide a foundation for:

- log levels
- timestamps
- consistent log messages
- contextual information
- configurable log destinations

The goal is to introduce these features in response to limitations observed during the previous stages.

### 5. Structured Logging and Request Correlation

Once basic logging is established, the project will explore structured log events and request correlation.

For example:

```json
{
  "level": "INFO",
  "event": "job_completed",
  "job_id": "001",
  "duration_ms": 823
}
```

Request identifiers will then be used to associate multiple log events with an individual request.

This becomes increasingly important when multiple requests are being processed concurrently.

### 6. Simulated Processing, Latency, and Failures

The application will introduce simulated job processing.

Jobs will be able to:

- complete quickly
- take an unusually long time
- fail

This will create realistic scenarios where observability is necessary to determine what happened.

The simulator and application will then provide a controlled environment for investigating questions such as:

- Which requests are slow?
- How slow are they?
- How frequently do failures occur?
- Which operations are responsible?
- Can a failed request be traced through the application?

### 7. Performance Measurement and Metrics

Metrics will be introduced to quantify application behaviour.

Examples include:

- request count
- error rate
- request duration
- latency distributions
- job processing duration
- throughput
- slow-request frequency

The goal is to move from:

> "This request looks slow."

to:

> "The measurements show that this endpoint's latency has increased."

### 8. Load Testing

The traffic simulator will eventually be extended or supplemented with load testing.

The goal is to investigate how application behaviour changes as traffic increases.

This will provide an opportunity to examine:

- throughput
- latency under load
- error rates
- resource usage
- application bottlenecks
- behaviour under sustained traffic

### 9. Profiling and Code Improvement

Once performance problems can be measured, profiling will be used to investigate their causes.

The intended feedback loop is:

```text
Measure
   ↓
Identify a problem
   ↓
Profile
   ↓
Identify the bottleneck
   ↓
Improve the code
   ↓
Measure again
   ↓
Compare results
```

This is intended to reinforce the principle that performance improvements should be based on evidence rather than assumptions.

### 10. Distributed Tracing

Distributed tracing will eventually be introduced to investigate how individual requests move through different components of the application.

The project will explore how traces complement logs and metrics and when each form of observability provides the most useful information.

---

## Architecture

The current architecture is intentionally simple:

```text
                 ┌─────────────────────┐
                 │  Simulated Client   │
                 └──────────┬──────────┘
                            │ HTTP
                            ▼
                 ┌─────────────────────┐
                 │      FastAPI        │
                 │                     │
                 │     Endpoints       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Job Model       │
                 │     (Pydantic)      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   In-memory Jobs    │
                 │     FAKE_JOBS       │
                 └─────────────────────┘
```

The architecture will become more sophisticated only when the next stage of the investigation requires it.

---

## Development Philosophy

This project intentionally avoids introducing infrastructure or optimizations prematurely.

Each stage follows an evidence-driven feedback loop:

```text
Build
  ↓
Exercise
  ↓
Measure / Observe
  ↓
Identify limitations
  ↓
Investigate
  ↓
Improve
  ↓
Measure again
```

This makes the project an experiment in observability and performance rather than simply a collection of technologies.

The aim is to understand the practical questions that logs, metrics, traces, load testing, and profiling are designed to answer — and how those tools can be used to make informed engineering decisions.

---

## Running the Project

### Start the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### Run the tests

```bash
pytest
```

### Run the traffic simulator

With the API running in another terminal:

```bash
python scripts/simulate_users.py
```

The simulator acts as an external client and sends HTTP requests to the running API.

---

## Project Structure

The structure will evolve as the project develops. The current organization is approximately:

```text
backend-observability-lab/
│
├── docs/
│   └── logs/
│       └── observability_baseline.md
│
├── routers/
│   └── endpoints.py
│
├── models/
│   └── job.py
│
├── scripts/
│   └── simulate_users.py
│
├── tests/
│   └── ...
│
├── main.py
└── README.md
```
