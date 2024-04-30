from django.shortcuts import render, redirect
from django.urls import reverse
import jwt
from django.conf import settings
from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            token = jwt.encode(
                {'email': email},
                settings.SECRET_KEY,
                algorithm='HS256'
            ).decode('utf-8')
            response = redirect(reverse('login_success'))
            response.set_cookie('jwt', token, httponly=True)
            return response
        else:
            return render(request, 'login.html', {'form': form, 'error': form.errors})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
