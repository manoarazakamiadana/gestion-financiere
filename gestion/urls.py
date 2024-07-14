from django.urls import path
from . import views

urlpatterns = [
    path("", views.domain, name="domain"),
    path("new/", views.new_domain, name="new-domain"),
    path("edit-domain/<int:id>", views.edit_domain, name="edit-domain"),
    path("view-subdomain/<int:id>", views.subdomain, name="subdomain"),
    path("new-subdomain/<int:id>", views.new_subdomain, name="new-subdomain"),
]