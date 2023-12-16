from django import forms
from .models import Album

class addalbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'