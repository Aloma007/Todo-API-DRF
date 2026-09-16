from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This forwards any request to /users/ to our custom app
    path('', include('users.urls')), 
    path('', include('tasks.urls')),
]