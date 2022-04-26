from django import forms
from .models import Exp

class ExpForm(forms.Form):
    class meta():
        model = Exp
        fields =['date','name','amount','note']
