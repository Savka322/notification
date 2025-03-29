from celery import Celery

celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["app.worker"]
)

celery_app.conf.task_routes = {"app.worker.analyze_notification": "main-queue"}
celery_app.conf.update(task_track_started=True)