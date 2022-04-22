from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Perfil

class CriarPerfilForm(UserCreationForm):
    
    email = forms.EmailField(required=True,
                             label="", 
                             widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True,
                               label="", 
                             widget=forms.TextInput(attrs={'placeholder':'Login'}))
    password1 = forms.CharField(
        required=True,
        label="",
        widget= forms.PasswordInput(attrs={'placeholder':'Senha'})
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget= forms.PasswordInput(attrs={'placeholder':'Senha'})
    )
    
    class Meta:
        model = User
        fields = ('email','username','password1','password2')
        
class EditarPerfilForm(forms.ModelForm):
    data_nasc = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Perfil
        exclude = ('usuario',)