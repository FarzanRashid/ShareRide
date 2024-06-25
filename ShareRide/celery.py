import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ShareRide.settings')

app = Celery('ShareRide')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-requests-every-minute': {
        'task': 'requestride.tasks.check_requests',
        'schedule': crontab(minute='*'),
    },
    'check_pending_requests_every_15_minutes': {
        'task': 'requestride.tasks.check_old_pending_requests',
        'schedule': crontab(minute='*/15'),
    },
}
