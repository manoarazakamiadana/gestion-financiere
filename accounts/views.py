from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm
from gestion.models import Gestion, DateInterval

# Create your views here.

def login_view(request):
    if request.user.username:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            form = LoginForm()
            return render(request, "accounts/login.html", {"form": form})
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def signup(request):
    if request.user.username:
        return redirect("home")
    if request.method == "POST":
        form = SignupForm(request.POST)
        if request.POST.get("password") == request.POST.get("password_confirmation"):
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data.get("password"))
                user.save()
                user_gestion = Gestion()
                user_gestion.owner = user
                user_gestion.save()
                user_date_suivi = DateInterval()
                user_date_suivi.user = user
                user_date_suivi.save()
                return redirect("login")
        else:
            return render(request, "accounts/signup.html", {"form": form, "message": "Verifiez votre mot de passe"})
    else:
        form = SignupForm()
    
    return render(request, "accounts/signup.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')