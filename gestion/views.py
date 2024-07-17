from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Gestion, Domain, RelationToParentDomain, Transaction
from .forms import DomainForm, TransactionForm, SpeedTransactionForm
from datetime import date

# Create your views here.


def index(request):
    return render(request, "home/index.html")

@login_required()
def domain(request):
    domains = Domain.objects.filter(gestion=Gestion.objects.get(owner=request.user), relation_to_parent_domain=None).order_by("name")
    transactions = Transaction.objects.filter(gestion=Gestion.objects.get(owner=request.user))
    depense = 0
    revenu = 0
    for transaction in transactions:
        if transaction.depense:
            depense += transaction.value
        else:
            revenu += transaction.value
    solde = revenu - depense
    return render(request, "domain/index.html", {"domains": domains, "principal_domain": True, "title": "Domain", "solde": solde, "depense": depense, "revenu": revenu})

@login_required()
def subdomain(request, id):
    domain = Domain.objects.get(id=id)
    relation = RelationToParentDomain.objects.get(parent_domain=domain)
    subdomains = Domain.objects.filter(gestion=Gestion.objects.get(owner=request.user), relation_to_parent_domain=relation).order_by("name")
    return render(request, "domain/index.html", {"domains": subdomains, "domain": domain, "title": "Subdomain"})

@login_required()
def new_domain(request):
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            domain = form.save(commit=False)
            domain.gestion = Gestion.objects.get(owner=request.user)
            domain.save()
            RelationToParentDomain(parent_domain=domain).save()
            return redirect("domain")
    else:
        form = DomainForm()
    return render(request, "domain/domain.html", {"form": form, "title": "Create new domain", "action": "New"})

@login_required()
def new_subdomain(request, id):
    domain = Domain.objects.get(id=id)
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            subdomain = form.save(commit=False)
            subdomain.gestion = Gestion.objects.get(owner=request.user)
            subdomain.relation_to_parent_domain = RelationToParentDomain.objects.get(parent_domain=domain)
            subdomain.save()
            RelationToParentDomain(parent_domain=subdomain).save()
            return redirect("subdomain", id=domain.id)
    else:
        form = DomainForm()
    return render(request, "domain/domain.html", {"form": form, "title": "Create new subdomain for " + domain.name.lower(), "action": "New"})

@login_required()
def edit_domain(request, id):
    domain = Domain.objects.get(id=id)
    if request.method == "POST":
        form = DomainForm(request.POST)
        if form.is_valid():
            domain.name = form.cleaned_data["name"]
            domain.excepted_depense = form.cleaned_data["excepted_depense"]
            domain.excepted_revenu = form.cleaned_data["excepted_revenu"]
            domain.description = form.cleaned_data["description"]
            domain.save()
            return redirect("subdomain", id=domain.id)
    else:
        form = DomainForm(data={"name": domain.name, "description": domain.description, "excepted_depense": domain.excepted_depense, "excepted_revenu": domain.excepted_revenu})
    return render(request, "domain/domain.html", {"form": form, "title": "Editing the domain " + domain.name.lower(), "action": "Edit"})

@login_required()
def new_transaction_domain(request, id):
    domain = Domain.objects.get(id=id)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.gestion = Gestion.objects.get(owner=request.user)
            transaction.domain = domain
            transaction.save()
            return redirect("transaction", id=domain.id)
    else:
        form = TransactionForm(data={"date": date.today(), "depense": True})
    return render(request, "transaction/transaction.html", {"form": form, "title": "New transaction", "action": "New transaction for " + domain.name.lower()})

@login_required()
def transaction(request, id):
    domain = Domain.objects.get(id=id)
    transaction = Transaction.objects.filter(domain=domain)
    return render(request, "transaction/index.html", {"domain":domain, "transactions":transaction})

@login_required()
def edit_transaction(request, id):
    transaction = Transaction.objects.get(id=id)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction.name = form.cleaned_data["name"]
            transaction.value = form.cleaned_data["value"]
            transaction.description = form.cleaned_data["description"]
            transaction.depense = form.cleaned_data["depense"]
            transaction.save()
            return redirect("transaction", id=transaction.domain.pk)
    else:
        form = TransactionForm(data={"name": transaction.name, "description": transaction.description, "value": transaction.value, "depense": transaction.depense, "date": transaction.date})
    return render(request, "transaction/transaction.html", {"form": form, "title": "Edit transaction", "action": "Editing the transaction " + transaction.name.lower()})

def quick_transaction(request):
    if request.method == "POST":
        form = SpeedTransactionForm(request.POST, user=request.user)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.gestion = Gestion.objects.get(owner=request.user)
            transaction.save()
            return redirect("quick-transaction")
    else:
        form = SpeedTransactionForm(user=request.user ,data={"date": date.today(), "depense": True})
    return render(request, "transaction/transaction.html", {"form": form, "title": "New transaction", "action": "New transaction"})