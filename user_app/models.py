from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from . import actions

class User(AbstractUser):
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __str__(self):
        return self.username

class Feedback(models.Model):
    """Feedback model to store user feedback."""
    username = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.username} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

class Notification(models.Model):
    """Notification model to store user notifications."""
    ACTION_CHOICES = [
        ("normal", "notification"),
        ("friend_apply", "friend_apply"),
        ("apply_check", "apply_check"),
    ]
    STATUS_MESSAGES = [
        "Your friend request has been sent successfully. The recipient will be notified and we will inform you once a response is received.",
        "Your friend request has been accepted. You are now connected and can start sharing learning content with each other.",
        "Your friend request has been declined. We respect the recipient’s decision and encourage you to continue exploring other learning connections.",
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, default="Notification")
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    action_type = models.CharField(max_length=25, default="normal", choices=ACTION_CHOICES)
    action_data = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    @property
    def action(self):
        if self.action_type in actions.ACTION_MAP.keys():
            try:
                return actions.ACTION_MAP[self.action_type](**self.action_data)
            except (TypeError, KeyError):
                pass
        return None