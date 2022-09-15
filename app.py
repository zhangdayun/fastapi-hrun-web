import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.exceptions import RequestValidationError

from demo.api.api import api_router
from demo.common.events import startup, stopping
from demo.core.config import settings
from demo.common.exception import http422_error_handler
from demo.schemas.requests.others import SystemItem

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    default_response_class=ORJSONResponse
)


@app.get("/")
async def root():
    return {}


@app.api_route(path="/healthcheck", methods=['GET', 'POST'])
async def health():
    return "success"


# 注册路由
app.include_router(api_router, prefix=settings.API_STR)

# 事件监听
app.add_event_handler("startup", startup(app))
app.add_event_handler("shutdown", stopping(app))

# 异常错误处理
app.add_exception_handler(RequestValidationError, http422_error_handler)


@app.post("/system", description="调用系统命令")
async def use_systems(command: SystemItem):
    if command.key != settings.SYSTEM_API_KEY:
        return {'result': "false"}
    return os.system(command.dict()['command'])


if __name__ == '__main__':
    uvicorn.run(app='app:app', host="0.0.0.0", port=8080)
    # uvicorn.run(app='app:app', host="127.0.0.1", port=7799, reload=True, debug=True)
