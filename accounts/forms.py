from django import forms
from .models import CustomUser

class SignupForm(forms.ModelForm):
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    # email = forms.EmailField(required=False)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control m-2", "placeholder": "Password confirmation"}))
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        ]
        widgets = {
            "password": forms.PasswordInput(attrs={'class': "form-control m-2", "placeholder": "Password"}),
            "email": forms.EmailInput(attrs={'class': "form-control m-2", "placeholder": "Email"}),
            "username" : forms.TextInput(attrs={'class': "form-control m-2", "placeholder": "Username"}),
            "first_name" : forms.TextInput(attrs={'class': "form-control m-2", "placeholder": "First name"}),
            "last_name" : forms.TextInput(attrs={'class': "form-control m-2", "placeholder": "Last name"})
        }

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control m-2", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control m-2", "placeholder": "Password"}), required=True)