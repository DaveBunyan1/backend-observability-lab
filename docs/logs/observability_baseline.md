# Observability Baseline

## Purpose

Before introducing structured logging, I exercised the API using a simple client script to establish a baseline for the application's behaviour and output.

## Example Output

```text
Received request: GET /jobs
INFO:     127.0.0.1:50589 - "GET /jobs HTTP/1.1" 200 OK
Received request: GET /jobs/001
Found job: 001
INFO:     127.0.0.1:50589 - "GET /jobs/001 HTTP/1.1" 200 OK
Received request: GET /jobs/999
Job not found: 999
INFO:     127.0.0.1:50589 - "GET /jobs/999 HTTP/1.1" 404 Not Found
Received request: POST /jobs
Job created successfully: job_id='003' job_type='simulated' job_message='Hello'
INFO:     127.0.0.1:50589 - "POST /jobs HTTP/1.1" 201 Created
Received request: PUT /jobs/003
Updated job: 003 with message: Updated
INFO:     127.0.0.1:50589 - "PUT /jobs/003 HTTP/1.1" 200 OK
Received request: DELETE /jobs/003
Deleted job: 003
INFO:     127.0.0.1:50589 - "DELETE /jobs/003 HTTP/1.1" 200 OK
Received request: DELETE /jobs/999
Job not found: 999
INFO:     127.0.0.1:50589 - "DELETE /jobs/999 HTTP/1.1" 404 Not Found
```

### Observations

- Uvicorn provides access logs

## Simulated Traffic

The initial deterministic API calls were replaced with a traffic simulation that randomly selects API operations and job IDs, and delays each request randomly between 0.2 and 1.0 seconds.

The simulation produced a mixture of successful and unsuccessful requests.

### Observations

- Repeated runs of the simulation highlighted the value of a way of distinguishing between different requests of the same type.

## Concurrent Traffic

The traffic simulation was modified to issue requests concurrently rather than sequentially.

### Observations

- Application log messages became interleaved, making it difficult to determine which messages belonged to the same request.
- Requests were completed in a different order from which they were initiated.
- The existing application logs do not provide a mechanism for explicitly correlating related messages with an individual request.

## Concurrent Traffic

The traffic simulation was modified to issue requests concurrently rather than sequentially. A single run was performed with 30 simulated users, with each user making one request.

### Script Output

The simulation began by initiating all 30 requests in user order:

```text
User 1 performing action delete_job
User 2 performing action create_job
User 3 performing action update_job
...
User 30 performing action get_job
```

However, the requests completed in a different order:

```text
User 1: DELETE /jobs/002 → 200
User 7: PUT /jobs/001 → 200
User 20: GET /jobs → 200
User 12: PUT /jobs/001 → 200
User 3: PUT /jobs/1000 → 404
...
User 13: POST /jobs → 201
User 25: DELETE /jobs/002 → 404
User 17: GET /jobs/001 → 200
User 11: GET /jobs/001 → 200
```

This demonstrates that with concurrent requests, **request completion order is not necessarily the same as request initiation order**.

The complete script output is available in [Basic script output](./log_output/basic_script_output.md).

### API Output

The application logs also became interleaved as requests were processed concurrently, with uvicorn logs also starting to mix in:

```text
Received request: GET /jobs/001
Received request: GET /jobs/002
Job not found: 002
Received request: DELETE /jobs/002
Received request: GET /jobs/002
Found job: 001
Received request: GET /jobs/1000
Job not found: 002
Received request: DELETE /jobs/1000
INFO:     127.0.0.1:54414 - "PUT /jobs/001 HTTP/1.1" 200 OK
Received request: POST /jobs
Job not found: 1000
Job not found: 1000
```

The individual application messages can no longer be reliably associated with a particular request from the application output alone.

The complete API output is available in [Basic API output](./log_output/basic_api_output.md).

### Observations

- Concurrent requests caused application log messages to become interleaved, making it difficult to associate related messages with an individual request.
- Request completion order differed from request initiation order.
- The existing application logs do not provide a mechanism for explicitly correlating messages belonging to the same request.

## Request ID Experiment

To address the correlation problem identified during concurrent traffic, a unique request ID was generated at the HTTP boundary using FastAPI middleware. The ID was then included in application-level log messages.

The same concurrent traffic simulation was run again.

### Example

Multiple requests were processed concurrently:

```text
81806ffe-c739-4508-877b-c94b7bc4b52a Received request: POST /jobs
07ad800c-8aa9-4da2-a19d-b8063e6351c2 Received request: POST /jobs
81806ffe-c739-4508-877b-c94b7bc4b52a Job created successfully: job_id='498' job_type='simulated' job_message='Hello'
07ad800c-8aa9-4da2-a19d-b8063e6351c2 Job created successfully: job_id='416' job_type='simulated' job_message='Hello'
```

Although messages from different requests are interleaved, the request ID makes it possible to associate related messages with the same request.

For example:

```text
81806ffe... → POST /jobs → job 498
07ad800c... → POST /jobs → job 416
```

### Observations

- Request IDs allow application log messages to be associated with an individual request.
- Interleaved messages from concurrent requests can now be distinguished from one another.
- The request ID is generated at the HTTP boundary, allowing it to be associated with the request independently of the endpoint being called.
- The Uvicorn access logs do not currently contain the application request ID, so the application logs and access logs remain separate sources of information.

The complete API output is available in [Request ID API output](./log_output/request_id_api_output.md).

## Request Timing

Request processing time was added at the HTTP boundary using `time.perf_counter()`.
The measured duration was returned in the `X-Process-Time` response header.

Example client output:

```text
User 5: GET /jobs → 200 (6.10 ms)
User 3: POST /jobs → 201 (8.08 ms)
User 6: GET /jobs/002 → 200 (7.63 ms)
```

The complete timing output is available in [timing script output](./log_output/timing_script_output.md)
