### Basic API output

Output from the API routes with basic randomized and concurrent calls. The related script output for these logs can be found:
[Script Output](./basic_script_output.md)

**Output:**

```text
Received request: DELETE /jobs/002
Deleted job: 002
Received request: PUT /jobs/001
Updated job: 001 with message: Updated by simulated user
Received request: GET /jobs
Received request: PUT /jobs/001
Updated job: 001 with message: Updated by simulated user
Received request: PUT /jobs/1000
Job not found: 1000
Received request: GET /jobs/002
Received request: PUT /jobs/1000
Job not found: 002
Job not found: 1000
Received request: DELETE /jobs/1000
Job not found: 1000
Received request: GET /jobs/001
Found job: 001
Received request: GET /jobs
Received request: GET /jobs/1000
Job not found: 1000
Received request: GET /jobs
Received request: DELETE /jobs/002
Received request: GET /jobs
Job not found: 002
Received request: DELETE /jobs/002
Job not found: 002
INFO:     127.0.0.1:54408 - "DELETE /jobs/002 HTTP/1.1" 200 OK
Received request: GET /jobs/002
Job not found: 002
Received request: POST /jobs
Job created successfully: job_id='462' job_type='simulated' job_message='Hello'
Received request: GET /jobs
Received request: POST /jobs
Job created successfully: job_id='528' job_type='simulated' job_message='Hello'
Received request: GET /jobs
Received request: PUT /jobs/002
Received request: DELETE /jobs/002
Job not found: 002
Job not found: 002
Received request: PUT /jobs/002
Job not found: 002
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
Job created successfully: job_id='530' job_type='simulated' job_message='Hello'
INFO:     127.0.0.1:54427 - "GET /jobs HTTP/1.1" 200 OK
Job not found: 002
INFO:     127.0.0.1:54419 - "PUT /jobs/001 HTTP/1.1" 200 OK
INFO:     127.0.0.1:54410 - "PUT /jobs/1000 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54423 - "PUT /jobs/1000 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54434 - "GET /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54435 - "DELETE /jobs/1000 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54436 - "GET /jobs HTTP/1.1" 200 OK
INFO:     127.0.0.1:54437 - "GET /jobs/1000 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54430 - "GET /jobs HTTP/1.1" 200 OK
INFO:     127.0.0.1:54428 - "GET /jobs HTTP/1.1" 200 OK
INFO:     127.0.0.1:54426 - "DELETE /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54425 - "DELETE /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54415 - "GET /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54422 - "POST /jobs HTTP/1.1" 201 Created
INFO:     127.0.0.1:54429 - "GET /jobs HTTP/1.1" 200 OK
INFO:     127.0.0.1:54409 - "POST /jobs HTTP/1.1" 201 Created
INFO:     127.0.0.1:54433 - "GET /jobs HTTP/1.1" 200 OK
INFO:     127.0.0.1:54417 - "PUT /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54416 - "DELETE /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54421 - "PUT /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54412 - "GET /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54411 - "GET /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54431 - "GET /jobs/1000 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54413 - "DELETE /jobs/1000 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54420 - "POST /jobs HTTP/1.1" 201 Created
INFO:     127.0.0.1:54432 - "DELETE /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54424 - "GET /jobs/001 HTTP/1.1" 200 OK
INFO:     127.0.0.1:54418 - "GET /jobs/001 HTTP/1.1" 200 OK
```
