from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import FeedbackForm
from .models import Notification

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

@login_required
def notifications(request):
    notifications_obj = Notification.objects.filter(user=request.user).order_by('-created_at')
    context = {'notifications': notifications_obj}
    for  obj in notifications_obj:
        obj.is_read = True
        obj.save()
    return render(request, 'user_app/notifications.html', context)

def feedback_ok(request):
    return render(request, 'user_app/feedback_ok.html')


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_obj = form.save(commit=False)
            if request.user.is_authenticated:
                feedback_obj.username = request.user.username
            feedback_obj.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('learning_logs_app:feedback_ok')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    else:
        if request.user.is_authenticated:
            initial = {'username': request.user.username}
            form = FeedbackForm(initial=initial)
            form.fields['username'].disabled = True
        else:
            form = FeedbackForm()
            form.fields['username'].required = True

    context = {'form': form}
    return render(request, 'user_app/feedback.html', context)