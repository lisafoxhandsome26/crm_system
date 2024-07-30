import datetime
import re

from django import forms
from django.core.exceptions import ValidationError
from .models import Contract, Product, Advertisement, Lead, Customer
from django.contrib.auth.forms import AuthenticationForm

attr: dict = {'class': 'form-control'}


def validate_mobile_number(value: str) -> str:
    if not re.match(r'^[+][7-9]\d{10}$', value):
        raise ValidationError(
            'Number phone must have 11 digits and begin from +7, +8 or +9.'
        )
    return value


def validate_name(value: str) -> str:
    if not re.match(r'^[а-яА-Я\s]+$', value):
        raise ValidationError('Name must have only letters')
    return value


def validate_dates(one_date):
    now = datetime.date.today()
    if one_date < now:
        raise ValidationError("The dates were indicated incorrectly")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "cost"]
        widgets = {
            'name': forms.TextInput(attrs=attr),
            'description': forms.Textarea(attrs=attr),
            'cost': forms.NumberInput(attrs=attr)
        }


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ["name", "budget", "ads_product"]
        widgets = {
            'name': forms.TextInput(attrs=attr),
            'budget': forms.NumberInput(attrs=attr),
            'ads_product': forms.Select(attrs=attr)
        }


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["last_name", "first_name", "phone", "email", "ads"]
        widgets = {
            'last_name': forms.TextInput(attrs=attr),
            'first_name': forms.TextInput(attrs=attr),
            'phone': forms.TextInput(attrs=attr),
            'email': forms.EmailInput(attrs=attr),
            'ads': forms.Select(attrs=attr)
        }

    def clean_last_name(self):
        name = self.cleaned_data.get('last_name')
        return validate_name(name)

    def clean_first_name(self):
        name = self.cleaned_data.get('first_name')
        return validate_name(name)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        return validate_mobile_number(phone)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["lead", ]
        widgets = {
            'lead': forms.Select(attrs=attr),
        }


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ["name", "cost", "start_date", "end_date", "product", "customer", "contract"]
        widgets = {
            'name': forms.TextInput(attrs=attr),
            'cost': forms.NumberInput(attrs=attr),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': attr['class']}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': attr['class']}),
            'contract': forms.FileInput(attrs=attr),
            'product': forms.Select(attrs=attr),
            'customer': forms.Select(attrs=attr)
        }

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        validate_dates(start_date)
        return start_date

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        validate_dates(end_date)
        return end_date

    def clean_contract(self):
        contract = self.cleaned_data.get('contract')
        if contract.name.endswith(".doc") or contract.name.endswith(".docx"):
            return contract
        else:
            raise ValidationError('The file must have an extension ".doc" or ".docx"')


class AuthForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs=attr))

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs=attr))
