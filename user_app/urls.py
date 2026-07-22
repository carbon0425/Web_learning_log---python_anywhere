from django.urls import path, include
from . import views

app_name = "user_app"

urlpatterns = [
    path("logout/", views.logout_get, name="logout"),
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    # Page for viewing feedback
    path('feedback/', views.feedback, name='feedback'),
    # Page for submitting feedback
    path('feedback_ok/', views.feedback_ok, name='feedback_ok'),
    # Page for showing notifications
    path('notifications/', views.notifications, name='notifications'),
]