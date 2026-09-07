import httpx2

BASE_URL = "http://127.0.0.1:8000"


def main() -> None:
    with httpx2.Client(base_url=BASE_URL) as client:
        client.get("/jobs")
        client.get("/jobs/001")
        client.get("/jobs/999")

        client.post(
            "/jobs",
            json={
                "job_id": "003",
                "job_type": "simulated",
                "job_message": "Hello",
            },
        )

        client.put("/jobs/003", json="Updated")

        client.delete("/jobs/003")
        client.delete("/jobs/999")


if __name__ == "__main__":
    main()
