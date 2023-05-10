from django.forms import ModelForm
from .models import Employee
from django import forms
from django.core.validators import MaxValueValidator
from datetime import date
from django.utils.timezone import now

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name','department','dateOfBirth','dateOfJoin','post','address','city','country','zipCode','state','is_active','on_leave']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'post':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'zipCode':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),

            'dateOfBirth': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'dateOfJoin': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
        }
    
    
     