from celery import shared_task
from .models import Requests
from django.utils import timezone


@shared_task
def check_requests():
    now = timezone.localtime(timezone.now()).time()

    requests = Requests.objects.filter(
        time__gte=now,
        status='pending',
    )

    if not requests:
        print("No requests found matching the criteria.")
        return

    for request in requests:
        print(f"Processing request: {request.pk} from {request.pickup} to {request.destination} at {request.time}")

        count = Requests.objects.filter(
            pickup=request.pickup,
            destination=request.destination,
            time=request.time
        ).count()

        print(f"Found {count} requests matching pickup: {request.pickup}, destination: {request.destination}, time: {request.time}")

        if count >= 2:
            updated_count = Requests.objects.filter(
                pickup=request.pickup,
                destination=request.destination,
                time=request.time,
                status='pending',
            ).update(status="finished")
            print(f"Updated status to 'finished' for {updated_count} requests")
