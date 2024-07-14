from typing import Iterable
from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import CustomUser

# Create your models here.

class Gestion(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=False)

class Domain(models.Model):
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(null=True)
    relation_to_parent_domain = models.ForeignKey("RelationToParentDomain", on_delete=models.SET_NULL, null=True)
    excepted_value = models.FloatField(default=0)

class RelationToParentDomain(models.Model):
    parent_domain = models.OneToOneField(Domain, on_delete=models.CASCADE, null=False)

class Transaction(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(null=True)
    value = models.FloatField(default=0)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True)
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE, null=False)
    depense = models.BooleanField(default=True, null=False)