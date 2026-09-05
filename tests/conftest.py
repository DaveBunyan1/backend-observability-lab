import pytest

from models.job import Job
from routers.endpoints import FAKE_JOBS


@pytest.fixture(autouse=True)
def reset_fake_jobs():
    FAKE_JOBS.clear()
    FAKE_JOBS.append(
        Job(job_id="001", job_type="first_type", job_message="This is the first job!"),
    )
    FAKE_JOBS.append(
        Job(job_id="002", job_type="second_type", job_message="This is the second!"),
    )
