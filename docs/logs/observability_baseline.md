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
- It is difficult to correlate application messages with individual requests.

## Simulated Traffic

The initial deterministic API calls were replaced with a traffic simulation that randomly selects API operations and job IDs, and delays each request randomly between 0.2 and 1.0 seconds.

The simulation produced a mixture of successful and unsuccessful requests.

### Observations

- Repeated runs of the simulation highlighted the value of timestamps for establishing the timing of requests and making a particular request easier to locate.

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
