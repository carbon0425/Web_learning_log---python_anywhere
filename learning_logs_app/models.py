from django.conf import settings
from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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


