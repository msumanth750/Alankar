from django import forms


class SaleForm(forms.Form):
    sdate = forms.DateField()
    edate = forms.DateField()
