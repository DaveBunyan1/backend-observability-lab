from typing import Annotated

from fastapi import Body

from main import app

fake_jobs = {
    "001": {"job_type": "first_type", "job_message": "Hello"},
    "002": {"job_type": "second_type", "job_message": "World!"},
}


@app.get("/jobs")
def get_jobs():
    return {"jobs": fake_jobs}


@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    return fake_jobs[job_id]


@app.post("/jobs")
def create_job(job: Annotated[dict[str, dict[str, str]], Body()]):
    fake_jobs.update(job)
    return fake_jobs


@app.delete("/jobs/{job_id}")
def delete_job(job_id: str):
    return fake_jobs.pop(job_id)


@app.put("/jobs/{job_id}")
def update_job(
    job_id: str,
    job_message: Annotated[str, Body()],
):
    fake_jobs[job_id]["job_message"] = job_message
    return fake_jobs
