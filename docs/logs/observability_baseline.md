# Observability Baseline

## Purpose

Before introducing structured logging, I exercised the API using a simple
client script to establish a baseline for the application's behaviour and
output.

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

## Observations

- Uvicorn provides access logs
- It is difficult to correlate application messages with individual requests.

## Next Step

Replace print() statements with Python's logging infrastructure and
evaluate whether timestamps, log levels, and structured fields provide
better visibility.