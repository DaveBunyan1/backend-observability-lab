import pytest

from routers.endpoints import FAKE_JOBS


@pytest.fixture(autouse=True)
def reset_fake_jobs():
    FAKE_JOBS.clear()
    FAKE_JOBS.update(
        {
            "001": {"job_type": "first_type", "job_message": "Hello"},
            "002": {"job_type": "second_type", "job_message": "World!"},
        }
    )
