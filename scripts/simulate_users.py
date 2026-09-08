import asyncio
import random
from typing import TypedDict

import httpx2

from models.job import JobType

BASE_URL = "http://127.0.0.1:8000"
DEFAULT_NUM_USERS = 20
SEED = 42


class SimulateUserResponse(TypedDict):
    user_id: int
    method: str
    path: str
    status_code: int
    process_time_ms: float


JOB_IDS = ["001", "002", "003"]


async def simulate_user(
    user_id: int,
    client: httpx2.AsyncClient,
) -> SimulateUserResponse:
    # action = random.choice(
    #     ["get_all", "get_job", "create_job", "run_job", "update_job", "delete_job"]
    # )

    action = "run_job"
    if action == "get_all":
        response = await client.get("/jobs")
    elif action == "get_job":
        job_id = random.choice(JOB_IDS)
        response = await client.get(f"/jobs/{job_id}")
    elif action == "create_job":
        job_id = str(random.randint(100, 999))
        response = await client.post(
            "/jobs",
            json={
                "job_id": job_id,
                "job_type": random.choice(
                    [JobType.NORMAL, JobType.SLOW, JobType.ERROR]
                ),
                "job_message": "Hello",
            },
        )
    elif action == "run_job":
        job_id = random.choice(JOB_IDS)
        response = await client.post(f"jobs/{job_id}/run")
    elif action == "update_job":
        job_id = random.choice(JOB_IDS)
        response = await client.put(
            f"/jobs/{job_id}",
            json="Updated by simulated user",
        )
    elif action == "delete_job":
        job_id = random.choice(["002", "1000"])
        response = await client.delete(f"/jobs/{job_id}")
    else:
        raise ValueError(f"Unknown action: {action}")

    process_time = float(response.headers["X-Process-Time"])

    return {
        "user_id": user_id,
        "method": response.request.method,
        "path": response.request.url.path,
        "status_code": response.status_code,
        "process_time_ms": process_time * 1000,
    }


async def run_simulation(
    num_users: int, seed: int | None = None
) -> list[SimulateUserResponse]:
    random.seed(seed)

    async with httpx2.AsyncClient(base_url=BASE_URL) as client:
        users = [simulate_user(user_id, client) for user_id in range(1, num_users + 1)]
        results = await asyncio.gather(*users)

    return results


if __name__ == "__main__":
    asyncio.run(run_simulation(num_users=DEFAULT_NUM_USERS, seed=SEED))
