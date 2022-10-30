from celery import Celery
from celery.schedules import crontab

from models import MongoMethods

# Initialize Celery
celery = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

db = MongoMethods()
celery.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasks.remove_collection',
        'schedule': crontab(minute='*/1'),
    },
}


@celery.task()
def remove_collection():
    db.remove_all_records()

