from celery import Celery


app = Celery('proj')
app.config_from_object('celery.config', namespace='CELERY')
app.autodiscover_tasks()