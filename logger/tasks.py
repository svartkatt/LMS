from celery import shared_task

from logger.models import Log


@shared_task
def delete_logs():
    Log.objects.all().delete()
