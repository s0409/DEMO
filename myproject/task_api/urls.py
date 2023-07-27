from django.urls import path
from .views import CreateTask, GetTask, ListTask, DeleteTask
from . import views

urlpatterns = [
    path('create/',CreateTask.as_view()),
    path('get/<int:task_id>/',GetTask.as_view()),
    path('list/',ListTask.as_view()),
    path('delete/<int:task_id>/',DeleteTask.as_view()),
]