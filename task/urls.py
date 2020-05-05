from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('task_add/', views.add_task, name="task-add"),
    path('task/<int:task_id>/', views.task_detail, name="task-detail"),
    path('task/delete/<int:task_id>/', views.task_delete, name="task-delete"),
    path('task/update/<int:task_id>/', views.task_update, name="task-update"),
]