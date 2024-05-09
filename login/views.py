from django.shortcuts import render, redirect
from django.urls import reverse
import jwt
from django.conf import settings
from .forms import LoginForm
from django.http import HttpResponseForbidden
from signup.models import Users
from requestride.models import Requests


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
            response = redirect(reverse('profile'))
            response.set_cookie('jwt', token, httponly=True)
            return response
        else:
            return render(request, 'login.html', {'form': form, 'error': form.errors})
    else:
        if request.COOKIES.get('jwt'):
            return redirect(reverse('profile'))
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def profile(request):
    jwt_token = request.COOKIES.get('jwt')
    if jwt_token:
        try:
            decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
            email = decoded_token['email']
            user = Users.objects.get(email=email)
            pending_requests = Requests.objects.filter(user=user, status='pending')
            finished_requests = Requests.objects.filter(user=user, status='finished')
            return render(request, 'profile.html', {'pending_requests': pending_requests,
                                                    'finished_requests': finished_requests})
        except jwt.InvalidTokenError:
            return HttpResponseForbidden("Invalid token")
    return redirect(reverse('login'))
