from django import forms
from .models import Donee,Donor,Item,Requirement
from passwords.validators import (DictionaryValidator, LengthValidator, ComplexityValidator)

class DonorForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Donor
        fields="__all__"

class DoneeForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Donee
        fields="__all__"

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields="__all__"

class RequirementForm(forms.ModelForm):
    class Meta:
        model=Requirement
        fields="__all__"
