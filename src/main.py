from fastapi import FastAPI

from routers import endpoints

app = FastAPI()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


app.include_router(endpoints.router)
