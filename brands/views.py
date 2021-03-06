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

class Brands():
    """Brands object for using brand model"""
    def __init__(self, arg):
        super(Brands, self).__init__()
        self.arg = arg
    def getBrands(*args,**kwargs):
        brands = Brand.objects.all().order_by('-ncode')
        liquors = brands.filter(type='L')
        beers = brands.filter(type='B')
        miscs = brands.filter(type='M')
        context = {
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
    context = getTotalBrands()
    context['brands']=brands
    context['form']=form
    return render(request,'brands/brand.html',context)

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
