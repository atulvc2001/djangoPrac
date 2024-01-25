from django import forms
from app1.models import registration

class rgform(forms.ModelForm):
    class Meta:
        model=registration
        fields=["username","mob","email","password","last_name","first_name"]