from pydantic import BaseModel, Field, field_validator


class Job(BaseModel):
    job_id: str = Field(min_length=1)
    job_type: str = Field(min_length=1)
    job_message: str = Field(min_length=1)

    @field_validator("job_id", "job_type", "job_message")
    @classmethod
    def must_not_be_blank(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("must not be blank")

        return value
