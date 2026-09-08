from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, Request

from database.fake_db import FAKE_JOBS, reset_fake_jobs
from models.job import Job
from telemetry.logger import setup_logging

router = APIRouter(prefix="")

logger = setup_logging()


@router.get("/jobs")
def get_jobs(request: Request):
    request_id = request.state.request_id

    logger.info(f"{request_id} Received request: GET /jobs")
    return {"jobs": FAKE_JOBS}


@router.get("/jobs/{job_id}")
def get_job(job_id: str, request: Request) -> Job:
    request_id = request.state.request_id

    logger.info(f"{request_id} Received request: GET /jobs/{job_id}")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            logger.info(f"{request_id} Found job: {job_id}")
            return job

    logger.info(f"{request_id} Job not found: {job_id}")
    raise HTTPException(status_code=404, detail=f"Job not found with id: {job_id}")


@router.post("/jobs", status_code=201)
def create_job(job: Annotated[Job, Body()], request: Request):
    request_id = request.state.request_id

    logger.info(f"{request_id} Received request: POST /jobs")
    FAKE_JOBS.append(job)

    logger.info(f"{request_id} Job created successfully: {job}")
    return job


@router.delete("/jobs/{job_id}")
def delete_job(job_id: str, request: Request):
    request_id = request.state.request_id

    logger.info(f"{request_id} Received request: DELETE /jobs/{job_id}")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            FAKE_JOBS.remove(job)

            logger.info(f"{request_id} Deleted job: {job_id}")
            return job

    logger.info(f"{request_id} Job not found: {job_id}")
    raise HTTPException(status_code=404, detail="Job not found")


@router.put("/jobs/{job_id}")
def update_job(job_id: str, job_message: Annotated[str, Body()], request: Request):
    request_id = request.state.request_id

    logger.info(f"{request_id} Received request: PUT /jobs/{job_id}")
    for job in FAKE_JOBS:
        if job.job_id == job_id:
            job.job_message = job_message

            logger.info(
                f"{request_id} Updated job: {job_id} with message: {job_message}"
            )
            return job

    logger.info(f"{request_id} Job not found: {job_id}")
    raise HTTPException(status_code=404, detail="Job not found")


@router.post("/benchmark/reset")
def benchmark_reset():
    reset_fake_jobs()
