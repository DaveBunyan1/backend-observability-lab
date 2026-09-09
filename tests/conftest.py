import pytest

from models.job import Job, JobType
from routers.endpoints import FAKE_JOBS


@pytest.fixture(autouse=True)
def reset_fake_jobs():
    FAKE_JOBS.clear()
    FAKE_JOBS.append(
        Job(
            job_id="001", job_type=JobType.NORMAL, job_message="This is the first job!"
        ),
    )
    FAKE_JOBS.append(
        Job(job_id="002", job_type=JobType.SLOW, job_message="This is the second!"),
    )
