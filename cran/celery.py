import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('cran')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-15-minutes': {
        'task': 'cran.tasks.update_packages',
        'schedule': 60.0 * 15,
    },
}
app.conf.timezone = 'UTC'