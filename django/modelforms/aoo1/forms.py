from django import forms
from aoo1.models import emp


class empform(forms.ModelForm):
    class Meta: 
        model=emp
        # fields="__all__"
        fields=["eno","ename"]
