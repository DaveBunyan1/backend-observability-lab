from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Body, HTTPException, Request

from database.fake_db import FAKE_JOBS, reset_fake_jobs
from models.job import Job
from services.job_service import process_job

router = APIRouter(prefix="")


@router.get("/jobs")
def get_jobs(request: Request):
    request.state.logger.info("Received request: GET /jobs")
    return {"jobs": FAKE_JOBS}


@router.get("/jobs/{job_id}")
def get_job(job_id: str, request: Request) -> Job:
    request.state.logger.info(f"Received request: GET /jobs/{job_id}")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            request.state.logger.info(f"Found job: {job_id}")
            return job

    request.state.logger.info(f"Job not found: {job_id}")
    raise HTTPException(status_code=404, detail=f"Job not found with id: {job_id}")


@router.post("/jobs", status_code=201)
def create_job(job: Annotated[Job, Body()], request: Request):
    request.state.logger.info("Received request: POST /jobs")
    FAKE_JOBS.append(job)

    request.state.logger.info(f"Job created successfully: {job}")
    return job


@router.post("/jobs/{job_id}/run", status_code=202)
def run_job(job_id: str, request: Request, background_tasks: BackgroundTasks):
    request.state.logger.info(f"Received request: POST /jobs/{job_id}/run")

    for job in FAKE_JOBS:
        if job.job_id == job_id:
            request.state.logger.info(f"Scheduling job: {job_id}")
            background_tasks.add_task(process_job, job)
            return job

    request.state.logger.info(f"Job not found: {job_id}")
    raise HTTPException(status_code=404, detail="Job not found")


@router.delete("/jobs/{job_id}")
def delete_job(job_id: str, request: Request):
    request.state.logger.info(f"Received request: DELETE /jobs/{job_id}")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            FAKE_JOBS.remove(job)

            request.state.logger.info(f"Deleted job: {job_id}")
            return job

    request.state.logger.info(f"Job not found: {job_id}")
    raise HTTPException(status_code=404, detail="Job not found")


@router.put("/jobs/{job_id}")
def update_job(job_id: str, job_message: Annotated[str, Body()], request: Request):
    request.state.logger.info(f"Received request: PUT /jobs/{job_id}")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            job.job_message = job_message

            request.state.logger.info(
                f"Updated job: {job_id} with message: {job_message}"
            )
            return job

    request.state.logger.info(f"Job not found: {job_id}")
    raise HTTPException(status_code=404, detail="Job not found")


@router.post("/benchmark/reset")
def benchmark_reset():
    reset_fake_jobs()
