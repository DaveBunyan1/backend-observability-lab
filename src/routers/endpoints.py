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
    return {"jobs": FAKE_JOBS}


@router.get("/jobs/{job_id}")
def get_job(job_id: str) -> Job:
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            return job
    raise HTTPException(status_code=404, detail=f"Job not found with id: {job_id}")


@router.post("/jobs", status_code=201)
def create_job(job: Annotated[Job, Body()]):
    FAKE_JOBS.append(job)
    return job


@router.delete("/jobs/{job_id}")
def delete_job(job_id: str):
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            FAKE_JOBS.remove(job)
            return job
    raise HTTPException(status_code=404, detail="Job not found")


@router.put("/jobs/{job_id}")
def update_job(
    job_id: str,
    job_message: Annotated[str, Body()],
):
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            job.job_message = job_message
            return job
    raise HTTPException(status_code=404, detail="Job not found")
