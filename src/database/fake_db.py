from models.job import Job, JobType


def create_initial_jobs() -> list[Job]:
    return [
        Job(
            job_id="001",
            job_type=JobType.NORMAL,
            job_message="This is a normal job",
        ),
        Job(
            job_id="002",
            job_type=JobType.SLOW,
            job_message="This is a slow job!",
        ),
        Job(
            job_id="003",
            job_type=JobType.ERROR,
            job_message="This job produced an error!",
        ),
    ]


FAKE_JOBS = create_initial_jobs()


def reset_fake_jobs() -> None:
    FAKE_JOBS.clear()
    FAKE_JOBS.extend(create_initial_jobs())
