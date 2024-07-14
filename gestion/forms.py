from django import forms
from .models import Domain

class DomainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DomainForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
    class Meta:
        model = Domain
        fields = [
            "name",
            "description",
            "excepted_value"
        ]
        widgets = {
            "name" : forms.TextInput(attrs={'class': "form-control m-2", "placeholder": "Name of the domain"}),
            "description" : forms.TextInput(attrs={'class': "form-control m-2", "placeholder": "Description"}),
            "excepted_value" : forms.NumberInput(attrs={'class': "form-control m-2"})
        }
        