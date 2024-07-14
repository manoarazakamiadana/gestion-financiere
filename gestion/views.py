from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Gestion, Domain, RelationToParentDomain
from .forms import DomainForm

# Create your views here.


def index(request):
    return render(request, "home/index.html")

@login_required()
def domain(request):
    domains = Domain.objects.filter(gestion=Gestion.objects.get(owner=request.user), relation_to_parent_domain=None).order_by("-excepted_value")
    return render(request, "domain/index.html", {"domains": domains, "principal_domain": True})

@login_required()
def subdomain(request, id):
    domain = Domain.objects.get(id=id)
    relation = RelationToParentDomain.objects.get(parent_domain=domain)
    subdomains = Domain.objects.filter(gestion=Gestion.objects.get(owner=request.user), relation_to_parent_domain=relation).order_by("-excepted_value")
    return render(request, "domain/index.html", {"domains": subdomains, "domain": domain})

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
    return render(request, "domain/domain.html", {"form": form, "title": "Create new domain"})

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
    return render(request, "domain/domain.html", {"form": form, "title": "Create new subdomain for " + domain.name.lower()})

@login_required()
def edit_domain(request, id):
    domain = Domain.objects.get(id=id)
    if request.method == "POST":
        form = DomainForm(request.POST)
        if form.is_valid():
            domain.name = form.cleaned_data["name"]
            domain.excepted_value = form.cleaned_data["excepted_value"]
            domain.description = form.cleaned_data["description"]
            domain.save()
            return redirect("subdomain", id=domain.id)
    else:
        form = DomainForm(data={"name": domain.name, "description": domain.description, "excepted_value": domain.excepted_value})
    return render(request, "domain/domain.html", {"form": form, "title": "Editing the domain " + domain.name.lower()})