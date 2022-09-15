from fastapi import APIRouter
from demo.api.endpoints import run, utils, report, make

api_router = APIRouter()
api_router.include_router(run.router, prefix="/run", tags=["用例执行"])
api_router.include_router(utils.router, prefix="/utils", tags=["工具"])
api_router.include_router(report.router, prefix="/report", tags=["报告查看"])
api_router.include_router(make.router, prefix="/make", tags=["数据构造"])
