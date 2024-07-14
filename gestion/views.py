from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Gestion, Domain
from .forms import DomainForm

# Create your views here.


def index(request):
    return render(request, "home/index.html")

@login_required()
def domain(request):
    domains = Domain.objects.filter(gestion=Gestion.objects.get(owner=request.user), relation_to_parent_domain=None).order_by("-excepted_value")
    return render(request, "domain/index.html", {"domains": domains})

@login_required()
def new_domain(request):
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            domain = form.save(commit=False)
            domain.gestion = Gestion.objects.get(owner=request.user)
            domain.save()
            return redirect("domain")
    else:
        form = DomainForm()
    return render(request, "domain/domain.html", {"form": form, "title": "Create new domain"})