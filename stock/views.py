from django.shortcuts import render
from .models import Brand,Stock,Receits
from django.views import View

from .forms import StockForm,DateForm
from core.utils import render_to_pdf
from django.http import HttpResponse
from brands import models as mb

import datetime
# Create your views here.
def strtodate(date):
    tpl=tuple(map(int,date.split('-')))
    return datetime.date(tpl[0],tpl[1],tpl[2]);

def dashboard(request):
    total_brands = mb.Brand.objects.all().count()
    stocks=Stock.objects.all().filter(date=datetime.date(2022, 4, 12))
    st=stocks.order_by('obal')
    mins=stocks.filter(obal__lte=3 ).order_by('obal')
    return render(request,'ui/dashboard.html',{'stocks':st,'mins':mins,'tb':total_brands})

def saletable(request):
    cont=[]
    salesum=0
    #brandcount =Brand.objects.all().count()
    brands =Brand.objects.all()
    stocks = Stock.objects.all()
    for brand in brands:
        datea = datetime.date(2022, 4, 10)
        dateb = datetime.date(2022, 4, 13)
        id='1'
        if request.method == 'POST':
            form = StockForm(request.POST)
            datea = strtodate(form['sdate'].value())
            dateb = strtodate(form['edate'].value())
            print(dateb,type(dateb))
        stocks= Stock.objects.all().filter(brand = brand)
        receits = Receits.objects.all().filter(brand = brand)

        #datea ='2022-04-10'#input('Enter The Start Date:')
        #dateb ='2022-04-11'#input('Enter The Start Date:')
        osa=0
        osb=0
        rcsum=0
        notes=""
        for rc in receits:
            if rc.date>=datea and rc.date<=dateb:
                rcsum+=rc.qty
                notes+=(str("("+str(rc.qty)+")"))


        for stock in stocks:
            stockn = stock
            if (stock.date==datea):
                osa=stock.obal
            if (stock.date==dateb):
                osb =stock.obal
            context = {
                'name':stockn.brand.name,
                'osa':osa,
                'rc':str(rcsum)+notes,
                'tt':osa+rcsum,
                'osb':osb,
                'sold': str(osa+rcsum-osb),
                'price' :int(stockn.brand.price/stockn.brand.qty),
                'total':int((stockn.brand.price/stockn.brand.qty)*(osa+rcsum-osb)),}
            cont.append(context)
            salesum+=(stockn.brand.price/stockn.brand.qty)*(osa+rcsum-osb)
    print(cont)
    #return render(request,'ui/table.html',{'brands':brands})
    return render(request,'ui/test.html',{'datas':cont,'form':StockForm(request.POST),"datea":datea,
    "dateb":dateb,'sale':int(salesum)})

def brands(request):
    brands = Brand.objects.all().order_by('ncode')
    return render(request,'stock/brands.html',{'brands':brands})

def stock(request):
    form=DateForm(request.POST)
    today =datetime.date.today()
    stocks =Stock.objects.all().filter(date=today)
    if request.method=='POST':
        form= DateForm(request.POST)
        input =strtodate(form['date'].value())
        stocks =Stock.objects.all().filter(date=input)
        return render(request,'stock/stock.html',{'stocks':stocks,'form':form,'date':input.strftime('%Y-%m-%d')})
    return render(request,'stock/stock.html',{'stocks':stocks,'form':form,'date':today.strftime('%Y-%m-%d')})

def receit(request):
    form=DateForm(request.POST)
    today =datetime.date.today()
    receits=Receits.objects.all().filter(date=today)
    if request.method=='POST':
        form= DateForm(request.POST)
        input =strtodate(form['date'].value())
        receits =Receits.objects.all().filter(date=input)
        return render(request,'stock/receits.html',{'receits':receits,'form':form,'date':input.strftime('%Y-%m-%d')})

    return render(request,'stock/receits.html',{'receits':receits,'form':form})

class PdfReceit(View):
    def get(self,request,*args,**kwargs):
        receits=Receits.objects.all().filter(date=datetime.date(2022, 4, 12))
        pdf = render_to_pdf('stock/receitpdf.html',{'receits':receits})
        return HttpResponse(pdf,content_type='application/pdf')
    def post(self,request,*args,**kwargs):
        date = strtodate(request.POST['date'])
        receits=Receits.objects.all().filter(date=date)
        pdf = render_to_pdf('stock/receitpdf.html',{'receits':reversed(receits),'date':date.strftime('%Y-%m-%d')})
        return HttpResponse(pdf,content_type='application/pdf')