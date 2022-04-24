from django import forms


class StockForm(forms.Form):
    sdate = forms.DateField()
    edate = forms.DateField()

class DateForm(forms.Form):
    date=forms.DateField()
    
