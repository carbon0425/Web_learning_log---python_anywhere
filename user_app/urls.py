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
    # Page for searching users
    path('search_users/', views.search_users, name='search_users'),
    # Page for sending applies
    path('send_apply/<int:user_id>', views.add_user, name='send_apply'),
    # Page for apply messages
    path('apply_message/<int:type>', views.apply_message, name='apply_message'),
]