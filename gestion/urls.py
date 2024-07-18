from django.urls import path
from . import views

urlpatterns = [
    # path("custom/", views.custom),
    path("", views.index, name="home"),
    path("domain/", views.domain, name="domain"),
    path("domain/tree", views.domain_tree, name="domain-tree"),
    path("domain/new/", views.new_domain, name="new-domain"),
    path("transaction/<int:id>", views.transaction, name="transaction"),
    path("domain/view-subdomain/<int:id>", views.subdomain, name="subdomain"),
    path("domain/edit-domain/<int:id>", views.edit_domain, name="edit-domain"),
    path("period-to-monitor/", views.period_to_monitor, name="period-to-monitor"),
    path("quick-transaction/", views.quick_transaction, name="quick-transaction"),
    path("domain/new-subdomain/<int:id>", views.new_subdomain, name="new-subdomain"),
    path("transaction/edit-transaction/<int:id>", views.edit_transaction, name="edit-transaction"),
    path("transaction/new-transaction/<int:id>", views.new_transaction_domain, name="new-transaction-domain"),
]