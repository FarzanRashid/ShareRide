from django.urls import path
from .views import ride_request

urlpatterns = [
    path('', ride_request, name='request'),
]
