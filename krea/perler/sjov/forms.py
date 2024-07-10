from django import forms
from django.forms import ModelForm
from .models import Anmeld 

class AnmeldForm(forms.ModelForm):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={'placeholder': 'ny meddelelse...'}))

  class Meta:
    model = Anmeld 
    fields = '__all__'