from django import forms
from .models import Lead
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['LeadType', 'name', 'email', 'Mobile' ]

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        