from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=False, label='Your Name (required)')
    email = forms.EmailField(required=False, label='Email (optional)')
    message = forms.CharField(widget=forms.Textarea, label='Feedback')

    class Meta:
        model = Feedback
        fields = ['username', 'email', 'message']

class NotificationForm(forms.Form):
    title = forms.CharField(max_length=100, required=False, label='Title (optional)')
    message = forms.CharField(widget=forms.Textarea, label='broadcast message')

    class Meta:
        fields = ['title', 'message']