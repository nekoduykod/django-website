from celery import Celery
from celery.schedules import crontab


app = Celery('proj')


app.config_from_object('celeryconfig.py', namespace='CELERY')


app.autodiscover_tasks()


app.conf.beat_schedule = {
    'execute-scrape-to-postgres': {
        'task': 'tasks.scrape_to_postgres',
        'schedule': crontab(hour=3, minute=0), # кожен день 3 АМ
    },
}