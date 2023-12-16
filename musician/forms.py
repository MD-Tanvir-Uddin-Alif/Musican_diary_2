from django import forms
from .models import Musician
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUP(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    instrument = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','phone','instrument','email'] 

class AddMusician(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'