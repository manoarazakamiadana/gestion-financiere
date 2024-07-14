from django.contrib import admin
from .models import Gestion, Domain, RelationToParentDomain, Transaction

# Register your models here.

@admin.register(Gestion)
class GestionAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
    )

@admin.register(RelationToParentDomain)
class RelationToParentDomainAdmin(admin.ModelAdmin):
    list_display = (
        "parent_domain",
    )

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "relation_to_parent_domain",
        "excepted_value",
        "gestion"
    )

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "value",
        "domain"
    )