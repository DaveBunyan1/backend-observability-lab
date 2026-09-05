from collections.abc import Callable

from fastapi.testclient import TestClient

from main import app
from routers.endpoints import FAKE_JOBS

client = TestClient(app)


# get("/jobs") tests
class TestGetAllJobs:
    def test_get_all_jobs(self, reset_fake_jobs: Callable[..., None]):
        response = client.get("/jobs")

        assert response.status_code == 200

        data = response.json()
        jobs = data["jobs"]
        assert jobs == FAKE_JOBS


# get("/jobs/{job_id}") tests
class TestGetSingleJob:
    def test_get_single_job(self, reset_fake_jobs: Callable[..., None]):
        job_id = "001"
        response = client.get(f"/jobs/{job_id}")
        assert response.status_code == 200

        job = response.json()
        assert job == FAKE_JOBS[job_id]


# delete("/jobs/{job_id}"") tests
class TestDeleteJob:
    def test_delete_job(self, reset_fake_jobs: Callable[..., None]):
        job_id = "001"
        response = client.delete(f"/jobs/{job_id}")

        assert response.status_code == 200
        assert job_id not in FAKE_JOBS


# post("/jobs") tests
class TestCreateJob:
    def test_create_job(self, reset_fake_jobs: Callable[..., None]):
        job_id = "003"
        response = client.post("/jobs", json={job_id: {"job_type": "new_type"}})

        assert response.status_code == 200
        assert job_id in FAKE_JOBS


# put("/jobs/{job_id}") tests
class TestUpdateJob:
    def test_update_job(self, reset_fake_jobs: Callable[..., None]):
        job_id = "001"
        response = client.put(f"/jobs/{job_id}", json="new")

        assert response.status_code == 200
        assert FAKE_JOBS[job_id]["job_message"] == "new"
