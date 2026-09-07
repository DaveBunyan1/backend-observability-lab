```text
3207fcde-6697-48d2-8590-034473b4c8f8 Received request: DELETE /jobs/002
3207fcde-6697-48d2-8590-034473b4c8f8 Deleted job: 002
80da7649-9fcb-4e47-82de-2220587bf9db Received request: GET /jobs/1000
2423e1f8-6455-4eca-bcf6-61079a39a093 Received request: GET /jobs
80da7649-9fcb-4e47-82de-2220587bf9db Job not found: 1000
729963ab-e4e9-4d6a-8184-a5bdcec37f7d Received request: GET /jobs
82eb1964-c2db-41b4-92cb-e440cb54b7a2 Received request: GET /jobs/002
7bd36034-a94e-4836-b431-cc0a65fa400b Received request: GET /jobs/1000
82eb1964-c2db-41b4-92cb-e440cb54b7a2 Job not found: 002
7bd36034-a94e-4836-b431-cc0a65fa400b Job not found: 1000
3b287a16-599a-415d-bc25-bebdc2a515fb Received request: DELETE /jobs/002
INFO:     127.0.0.1:61123 - "DELETE /jobs/002 HTTP/1.1" 200 OK
3b287a16-599a-415d-bc25-bebdc2a515fb Job not found: 002
INFO:     127.0.0.1:61130 - "GET /jobs HTTP/1.1" 200 OK
81806ffe-c739-4508-877b-c94b7bc4b52a Received request: POST /jobs
07ad800c-8aa9-4da2-a19d-b8063e6351c2 Received request: POST /jobs
81806ffe-c739-4508-877b-c94b7bc4b52a Job created successfully: job_id='498' job_type='simulated' job_message='Hello'
07ad800c-8aa9-4da2-a19d-b8063e6351c2 Job created successfully: job_id='416' job_type='simulated' job_message='Hello'
INFO:     127.0.0.1:61124 - "GET /jobs/1000 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:61132 - "GET /jobs HTTP/1.1" 200 OK
INFO:     127.0.0.1:61128 - "GET /jobs/002 HTTP/1.1" 404 Not Found
0c37a7fb-a917-4526-b626-ddb6e0f29530 Received request: PUT /jobs/002
0c37a7fb-a917-4526-b626-ddb6e0f29530 Job not found: 002
INFO:     127.0.0.1:61125 - "GET /jobs/1000 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:61127 - "DELETE /jobs/002 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:61131 - "POST /jobs HTTP/1.1" 201 Created
INFO:     127.0.0.1:61126 - "POST /jobs HTTP/1.1" 201 Created
INFO:     127.0.0.1:61129 - "PUT /jobs/002 HTTP/1.1" 404 Not Found
```
