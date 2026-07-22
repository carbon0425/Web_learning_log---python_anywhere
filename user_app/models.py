from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, default="Notification")
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"