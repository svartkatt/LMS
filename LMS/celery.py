import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMS.settings')

app = Celery('LMS')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'delete_logs': {
        'task': 'logger.tasks.delete_logs',
        'schedule': crontab(hour=0)
    }
}

app.conf.beat_schedule = {
    'get_exchange_rates': {
        'task': 'exchanger.tasks.get_exchange_rates',
        'schedule': crontab(minute='*/30')
    }
}
