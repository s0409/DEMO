from celery import shared_task

from .models import Task


@shared_task
def update_task_status(task_id):
    try:
        task = Task.objects.get(pk=task_id)

        if task.priority == '0':
            task.status = '1'
            task.save()
            update_task_status.apply_async((task_id,), countdown=60) 
        elif task.priority == '1':
            task.status = '1'
            task.save()
            update_task_status.apply_async((task_id,), countdown=120)  
        elif task.priority == '2':
            task.status = '1'
            task.save()
            update_task_status.apply_async((task_id,), countdown=300) 

    except Task.DoesNotExist:
        pass
