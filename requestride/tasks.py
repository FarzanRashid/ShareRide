from celery import shared_task
from .models import Requests
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def check_requests():
    now = timezone.localtime(timezone.now()).time()

    pending_requests = Requests.objects.filter(
        time__gte=now,
        status='pending',
    )

    if not pending_requests:
        print("No pending requests found.")
        return

    for request in pending_requests:
        print(
            f"Processing request: {request.pk} from {request.pickup} to {request.destination} at {request.time}")

        matching_requests = Requests.objects.filter(
            pickup=request.pickup,
            destination=request.destination,
            time=request.time,
            status='pending'
        ).exclude(user=request.user).order_by('created_at')

        if matching_requests.exists():
            matched_request = matching_requests.first()
            request.status = 'Matched'
            request.matched_user = matched_request.user
            request.save()

            matched_request.status = 'Matched'
            matched_request.matched_user = request.user
            matched_request.save()

            print(
                f"Requests {request.pk} and {matched_request.pk} are matched and updated to "
                f"'Matched' status.")

            send_mail(
                subject='Your request has been matched!',
                message=f'Your request from {request.pickup} to {request.destination} at {request.time} has been matched with another user. Their email is {matched_request.user.email}.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=False,
            )

            send_mail(
                subject='Your request has been matched!',
                message=f'Your request from {matched_request.pickup} to {matched_request.destination} at {matched_request.time} has been matched with another user. Their email is {request.user.email}.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[matched_request.user.email],
                fail_silently=False,
            )


@shared_task
def check_old_pending_requests():
    now = timezone.localtime(timezone.now())
    old_pending_requests = Requests.objects.filter(
        date__lt=now.date(),
        status='pending'
    ) | Requests.objects.filter(
        date=now.date(),
        time__lt=now.time(),
        status='pending'
    )
    if not old_pending_requests.exists():
        print("No old pending requests found.")
        return

    for request in old_pending_requests:
        print(
            f"Updating request: {request.pk} from {request.pickup} to {request.destination} at {request.date} {request.time} to 'Unmatched'")
        request.status = 'Unmatched'
        request.save()
        print(f"Request {request.pk} status updated to 'Unmatched'.")
