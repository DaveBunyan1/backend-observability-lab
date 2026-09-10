import asyncio
import random
from typing import TypedDict

import httpx2

BASE_URL = "http://127.0.0.1:8000"
NUM_USERS = 100
SEED = 42
MAX_ACTIONS = 5

SCENARIOS = [
    [
        ("GET", "/jobs"),
    ],
    [
        ("GET", "/jobs"),
        ("GET", "/jobs/001"),
    ],
    [
        ("GET", "/jobs/1000"),
        ("GET", "/jobs/001"),
    ],
    [("GET", "/jobs"), ("POST", "/jobs/003/run")],
    [("GET", "/jobs"), ("POST", "/jobs/004/run")],
]


class User(TypedDict):
    user_id: int
    num_scenarios: int


async def simulate_scenarios(user: User, client: httpx2.AsyncClient):
    for i in range(1, user["num_scenarios"] + 1):
        scenario = random.choice(SCENARIOS)

        print(
            f"User: {user['user_id']} "
            f"performing scenario {i} of {user['num_scenarios']}"
        )

        for method, endpoint in scenario:
            if method == "GET":
                await client.get(endpoint)
            elif method == "POST":
                await client.post(endpoint)
            elif method == "PUT":
                await client.put(endpoint)
            elif method == "DELETE":
                await client.delete(endpoint)


async def run_simulation(num_users: int, seed: int | None = None):
    random.seed(seed)
    users = [
        User(user_id=id, num_scenarios=random.randint(1, MAX_ACTIONS))
        for id in range(1, num_users + 1)
    ]

    async with httpx2.AsyncClient(base_url=BASE_URL) as client:
        scenarios = [simulate_scenarios(user, client) for user in users]
        await asyncio.gather(*scenarios)


if __name__ == "__main__":
    asyncio.run(run_simulation(num_users=NUM_USERS, seed=SEED))
