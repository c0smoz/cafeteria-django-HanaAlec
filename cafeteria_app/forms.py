from django import forms
from .models import User  # le modèle "User" (anciennement Student)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'credit']