from django import forms
from datetime import datetime, timedelta


def get_times():
    now = datetime.now()
    times = []

    if now.minute < 30:
        next_half_hour = now.replace(minute=30, second=0, microsecond=0)
    else:
        next_half_hour = (now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1))

    current_time = next_half_hour

    end_of_day = now.replace(hour=23, minute=30, second=0, microsecond=0)
    while current_time <= end_of_day:
        time_str = current_time.strftime('%H:%M')
        times.append((time_str, time_str))
        current_time += timedelta(minutes=30)

    return times


class LocationForm(forms.Form):
    locations = [('Dhanmondi', 'Dhanmondi'),
                 ('Banani', 'Banani'),
                 ('Gulshan', 'Gulshan'),
                 ]

    pickup = forms.ChoiceField(choices=locations, label="Pickup")
    destination = forms.ChoiceField(choices=locations, label="Destination")
    time = forms.ChoiceField(choices=[], label="Time")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].choices = get_times()
