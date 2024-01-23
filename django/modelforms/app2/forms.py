from django import forms
from app2.models import movie

class movieform(forms.ModelForm):
    class Meta:
        model=movie
        fields="__all__"