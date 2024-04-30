from django.urls import path
from .views import login, login_success

urlpatterns = [
    path('', login, name='login'),
    path("success/", login_success, name='login_success')
]
