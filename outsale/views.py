from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View

from .models import Outsale
from .forms import OutsaleForm

from brands import models as bm
from stock import models as sm
from expenditure import models as em
from expenditure.views import getExp

from .forms import SaleForm

from core.utils import render_to_pdf


from django.db.models import Avg, Max, Min, Sum

import datetime

def strtodate(date):
    tpl=tuple(map(int,date.split('-')))
    return datetime.date(tpl[0],tpl[1],tpl[2]);

def sale(datea,dateb):
    form =SaleForm()
    brands = bm.Brand.objects.all().order_by('ncode')
    stocka=sm.Stock.objects.all().filter(date=datea)
    stockb=sm.Stock.objects.all().filter(date=dateb)
    receits = sm.Receits.objects.all().filter(date=datea)
    exps= em.Exp.objects.all().filter(date=datea)
    ttl = int(0 if exps.aggregate(Sum('amount'))['amount__sum'] is None else exps.aggregate(Sum('amount'))['amount__sum'])
    sales=[]
    salet=0;
    cont={}
    for brand in brands:
        cont={}
        cont['os']=0
        cont['cs']=0
        cont['rc']=0
        for stock in stocka:
            cont['brand']=brand
            if stock.brand.ncode==brand.ncode:
                cont['os']=stock.obal
                break;
        for stock in stockb:
            if stock.brand.ncode==brand.ncode:
                cont['cs']=stock.obal
                break;
        for receit in receits:
            if receit.brand==brand:
                cont['rc']=receit.qty
                break;
        cont['s']=cont['os']+cont['rc']-cont['cs']
        cont['amt']=int(cont['s']*brand.bprice)
        salet+=cont['amt']
        sales.append(cont)
    context ={'sales':sales,'salet':salet,'date':datea,'exps':exps,'ttl':ttl,'dateb':dateb,'form':SaleForm()}
    return context;

# Create your views here.
def indexview(request):
    if request.method=='POST':
        form = request.POST
        datea =strtodate(form['date'])
        return render(request,'outsale/outsale.html',sale(datea,datea+datetime.timedelta(days=1)))
    return render(request,'outsale/outsale.html',sale(datetime.date(2022,4,11),datetime.date(2022,4,13)))

#pdf sale for a day
class PdfView(View):
    def get(self,request,*args,**kwargs):
        datea =datetime.date(2022,4,12)
        pdf = render_to_pdf('outsale/pdf.html',sale(datea,datea+datetime.timedelta(days=1)))
        return HttpResponse(pdf, content_type='application/pdf')

    def post(self,request,*args,**kwargs):
        datea = strtodate(request.POST['date'])
        pdf = render_to_pdf('outsale/pdf.html',sale(datea,datea+datetime.timedelta(days=1)))
        return HttpResponse(pdf, content_type='application/pdf')

# discountsales depends on date
def getoutsale(datea=datetime.date(1,1,1)):
    if datea==datetime.date(1,1,1):
        sales = Outsale.objects.all().order_by('-date')
        dis=gettotaloutsalediscount(sales)
    else:
        sales = Outsale.objects.all().filter(date=datea)
        dis=gettotaloutsalediscount(sales)
    return {'sales':sales,'discount':dis,'date':datea}

def gettotaloutsalediscount(sales):
    discount= 0;
    for sale in sales:
        discount+=(sale.brand.bprice-sale.price)*sale.qty
    return discount

def mrpview(request):
    if request.method == "POST":
        datea =strtodate(request.POST['date'])
        sales = getoutsale(datea)
        return render(request,'outsale/mrp.html',sales)
    sales = getoutsale()
    return render(request,'outsale/mrp.html',sales)

def outsaleAdd(request):
    form = OutsaleForm()
    if request.method == "POST":
        form = OutsaleForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'outsale/add.html',{'form':form,'sales':getoutsale()})

def outsaleDelete(request,pk):
    sale= Outsale.objects.get(id=pk)
    sale.delete()
    return redirect("/outsale/add")

def dailysheet(request):
    if request.method == "POST":
        form = request.POST
        datea =strtodate(form['date'])
        sales=sale(datea,datea+datetime.timedelta(days=1))
        outsales = getoutsale(datea)
        cc = sales['salet']-outsales['discount']-sales['ttl']
        context ={
        'sales':sales,
        'outsales':outsales,
        'date':datea,
        'cc':cc,
        'message' : 'Data Not Updated'
        }
        return render(request,'outsale/salesheet.html',context)
    sales={
    'salet':0
    }
    message ="Please enter the date"
    return render(request,'outsale/salesheet.html',{'sales':sales,'message':message})
