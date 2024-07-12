from django import forms
from .models import CustomUser

class SignupForm(forms.ModelForm):
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    # email = forms.EmailField(required=False)
    password_confirmation = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        ]
        widgets = {"password": forms.PasswordInput(), "email": forms.EmailInput()}

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)