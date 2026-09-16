from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # We only expose id, title, and description to match your guide's JSON screenshots
        fields = ['id', 'title', 'description']