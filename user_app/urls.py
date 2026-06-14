from django.urls import path, include
from . import views

app_name = "user_app"

urlpatterns = [
    path("logout/", views.logout_get, name="logout"),
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]