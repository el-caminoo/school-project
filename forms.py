from django import forms
from .models import *


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=33, widget=forms.TextInput(attrs={
        'class': 'input100'
    }))

    last_name = forms.CharField(max_length=33, widget=forms.TextInput(attrs={
        'class': 'input100'
    }))

    DOB = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'input100',
        'type': 'date'
    }))

    country = forms.ChoiceField(choices=Company.COUNTRY, widget=forms.Select(attrs={
        'class': 'input100',
        'type': 'option'
    }))

    state = forms.CharField(max_length=33, widget=forms.TextInput(attrs={
        'class': 'input100'
    }))

    city = forms.CharField(max_length=33, widget=forms.TextInput(attrs={
        'class': 'input100'
    }))

    sex = forms.ChoiceField(choices=Company.SEX, widget=forms.Select(attrs={
        'class': 'input100',
        'type': 'option'
    }))

    use_duration = forms.ChoiceField(choices=Company.DURATION, widget=forms.Select(attrs={
        'class': 'input100',
        'type': 'option'
    }))

    product_rating = forms.ChoiceField(choices=Company.SCALE, widget=forms.Select(attrs={
        'class': 'input100',
        'type': 'option'
    }))

    cost_quality = forms.ChoiceField(choices=Company.COST_QUALITY, widget=forms.Select(attrs={
        'class': 'input100',
        'type': 'option'
    }))

    continuous_use = forms.ChoiceField(choices=Company.CONTINUOUS_USE, widget=forms.Select(attrs={
        'class': 'input100',
        'type': 'option'
    }))

    class Meta:
        model = Company
        fields = ['first_name', 'last_name', 'DOB', 'country', 'state', 'sex', 'city', 'continuous_use', 'cost_quality',
                  'product_rating', 'use_duration']

