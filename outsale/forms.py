from django import forms
from .models import Outsale

class SaleForm(forms.Form):
    sdate = forms.DateField()
    edate = forms.DateField()

class OutsaleForm(forms.ModelForm):
    class Meta:
        model = Outsale
        fields ='__all__'
