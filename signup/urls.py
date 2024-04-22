from django.urls import path
from .views import signup, signup_success

urlpatterns = [
    path('', signup, name='signup'),
    path('success/', signup_success, name='signup_success'),
]
