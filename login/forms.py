from django import forms
from signup.models import Users


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(), label='Password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        email = cleaned_data.get('email')
        if Users.objects.filter(email=email).exists():
            user = Users.objects.get(email=email)
            if user.password != password:
                raise forms.ValidationError("Incorrect E-mail or password")
        else:
            raise forms.ValidationError("Incorrect E-mail or password")
