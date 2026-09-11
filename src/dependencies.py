from fastapi import HTTPException, Request, status

from database.fake_db import FAKE_JOBS
from models.job import Job


def get_job_or_404(job_id: str, request: Request) -> Job:
    request.state.logger.info(f"Received request: {request.method} {request.url.path}")

    for job in FAKE_JOBS:
        if job.job_id == job_id:
            return job

    request.state.logger.warning(f"Job not found: {job_id}")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Job not found with id: {job_id}"
    )
