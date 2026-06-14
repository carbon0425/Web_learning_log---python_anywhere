from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def logout_get(request):
    """Logs out the user and renders the logout confirmation page."""
    logout(request)
    return render(request, "registration/logout.html")

def register(request):
    """Handles user registration."""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("learning_logs_app:index")  # Redirect to a home page or dashboard after registration

    return render(request, "registration/register.html", {"form": form})