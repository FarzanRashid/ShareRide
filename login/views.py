from django.shortcuts import render, redirect
from django.urls import reverse
import jwt
from django.conf import settings
from .forms import LoginForm
from django.http import HttpResponseForbidden
from signup.models import Users


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
        if request.COOKIES.get('jwt'):
            return redirect(reverse('login_success'))
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

