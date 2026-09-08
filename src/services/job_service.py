import logging
import time

from models.job import Job, JobType

logger = logging.getLogger("Test Logging")


def process_job(job: Job):
    print("Being called!")
    logger.info(f"Processing Job: {job.job_id}")
    if job.job_type == JobType.NORMAL:
        logger.info(f"Finished job: {job.job_id}")
    elif job.job_type == JobType.SLOW:
        time.sleep(2)
        logger.info(f"Finished job: {job.job_id}")
    elif job.job_type == JobType.ERROR:
        logger.info(f"Error for job: {job.job_id}")
        raise ValueError("Job Failed")
