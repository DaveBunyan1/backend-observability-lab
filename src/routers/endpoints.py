from typing import Annotated

from fastapi import APIRouter, Body

router = APIRouter(prefix="")

FAKE_JOBS = {
    "001": {"job_type": "first_type", "job_message": "Hello"},
    "002": {"job_type": "second_type", "job_message": "World!"},
}


@router.get("/jobs")
def get_jobs():
    return {"jobs": FAKE_JOBS}


@router.get("/jobs/{job_id}")
def get_job(job_id: str):
    print("job_id:", job_id)
    print("fake_jobs:", FAKE_JOBS)
    return FAKE_JOBS[job_id]


@router.post("/jobs")
def create_job(job: Annotated[dict[str, dict[str, str]], Body()]):
    FAKE_JOBS.update(job)
    return FAKE_JOBS


@router.delete("/jobs/{job_id}")
def delete_job(job_id: str):
    return FAKE_JOBS.pop(job_id)


@router.put("/jobs/{job_id}")
def update_job(
    job_id: str,
    job_message: Annotated[str, Body()],
):
    FAKE_JOBS[job_id]["job_message"] = job_message
    return FAKE_JOBS
