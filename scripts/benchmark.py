import asyncio
import csv
from datetime import datetime
from pathlib import Path

import httpx2
from simulate_users import BASE_URL, run_simulation

CONCURRENCY_LEVELS = [30, 100, 1000]
RUNS_PER_LEVEL = 10
SEED = 42

OUTPUT_DIR = Path("benchmark_output")
RESULTS_FILE = OUTPUT_DIR / "results.csv"
RUNS_FILE = OUTPUT_DIR / "runs.csv"


async def run_benchmark() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    with (
        RESULTS_FILE.open("w", newline="") as results_file,
        RUNS_FILE.open("w", newline="") as runs_file,
    ):
        results_writer = csv.DictWriter(
            results_file,
            fieldnames=[
                "run_id",
                "timestamp",
                "users",
                "user_id",
                "method",
                "path",
                "status_code",
                "process_time_ms",
            ],
        )

        runs_writer = csv.DictWriter(
            runs_file,
            fieldnames=[
                "run_id",
                "timestamp",
                "users",
                "status",
                "error",
            ],
        )

        results_writer.writeheader()
        runs_writer.writeheader()

        run_id = 1

        for users in CONCURRENCY_LEVELS:
            for run in range(1, RUNS_PER_LEVEL + 1):
                print(f"Running {users} users - run {run}/{RUNS_PER_LEVEL}")
                async with httpx2.AsyncClient(base_url=BASE_URL) as client:
                    response = await client.post("/benchmark/reset")
                    response.raise_for_status()
                timestamp = datetime.now().isoformat()

                try:
                    results = await run_simulation(users, seed=SEED)

                except httpx2.PoolTimeout:
                    print(f"Pool timeout: {users} users - run {run}/{RUNS_PER_LEVEL}")

                    runs_writer.writerow(
                        {
                            "run_id": run_id,
                            "timestamp": timestamp,
                            "users": users,
                            "status": "pool_timeout",
                            "error": "PoolTimeout",
                        }
                    )

                except Exception as exc:
                    print(
                        f"Benchmark failed: {users} users - "
                        f"run {run}/{RUNS_PER_LEVEL}: {exc}"
                    )

                    runs_writer.writerow(
                        {
                            "run_id": run_id,
                            "timestamp": timestamp,
                            "users": users,
                            "status": "failed",
                            "error": type(exc).__name__,
                        }
                    )

                else:
                    for result in results:
                        results_writer.writerow(
                            {
                                "run_id": run_id,
                                "timestamp": timestamp,
                                "users": users,
                                **result,
                            }
                        )

                    runs_writer.writerow(
                        {
                            "run_id": run_id,
                            "timestamp": timestamp,
                            "users": users,
                            "status": "completed",
                            "error": "",
                        }
                    )

                    print(f"Completed {users} users - run {run}/{RUNS_PER_LEVEL}")

                results_file.flush()
                runs_file.flush()

                run_id += 1


if __name__ == "__main__":
    asyncio.run(run_benchmark())
