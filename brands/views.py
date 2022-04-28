from django.shortcuts import render,redirect
from .models import Brand
from .forms import Brandform

import datetime
import random
# Create your views here.
def getTotalBrands():
    brands = Brand.objects.all()
    liquors = brands.filter(type='L')
    beers = brands.filter(type='B')
    miscs = brands.filter(type='M')
    context ={
        'total':brands.count(),
        'Liquors':brands.filter(type='L').order_by('ncode'),
        'beers':brands.filter(type='B'),
        'miscs':brands.filter(type='M'),
        'l':liquors.count(),
        'b':beers.count(),
        'm':miscs.count(),
    }
    return context;


def brandtable(request):
    form = Brandform()
    brands = Brand.objects.all().order_by('ncode')
    return render(request,'brands/brand.html',{'brands':brands,'form':form})

def addbrand(request):
    if request.method=='POST':
        form = Brandform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/brands/')
def editbrand(request,pk):
    brand=Brand.objects.get(id=pk)
    form=Brandform(instance=brand)
    if request.method=="POST":
        form=Brandform(request.POST.copy(),instance=brand)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/brands/')
    return render(request,'brands/update.html',{'form':form})

def gettime(request):
    context = {
    'time' :datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
    'day':datetime.datetime.today().strftime('%A')

    }
    return render(request,'brands/time.html',context)
