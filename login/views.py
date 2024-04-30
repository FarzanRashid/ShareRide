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


def login_success(request):
    jwt_token = request.COOKIES.get('jwt')
    if jwt_token:
        try:
            decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
            email = decoded_token['email']
            user = Users.objects.get(email=email)
            first_name = user.first_name
            last_name = user.last_name
            return render(request, 'login_success.html', {'email': email,
                                                          'first_name': first_name,
                                                          'last_name': last_name})
        except jwt.ExpiredSignatureError:
            return HttpResponseForbidden('Token expired')
        except jwt.DecodeError:
            return HttpResponseForbidden('Error decoding token')
        except jwt.InvalidTokenError:
            return HttpResponseForbidden('Invalid Token')
    else:
        return redirect('login')
