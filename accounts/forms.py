from django import forms
from .models import CustomUser

class SignupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control m-2'
            visible.field.widget.attrs['autocomplete'] = "off"
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    # email = forms.EmailField(required=False)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password confirmation"}))
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
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "username" : forms.TextInput(attrs={"placeholder": "Username"}),
            "first_name" : forms.TextInput(attrs={"placeholder": "First name"}),
            "last_name" : forms.TextInput(attrs={"placeholder": "Last name"})
        }

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control m-2'
            visible.field.widget.attrs['autocomplete'] = "off"
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}), required=True)