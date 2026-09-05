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

        assert data["jobs"] == [job.model_dump() for job in FAKE_JOBS]

    def test_no_job_returns_empty_list(self):
        FAKE_JOBS.clear()
        response = client.get("/jobs")

        assert response.status_code == 200

        data = response.json()

        assert data["jobs"] == []


# get("/jobs/{job_id}") tests
class TestGetSingleJob:
    def test_get_single_job(self, reset_fake_jobs: Callable[..., None]):
        job_id = "001"
        response = client.get(f"/jobs/{job_id}")
        assert response.status_code == 200

        assert response.json() == FAKE_JOBS[0].model_dump()

    def test_invalid_id_returns_404(self, reset_fake_jobs: Callable[..., None]):
        job_id = "abc"
        response = client.get(f"/jobs/{job_id}")

        print(response.json())
        assert response.status_code == 404
        assert response.json()["detail"] == f"Job not found with id: {job_id}"


# post("/jobs") tests
class TestCreateJob:
    def test_create_job(self, reset_fake_jobs: Callable[..., None]):
        job_id = "003"
        response = client.post(
            "/jobs",
            json={"job_id": job_id, "job_type": "new_type", "job_message": "..."},
        )

        assert response.status_code == 201
        assert response.json()["job_id"] == job_id
        assert response.json()["job_type"] == "new_type"
        assert response.json()["job_message"] == "..."

    def test_invalid_job_returns_422(self):
        response = client.post(
            "/jobs",
            json={"invalid_job": "Test"},
        )

        print(response.json())
        assert response.status_code == 422


# delete("/jobs/{job_id}"") tests
class TestDeleteJob:
    def test_delete_job(self, reset_fake_jobs: Callable[..., None]):
        job_id = "001"
        response = client.delete(f"/jobs/{job_id}")

        assert response.status_code == 200
        assert response.json()["job_id"] == job_id
        assert all(job.job_id != job_id for job in FAKE_JOBS)

    def test_delete_invalid_job_returns_404(self, reset_fake_jobs: Callable[..., None]):
        job_id = "Wrong-id"
        response = client.delete(f"/jobs/{job_id}")

        assert response.status_code == 404
        assert response.json()["detail"] == "Job not found"


# put("/jobs/{job_id}") tests
class TestUpdateJob:
    def test_update_job(self, reset_fake_jobs: Callable[..., None]):
        job_id = "001"
        response = client.put(f"/jobs/{job_id}", json="new")

        assert response.status_code == 200
        assert response.json()["job_id"] == job_id
        assert response.json()["job_message"] == "new"

    def test_update_invalid_job_returns_404(self, reset_fake_jobs: Callable[..., None]):
        job_id = "Wrong-id"

        response = client.put(f"/jobs/{job_id}", json="new")

        assert response.status_code == 404
        assert response.json()["detail"] == "Job not found"

    def test_update_invalid_body_returns_422(
        self, reset_fake_jobs: Callable[..., None]
    ):
        response = client.put("/jobs/001", json=123)

        assert response.status_code == 422
