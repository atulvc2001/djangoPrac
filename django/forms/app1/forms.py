from django import forms

class customerform(forms.Form):
    cname = forms.CharField(widget=forms.TextInput())
    mob = forms.IntegerField(widget=forms.NumberInput())
    addrs = forms.CharField(widget=forms.TextInput())
    cdob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    cdobtime = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))