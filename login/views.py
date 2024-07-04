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
            response = redirect(reverse('home'))
            response.set_cookie('jwt', token, httponly=True)
            return response
        else:
            return render(request, 'login.html', {'form': form, 'error': form.errors})
    else:
        if request.COOKIES.get('jwt'):
            return redirect(reverse('home'))
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def home(request):
    jwt_token = request.COOKIES.get('jwt')
    if jwt_token:
        try:
            decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
            email = decoded_token['email']
            user = Users.objects.get(email=email)
            pending_requests = Requests.objects.filter(user=user, status='pending')

            non_pending_requests = Requests.objects.filter(user=user).exclude(status='pending').select_related('matched_user').order_by('-date')

            non_pending_requests_with_emails = [
                {
                    'request': req,
                    'matched_user_email': req.matched_user.email if req.matched_user else 'No matched user'
                }
                for req in non_pending_requests
            ]

            return render(request, 'home.html', {
                'first_name': user.first_name,
                'pending_requests': pending_requests,
                'non_pending_requests_with_emails': non_pending_requests_with_emails,
            })
        except jwt.InvalidTokenError:
            return HttpResponseForbidden("Invalid token")
    return redirect(reverse('login'))
