from django import forms
from .models import Exp

class ExpForm(forms.Form):
    class meta():
        model = Exp
        fields =['name','amount','note']
