from typing import Iterable
from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import CustomUser

# Create your models here.

class Gestion(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=False)

class Domain(models.Model):

    def __str__(self):
        return self.name

    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(null=True)
    relation_to_parent_domain = models.ForeignKey("RelationToParentDomain", on_delete=models.SET_NULL, null=True)
    excepted_depense = models.FloatField(default=0)
    excepted_revenu = models.FloatField(default=0)

    def get_depense_total(self):
        depense_total = 0
        transactions = Transaction.objects.filter(domain=self)
        depense_total = sum(transaction.value if transaction.depense else 0 for transaction in transactions)
        relation_to_me = RelationToParentDomain.objects.get(parent_domain=self.id)
        subdomains = Domain.objects.filter(relation_to_parent_domain=relation_to_me)
        depense_total += sum(subdomain.get_depense_total() for subdomain in subdomains)
        return depense_total

    def get_revenu_total(self):
        revenu_total = 0
        transactions = Transaction.objects.filter(domain=self)
        revenu_total = sum(transaction.value if not transaction.depense else 0 for transaction in transactions)
        relation_to_me = RelationToParentDomain.objects.get(parent_domain=self.id)
        subdomains = Domain.objects.filter(relation_to_parent_domain=relation_to_me)
        revenu_total += sum(subdomain.get_revenu_total() for subdomain in subdomains)
        return revenu_total
    
    def get_solde(self):
        return self.get_revenu_total() - self.get_depense_total()
    
    # ampiana oe get arbre

class RelationToParentDomain(models.Model):
    parent_domain = models.OneToOneField(Domain, on_delete=models.CASCADE, null=False)

class Transaction(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(null=True)
    value = models.FloatField(default=0)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True)
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE, null=False)
    depense = models.BooleanField(default=True, null=False)
    date = models.DateField(null=False)

# ampiana class oe date le affihcer-na (ohatra oe mois de juillet)

class DateInterval(models.Model):
    start = models.DateField()
    end = models.DateField()