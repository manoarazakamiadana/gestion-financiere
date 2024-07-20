from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("log-out", views.logout_view, name="logout"),
    path("sign-up/", views.signup, name="signup")
]