import jwt
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from .forms import LocationForm
from .models import Requests
from signup.models import Users


def ride_request(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            jwt_token = request.COOKIES.get('jwt')
            decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
            email = decoded_token['email']
            user = Users.objects.get(email=email)
            Requests.objects.create(
                pickup=form.cleaned_data['pickup'],
                destination=form.cleaned_data['destination'],
                time=form.cleaned_data['time'],
                user=user,
            )
            return HttpResponse("Request successfully created")
        return HttpResponse("Request failed")
    else:
        if request.COOKIES.get('jwt'):
            form = LocationForm()
            return render(request, 'request.html', {'form': form})
        return redirect('login')
