import argparse

LOG_FILE_PATH = "./logs/logs.log"


def analyze_logs(request_id: str):
    logs = []
    with open(LOG_FILE_PATH) as file:
        for line in file:
            if line.split(" ")[0] == request_id:
                logs.append(line)

    if logs:
        print(f"Logs for request_id {request_id}:")
        for log in logs:
            print(log, end="")
    else:
        print(f"No logs found with request_id {request_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Request ID")

    parser.add_argument("request_id")

    args = parser.parse_args()

    analyze_logs(args.request_id)
