from django import forms


from.models import Stock

class StockForm(forms.Form):
    sdate = forms.DateField()
    edate = forms.DateField()

class DateForm(forms.Form):
    date=forms.DateField()

class StockentryForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['date','brand','obal']
