from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    # Maps to POST /todos and GET /todos
    path('todos/', TaskListCreateView.as_view(), name='todo-list'),
    
    # Maps to GET /todos/1, PUT /todos/1, and DELETE /todos/1
    path('todos/<int:pk>/', TaskDetailView.as_view(), name='todo-detail'), 
]