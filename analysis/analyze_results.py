import csv
from pathlib import Path
from statistics import mean, median, stdev

import matplotlib.pyplot as plt

RESULTS_FILE = Path("benchmark_output/logging_results.csv")
OUTPUT_DIR = Path("analysis_output")
SUMMARY_FILE = OUTPUT_DIR / "summary.csv"


def percentile(values: list[float], percentile: float) -> float:
    values = sorted(values)

    index = (len(values) - 1) * percentile
    lower = int(index)
    upper = lower + 1

    if upper >= len(values):
        return values[lower]

    weight = index - lower
    return values[lower] + (values[upper] - values[lower]) * weight


def load_results() -> list[dict]:
    with RESULTS_FILE.open(newline="") as file:
        return list(csv.DictReader(file))


def group_by_users(results: list[dict]) -> dict[int, list[float]]:
    by_users: dict[int, list[float]] = {}

    for result in results:
        users = int(result["users"])
        process_time = float(result["process_time_ms"])

        by_users.setdefault(users, []).append(process_time)

    return by_users


def analyze_results(results: list[dict]) -> list[dict]:
    by_users = group_by_users(results)

    summary = []

    for users, values in sorted(by_users.items()):
        summary.append(
            {
                "users": users,
                "count": len(values),
                "mean_ms": mean(values),
                "median_ms": median(values),
                "min_ms": min(values),
                "max_ms": max(values),
                "p95_ms": percentile(values, 0.95),
                "p99_ms": percentile(values, 0.99),
                "std_dev_ms": stdev(values) if len(values) > 1 else 0.0,
            }
        )

    return summary


def save_summary(summary: list[dict]) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    with SUMMARY_FILE.open("w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "users",
                "count",
                "mean_ms",
                "median_ms",
                "min_ms",
                "max_ms",
                "p95_ms",
                "p99_ms",
                "std_dev_ms",
            ],
        )

        writer.writeheader()
        writer.writerows(summary)


def print_summary(summary: list[dict]) -> None:
    for row in summary:
        print(
            f"{row['users']:>5} users | "
            f"count={row['count']:>5} | "
            f"mean={row['mean_ms']:.2f} ms | "
            f"median={row['median_ms']:.2f} ms | "
            f"P95={row['p95_ms']:.2f} ms | "
            f"P99={row['p99_ms']:.2f} ms"
        )


def plot_latency_distribution(results: list[dict]) -> None:
    by_users = group_by_users(results)

    users = sorted(by_users)
    values = [by_users[user] for user in users]

    plt.figure()
    plt.boxplot(values, tick_labels=[str(user) for user in users])

    plt.xlabel("Concurrent users")
    plt.ylabel("Request processing time (ms)")
    plt.title("Request latency distribution by concurrency")

    plt.savefig(
        OUTPUT_DIR / "logging_latency_distribution.png",
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()


def plot_latency_percentiles(summary: list[dict]) -> None:
    users = [row["users"] for row in summary]
    median_values = [row["median_ms"] for row in summary]
    p95_values = [row["p95_ms"] for row in summary]
    p99_values = [row["p99_ms"] for row in summary]

    plt.figure()

    plt.plot(users, median_values, marker="o", label="Median")
    plt.plot(users, p95_values, marker="o", label="P95")
    plt.plot(users, p99_values, marker="o", label="P99")

    plt.xlabel("Concurrent users")
    plt.ylabel("Request processing time (ms)")
    plt.title("Request latency percentiles by concurrency")
    plt.legend()

    plt.savefig(
        OUTPUT_DIR / "logging_latency_percentiles.png",
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    results = load_results()
    summary = analyze_results(results)

    print_summary(summary)
    save_summary(summary)

    plot_latency_distribution(results)
    plot_latency_percentiles(summary)

    print(f"\nAnalysis written to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
