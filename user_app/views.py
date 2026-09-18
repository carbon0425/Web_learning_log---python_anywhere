from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MyUserCreationForm
from django.contrib import messages
from .forms import FeedbackForm
from .models import Notification
from .models import User
from django.db import models
from django.shortcuts import get_object_or_404
from . import actions
from .forms import FriendApplyForm

def logout_get(request):
    """Logs out the user and renders the logout confirmation page."""
    logout(request)
    return render(request, "registration/logout.html")

def register(request):
    """Handles user registration."""
    if request.method != "POST":
        form = MyUserCreationForm()
    else:
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            welcome_message = """
            Welcome to Learning Log — we're so glad you're here!

            This is your personal space to capture ideas, track progress, and reflect on everything you're learning.

            What you can do:
            - Create topics to organise your learning
            - Add entries to record your thoughts, notes, or questions
            - Manage your entries — when you view a topic, each of your entries has a three-dot menu (...) in the top-right corner. Click it to Edit or Delete that entry.
            - Use the navigation bar to browse your Topics, send Feedback, or check Notifications
            - Everything you write stays private to you — safe and simple

            If you ever need help, check the Topics page or use the Feedback form.

            Start your first topic today — happy learning!

            Have a good time learning,
            The Learning Log Team
            """
            login(request, user)
            Notification.objects.create(
                user=user,
                title="Welcome to learning log",
                message=welcome_message
                )
            return redirect("learning_logs_app:index")  # Redirect to a home page or dashboard after registration

    return render(request, "registration/register.html", {"form": form})

@login_required
def notifications(request):
    notifications_obj = Notification.objects.filter(user=request.user).order_by('-created_at')
    status_list = ["PENDING", "ACCEPTED", "REJECTED"]
    for noti in notifications_obj:
        if noti.action_type == "apply_check":
            noti_apply = get_object_or_404(Notification, id=noti.action.apply_obj)
            noti.to = get_object_or_404(User, id=noti_apply.action.to).username
            noti.status = status_list[noti_apply.action.status]
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
            return redirect('user_app:feedback_ok')
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


def search_users(request):
    query = request.GET.get('user_key', '').strip()

    results = []
    if query:
        results = User.objects.filter(
            models.Q(username__icontains=query)
        ).exclude(id=request.user.id)
    context = {'query': query, 'results': results}
    return render(request, 'user_app/search_users.html', context)


def add_user(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    apply = f'''Dear {to_user.username},

                I hope this message finds you well.

                My name is {request.user.username}, and I've been following your learning journey on Learning Log.

                I believe that learning becomes richer when we share it with others. That's why I'm writing to invite you to connect as learning partners on this platform.

                If you accept, we'll be able to:

                - View each other's public and friend‑only notes

                - Collaborate on shared topics and book studies

                - Exchange feedback and insights in a private, focused space

                Please know that I fully respect your decision, whether you choose to accept or not. There is no pressure — only an open invitation.

                You can respond by clicking the button below:

                I hope you'll consider it. Either way, I wish you all the best in your learning journey.

                Warm regards,
                {request.user.username},
                Learning Log
            '''
    if request.method == "POST":
        form = FriendApplyForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            _noti = Notification.objects.create(
                        user=to_user,
                        title=f"Friend Apply from {request.user.username}",
                        message=message,
                        action_type="friend_apply",
                        action_data={
                                "sender": request.user.id,
                                "to": to_user.id,
                                "status": actions.Status.PENDING.value
                            }
                    )
            Notification.objects.create(
                        user=request.user,
                        title="Your Friend Apply",
                        message=Notification.STATUS_MESSAGES[0],
                        action_type="apply_check",
                        action_data={"apply_obj": _noti.id}
                    )
            return redirect("user_app:apply_message", type=1)

    else:
        _1 = Notification.objects.filter(
                    user=to_user,
                    action_type='friend_apply',
                    action_data__sender=request.user.id,
                ).exists()
        _2 = Notification.objects.filter(
                    user=request.user,
                    action_type='friend_apply',
                    action_data__sender=to_user.id,
                ).exists()
        if  not _1 and not _2:
            form = FriendApplyForm(initial={"message": apply})
        else:
            return redirect("user_app:apply_message", type=0)

    context = {'form': form}
    return render(request, 'user_app/send_apply.html', context)


def apply_message(request, type):
    return render(request, 'user_app/apply_message.html', {"type": type})












