from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Users


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            Users.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect('success/')
        else:
            return render(request, 'signup.html', {'form': form, 'error': form.errors})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signup_success(request):
    return render(request, "success.html")
