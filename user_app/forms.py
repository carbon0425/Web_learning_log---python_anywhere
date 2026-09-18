from django import forms
from .models import Feedback
from .models import User
from django.contrib.auth.forms import UserCreationForm

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

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class FriendApplyForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='friend apply message')

    class Meta:
        fields = ['message']