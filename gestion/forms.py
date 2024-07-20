from django import forms
from .models import Domain, Transaction, Gestion, DateInterval

class DomainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DomainForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control m-2'
            visible.field.widget.attrs['autocomplete'] = "off"
    class Meta:
        model = Domain
        fields = [
            "name",
            "description",
            "excepted_depense",
            "excepted_revenu"
        ]
        widgets = {
            "name" : forms.TextInput(attrs={"placeholder": "Name of the domain"}),
            "description" : forms.TextInput(attrs={"placeholder": "Description"}),
        }

class TransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['depense'].label = "Type"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control m-2'
            visible.field.widget.attrs['autocomplete'] = "off"
        self.fields['depense'].widget.attrs['class'] = "m-2"

    class Meta:
        model = Transaction
        fields = [
            "name",
            "description",
            "value",
            "depense",
            "date"
        ]
        widgets = {
            "name" : forms.TextInput(attrs={"placeholder": "Name of the transaction"}),
            "description" : forms.TextInput(attrs={"placeholder": "Description"}),
            "value" : forms.NumberInput(attrs={"placeholder": "Transaction value"}),
            "depense": forms.RadioSelect(choices=[(True, "Depense"), (False, "Revenu")]),
            "date": forms.DateInput(attrs={"type": "date", "placeholder": "dd/mm/yyyy"})
        }

class SpeedTransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(SpeedTransactionForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['depense'].label = "Type"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control m-2'
            visible.field.widget.attrs['autocomplete'] = "off"
        self.fields['depense'].widget.attrs['class'] = "m-2"
        self.fields['domain'].queryset = Domain.objects.filter(gestion=Gestion.objects.get(owner=user)).order_by("name")
    class Meta:
        model = Transaction
        fields = [
            "name",
            "description",
            "value",
            "depense",
            "date",
            "domain"
        ]
        widgets = {
            "name" : forms.TextInput(attrs={"placeholder": "Name of the transaction"}),
            "description" : forms.TextInput(attrs={"placeholder": "Description"}),
            "value" : forms.NumberInput(attrs={"placeholder": "Transaction value"}),
            "depense": forms.RadioSelect(choices=[(True, "Depense"), (False, "Revenu")]),
            "date": forms.DateInput(attrs={"type": "date"}),
            "domain": forms.Select()
        }

class DateIntervalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DateIntervalForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control m-2'
            visible.field.widget.attrs['autocomplete'] = "off"
    class Meta:
        model = DateInterval
        fields = [
            "start",
            "end"
        ]
        widgets = {
            "start": forms.DateInput(attrs={"type": "date"}),
            "end": forms.DateInput(attrs={"type": "date"}),
        }