from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a new user."""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")

    context = {"form": form}
    return render(request, "registration/register.html", context)
