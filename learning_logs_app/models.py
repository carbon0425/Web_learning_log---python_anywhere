from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text

class ErrorLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField(default=500)
    exception_type = models.CharField(max_length=200, blank=True, null=True)
    exception_message = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.exception_type} at {self.path} ({self.status}, {self.timestamp})"

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, default="Notification")
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
