from django.db import models
from django.conf import settings

class Task(models.Model):
    # This Foreign Key links the task strictly to the user who created it
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # The fields required by your project guide
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    # It's always good practice to track when a record was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title