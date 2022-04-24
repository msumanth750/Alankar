from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Outsale

from brands import models as bm
from stock import models as sm
from expenditure import models as em

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
    exps= em.Exp.objects.all().filter(cdate=datea)
    ttl = exps.aggregate(Sum('amount'))
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
        sales = Outsale.objects.all()
        dis=gettotaloutsalediscount(sales)
    else:
        sales = Outsale.objects.all().filter(date=datea)
        dis=gettotaloutsalediscount(sales)
    return {'sales':sales,'discount':dis}


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


def dailysheet(request):
    if request.method == "POST":
        form = request.POST
        datea =strtodate(form['date'])
        sales=sale(datea,datea+datetime.timedelta(days=1))
        outsales = getoutsale(datea)
        context ={
        'sales':sales,
        'outsales':outsales,
        }
        return render(request,'outsale/salesheet.html',context)
    sales=sale(datetime.date(2022,4,11),datetime.date(2022,4,13))
    outsales = getoutsale()
    context ={
    'sales':sales,
    'outsales':outsales,
    }
    print(sale,outsales)
    return render(request,'outsale/salesheet.html',context)
