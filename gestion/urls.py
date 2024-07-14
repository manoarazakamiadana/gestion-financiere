from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("domain/", views.domain, name="domain"),
    path("domain/new", views.new_domain, name="new-domain")
]