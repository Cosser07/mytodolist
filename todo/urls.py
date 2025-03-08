from django.urls import path
from .views import *

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task_update/<int:task_id>/', task_update, name='task_update'),
    path('task_delete/<int:task_id>/', task_delete, name='task_delete'),
    path('task/complete/<int:task_id>/', task_complete, name='task_complete'),
]