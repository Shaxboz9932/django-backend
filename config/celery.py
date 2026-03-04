import os
from celery import Celery

# Django sozlamalarini celery uchun o'rnatish
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Barcha sozlamalarni settings.py dan 'CELERY' prefiksi bilan o'qiydi
app.config_from_object('django.conf:settings', namespace='CELERY')

# Tasklarni avtomatik qidirib topish
app.autodiscover_tasks()