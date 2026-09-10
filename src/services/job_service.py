import logging
import time

from models.job import Job, JobType

logger = logging.getLogger("Test Logging")


def process_job(job: Job, request_id: str):
    adapter = logging.LoggerAdapter(logger, {"request_id": request_id})
    adapter.info(f"Processing Job: {job.job_id}")
    try:
        if job.job_type == JobType.NORMAL:
            adapter.info(f"Finished job: {job.job_id}")
        elif job.job_type == JobType.SLOW:
            time.sleep(2)
            adapter.info(f"Finished job: {job.job_id}")
        elif job.job_type == JobType.ERROR:
            raise ValueError("Job Failed")
    except ValueError:
        adapter.info(f"Error for job: {job.job_id}")
