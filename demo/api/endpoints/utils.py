from fastapi import APIRouter
from typing import Any

router = APIRouter()


@router.post("/test-celery/", response_model=Msg, status_code=201)
def test_celery(
        msg: Msg,
) -> Any:
    """
    Test Celery worker.
    """
    celery_app.send_task("demo.worker.test_celery", args=[msg.msg])
    return {"msg": "Word received"}
