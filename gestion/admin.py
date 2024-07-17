from django.contrib import admin
from .models import Gestion, Domain, RelationToParentDomain, Transaction, DateInterval

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
        "excepted_revenu",
        "excepted_depense",
        "gestion"
    )

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "value",
        "domain",
        "date",
        "depense"
    )

@admin.register(DateInterval)
class DateIntervalAdmin(admin.ModelAdmin):
    list_display = (
        "start",
        "end"
    )