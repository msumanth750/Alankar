from django import forms

from .models import Brand


class Brandform(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['ncode','name','scode','type','price','qty','mrp','bprice']
