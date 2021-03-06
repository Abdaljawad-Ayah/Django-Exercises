from  django import forms
from .models import User
from  django.core import validators

class DjCrud (forms.ModelForm) : 
  class Meta:
    model = User
    fields = ['name', 'email', 'password']
    widgets = {
      'name' : forms.TextInput(attrs={'class' : 'form-control'}),
      'email': forms.EmailInput(attrs={'class' : 'form-control'}),
      'name' : forms.TextInput(attrs={'class' : 'form-control'}),
    }
    