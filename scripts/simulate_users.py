import random
import time

import httpx2

BASE_URL = "http://127.0.0.1:8000"


def simulate_user(user_id: int) -> None:
    with httpx2.Client(base_url=BASE_URL) as client:
        action = random.choice(
            ["get_all", "get_job", "create_job", "update_job", "delete_job"]
        )

        print(f"User {user_id} performing action {action}")

        if action == "get_all":
            response = client.get("/jobs")
        elif action == "get_job":
            # 001 will always be successful, 002 will be if not deleted, 1000 will always fail
            job_id = random.choice(["001", "002", "1000"])
            response = client.get(f"/jobs/{job_id}")
        elif action == "create_job":
            job_id = str(random.randint(100, 999))
            response = client.post(
                "/jobs",
                json={
                    "job_id": job_id,
                    "job_type": "simulated",
                    "job_message": "Hello",
                },
            )

        elif action == "update_job":
            job_id = random.choice(["001", "002", "1000"])
            response = client.put(
                f"/jobs/{job_id}",
                json="Updated by simulated user",
            )

        elif action == "delete_job":
            job_id = random.choice(["002", "1000"])
            response = client.delete(f"/jobs/{job_id}")

        print(
            f"User {user_id}: "
            f"{response.request.method} {response.request.url.path} "  # type: ignore
            f"→ {response.status_code}"  # type: ignore
        )


def main():
    for user_id in range(1, 11):
        simulate_user(user_id)
        time.sleep(random.uniform(0.2, 1.0))


if __name__ == "__main__":
    main()
