from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label="Last Name")
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(), label='Password')
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput(),
                                       label='Confirm Password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data
