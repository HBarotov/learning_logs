from django.urls import path, include

from .views import register

app_name = "accounts"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
]
