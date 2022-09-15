from celery import Celery

celery_app = Celery("worker", broker="redis://@127.0.0.1/7")

celery_app.conf.task_routes = {"demo-test-web.worker.test_celery": "main-queue"}
