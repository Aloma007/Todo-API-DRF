from django.urls import path
from .views import RegisterView, LoginView # Imported LoginView here

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]