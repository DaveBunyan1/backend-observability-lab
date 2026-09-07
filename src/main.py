import time
import uuid
from collections.abc import Awaitable, Callable

from fastapi import FastAPI, Request, Response

from routers import endpoints

app = FastAPI()


@app.middleware("http")
async def add_request_id(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
):
    start_time = time.perf_counter()
    request_id = str(uuid.uuid4())

    request.state.request_id = request_id

    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-time"] = str(process_time)

    return response


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


app.include_router(endpoints.router)
