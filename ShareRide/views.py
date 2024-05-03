from django.shortcuts import redirect
from django.urls import reverse


def logout(request):
    response = redirect(reverse('login'))
    response.delete_cookie('jwt')
    return response
