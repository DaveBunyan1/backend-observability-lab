from typing import Annotated

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Body,
    Depends,
    Request,
    status,
)

from database.fake_db import FAKE_JOBS, reset_fake_jobs
from dependencies import get_job_or_404
from models.job import Job
from services.job_service import process_job

router = APIRouter(prefix="")


@router.get("/jobs")
def get_jobs(request: Request):
    request.state.logger.info("Received request: GET /jobs")
    return {"jobs": FAKE_JOBS}


@router.get("/jobs/{job_id}")
def get_job(
    request: Request,
    job: Job = Depends(get_job_or_404),
) -> Job:
    request.state.logger.info(f"Found job: {job.job_id}")
    return job


@router.post("/jobs", status_code=status.HTTP_201_CREATED)
def create_job(job: Annotated[Job, Body()], request: Request):
    request.state.logger.info("Received request: POST /jobs")
    FAKE_JOBS.append(job)
    request.state.logger.info(f"Job created successfully: {job}")
    return job


@router.post("/jobs/{job_id}/run", status_code=status.HTTP_202_ACCEPTED)
def run_job(
    request: Request,
    background_tasks: BackgroundTasks,
    job: Job = Depends(get_job_or_404),
):
    request.state.logger.info(f"Scheduling job: {job.job_id}")
    background_tasks.add_task(process_job, job, request.state.request_id)
    return job


@router.delete("/jobs/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(request: Request, job: Job = Depends(get_job_or_404)):
    FAKE_JOBS.remove(job)
    request.state.logger.info(f"Deleted job: {job.job_id}")
    return None


@router.put("/jobs/{job_id}")
def update_job(
    job_message: Annotated[str, Body()],
    request: Request,
    job: Job = Depends(get_job_or_404),
):
    job.job_message = job_message
    request.state.logger.info(f"Updated job: {job.job_id} with message: {job_message}")
    return job


@router.post("/benchmark/reset")
def benchmark_reset():
    reset_fake_jobs()
