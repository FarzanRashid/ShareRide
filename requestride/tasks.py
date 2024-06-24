from celery import shared_task
from .models import Requests
from django.utils import timezone


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
        ).exclude(user=request.user)

        if matching_requests.exists():
            matched_request = matching_requests.first()
            request.status = 'finished'
            request.matched_user = matched_request.user
            request.save()

            matched_request.status = 'finished'
            matched_request.matched_user = request.user
            matched_request.save()

            print(
                f"Requests {request.pk} and {matched_request.pk} are matched and updated to 'finished' status.")
