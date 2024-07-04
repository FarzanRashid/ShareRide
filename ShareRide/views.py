import jwt
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings

from requestride.models import Requests
from signup.models import Users


def logout(request):
    response = redirect(reverse('login'))
    response.delete_cookie('jwt')
    return response


def cancel_request(request, request_id):
    jwt_token = request.COOKIES.get('jwt')
    if jwt_token:
        try:
            decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
            email = decoded_token['email']
            user = Users.objects.get(email=email)

            request_to_cancel = get_object_or_404(Requests, id=request_id, user=user, status='pending')
            request_to_cancel.status = 'Cancelled'
            request_to_cancel.save()

            return redirect(reverse('home'))
        except jwt.InvalidTokenError:
            return HttpResponseForbidden("Invalid token")
    return redirect(reverse('login'))
