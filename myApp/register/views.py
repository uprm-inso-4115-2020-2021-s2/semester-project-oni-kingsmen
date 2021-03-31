from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(response, f'Account created for {username}!')
            return redirect("cooking-home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
