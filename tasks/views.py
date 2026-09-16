from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .pagination import CustomTodoPagination

# Handles GET (all tasks) and POST (create task)
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] # Enforces the 401 Unauthorized error if no token is sent
    pagination_class = CustomTodoPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']  # Allows searching text in these fields
    ordering_fields = ['id', 'title']         # Allows sorting by ID or alphabetical title

    def get_queryset(self):
        # Security: Only return tasks created by the currently logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Security: Automatically attach the logged-in user to the new task
        serializer.save(user=self.request.user)

# Handles GET (single task), PUT (update), and DELETE
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Security: Ensure they can only view/edit/delete their own specific tasks
        return Task.objects.filter(user=self.request.user)