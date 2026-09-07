from models.job import Job


def create_initial_jobs() -> list[Job]:
    return [
        Job(
            job_id="001",
            job_type="first_type",
            job_message="This is the first job!",
        ),
        Job(
            job_id="002",
            job_type="second_type",
            job_message="This is the second job!",
        ),
    ]


FAKE_JOBS = create_initial_jobs()


def reset_fake_jobs() -> None:
    FAKE_JOBS.clear()
    FAKE_JOBS.extend(create_initial_jobs())
