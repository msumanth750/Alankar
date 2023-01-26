from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Brand
from .forms import Brandform
import datetime
import random
from django.db import models
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

from django.contrib import admin
def create_model(name, fields=None, app_label='', module='', options=None, admin_opts=None):
    class Meta:
        # Using type('Meta', ...) gives a dictproxy error during model creation
        pass

    if app_label:
        # app_label must be set using the Meta inner class
        setattr(Meta, 'app_label', app_label)

    # Update Meta with any options that were provided
    if options is not None:
        for key, value in options.items():
            setattr(Meta, key, value)

    # Set up a dictionary to simulate declarations within a class
    attrs = {'__module__': module, 'Meta': Meta}

    # Add in any fields that were provided
    if fields:
        attrs.update(fields)

    # Create the class, which automatically triggers ModelBase processing
    model = type(name, (models.Model,), attrs)

    # Create an Admin class if admin options were provided
    if admin_opts is not None:
        class Admin(admin.ModelAdmin):
            pass
        for key, value in admin_opts:
            setattr(Admin, key, value)
        admin.site.register(model, Admin)

    return model

fields = {
     'first_name': models.CharField(max_length=255),
     'last_name': models.CharField(max_length=255),
     '__str__': lambda self: '%s %s' (self.first_name, self.last_name),
 }

options = {
     'ordering': ['last_name', 'first_name'],
     'verbose_name': 'valued customer',
 }
admin_opts = {}

def install(model):
    from django.core.management import sql, color
    from django.db import connection

    # Standard syncdb expects models to be in reliable locations,
    # so dynamic models need to bypass django.core.management.syncdb.
    # On the plus side, this allows individual models to be installed
    # without installing the entire project structure.
    # On the other hand, this means that things like relationships and
    # indexes will have to be handled manually.
    # This installs only the basic table definition.

    # disable terminal colors in the sql statements
    style = color.no_style()

    cursor = connection.cursor()
    statements, pending = sql.sql_model_create(model, style)
    for sql in statements:
        cursor.execute(sql)

def modelsave(request):
    model = create_model('Person', fields,
        options=options,
        admin_opts=admin_opts,
        app_label='brands_app',
        )
    print(model)
    install(model)
    print('Installed model ')
    return HttpResponse('<h1>object created </h1>')
