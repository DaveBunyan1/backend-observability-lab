from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, Request

from models.job import Job

router = APIRouter(prefix="")

FAKE_JOBS: list[Job] = [
    Job(job_id="001", job_type="first_type", job_message="This is the first job!"),
    Job(job_id="002", job_type="second_type", job_message="This is the second job!"),
]


@router.get("/jobs")
def get_jobs(request: Request):
    request_id = request.state.request_id
    with open("logs/logs.log", "a") as file:
        file.write(f"{request_id} Received request: GET /jobs\n")
    return {"jobs": FAKE_JOBS}


@router.get("/jobs/{job_id}")
def get_job(job_id: str, request: Request) -> Job:
    request_id = request.state.request_id
    with open("logs/logs.log", "a") as file:
        file.write(f"{request_id} Received request: GET /jobs/{job_id}\n")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            with open("logs/logs.log", "a") as file:
                file.write(f"{request_id} Found job: {job_id}\n")
            return job
    with open("logs/logs.log", "a") as file:
        file.write(f"{request_id} Job not found: {job_id}\n")
    raise HTTPException(status_code=404, detail=f"Job not found with id: {job_id}\n")


@router.post("/jobs", status_code=201)
def create_job(job: Annotated[Job, Body()], request: Request):
    request_id = request.state.request_id
    with open("logs/logs.log", "a") as file:
        file.write(f"{request_id} Received request: POST /jobs\n")
    FAKE_JOBS.append(job)
    with open("logs/logs.log", "a") as file:
        file.write(f"{request_id} Job created successfully: {job}\n")
    return job


@router.delete("/jobs/{job_id}")
def delete_job(job_id: str, request: Request):
    request_id = request.state.request_id
    with open("logs/logs.log", "a") as file:
        file.write(f"{request_id} Received request: DELETE /jobs/{job_id}\n")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            FAKE_JOBS.remove(job)
            with open("logs/logs.log", "a") as file:
                file.write(f"{request_id} Deleted job: {job_id}\n")
            return job
    with open("logs/logs.log", "a") as file:
        file.write(f"{request_id} Job not found: {job_id}\n")
    raise HTTPException(status_code=404, detail="Job not found")


@router.put("/jobs/{job_id}")
def update_job(job_id: str, job_message: Annotated[str, Body()], request: Request):
    request_id = request.state.request_id
    with open("logs/logs.log", "a") as file:
        file.write(f"{request_id} Received request: PUT /jobs/{job_id}\n")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            job.job_message = job_message
            with open("logs/logs.log", "a") as file:
                file.write(
                    f"{request_id} Updated job: {job_id} with message: {job_message}\n"
                )
            return job
    with open("logs/logs.log", "a") as file:
        file.write(f"{request_id} Job not found: {job_id}\n")
    raise HTTPException(status_code=404, detail="Job not found")
