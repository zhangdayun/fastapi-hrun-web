import os
import time

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel

from demo.api.api import api_router
from demo.api.deps import logs
from demo.core.config import settings

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    default_response_class=ORJSONResponse
)

app.include_router(api_router, prefix=settings.API_STR)


@app.get("/")
async def root():
    return {}


def run():
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    run()
