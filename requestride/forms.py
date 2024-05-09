from django import forms


class LocationForm(forms.Form):
    locations = [('Dhanmondi', 'Dhanmondi'),
                 ('Banani', 'Banani'),
                 ('Gulshan', 'Gulshan'),
                 ]
    times = [(f"{h:02}:{m:02}", f"{h:02}:{m:02}") for h in range(0, 24) for m in range(0, 60, 30)]

    pickup = forms.ChoiceField(choices=locations, label="Pickup")
    destination = forms.ChoiceField(choices=locations, label="Destination")
    time = forms.ChoiceField(choices=times, label="Time")
