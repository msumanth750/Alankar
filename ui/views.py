from django.shortcuts import render
import random


from brands.views import getTotalBrands
# Create your views here.
def home(request):
    context = getTotalBrands()
    return render(request,'ui/home.html',context)

def viewbase(request):
    return render(request,'ui/base.html')

def index(request):
    return render(request,'ui/line.html')
