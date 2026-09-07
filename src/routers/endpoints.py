from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from models.job import Job

router = APIRouter(prefix="")

FAKE_JOBS: list[Job] = [
    Job(job_id="001", job_type="first_type", job_message="This is the first job!"),
    Job(job_id="002", job_type="second_type", job_message="This is the second job!"),
]


@router.get("/jobs")
def get_jobs():
    print("Received request: GET /jobs")
    return {"jobs": FAKE_JOBS}


@router.get("/jobs/{job_id}")
def get_job(job_id: str) -> Job:
    print(f"Received request: GET /jobs/{job_id}")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            print(f"Found job: {job_id}")
            return job
    print(f"Job not found: {job_id}")
    raise HTTPException(status_code=404, detail=f"Job not found with id: {job_id}")


@router.post("/jobs", status_code=201)
def create_job(job: Annotated[Job, Body()]):
    print("Received request: POST /jobs")
    FAKE_JOBS.append(job)
    print(f"Job created successfully: {job}")
    return job


@router.delete("/jobs/{job_id}")
def delete_job(job_id: str):
    print(f"Received request: DELETE /jobs/{job_id}")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            FAKE_JOBS.remove(job)
            print(f"Deleted job: {job_id}")
            return job
    print(f"Job not found: {job_id}")
    raise HTTPException(status_code=404, detail="Job not found")


@router.put("/jobs/{job_id}")
def update_job(
    job_id: str,
    job_message: Annotated[str, Body()],
):
    print(f"Received request: PUT /jobs/{job_id}")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            job.job_message = job_message
            print(f"Updated job: {job_id} with message: {job_message}")
            return job
    print(f"Job not found: {job_id}")
    raise HTTPException(status_code=404, detail="Job not found")
