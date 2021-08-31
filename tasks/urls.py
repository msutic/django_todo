from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='task-list'),
    path('<int:pk>/', views.task_detail, name='task-detail'),
    path('<int:pk>/delete/', views.task_delete, name='task-delete'),
]