from django.shortcuts import render,redirect
from .models import Exp
from .forms import ExpForm
from django.urls import reverse_lazy
import datetime


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.db.models import Avg, Max, Min, Sum
def strtodate(date):
    tpl=tuple(map(int,date.split('-')))
    return datetime.date(tpl[0],tpl[1],tpl[2]);

# Create your views here.
'''def indexview(request):
    exps=Exp.objects.all().order_by('-cdate')
    total =Exp.objects.all().aggregate(Sum('amount'))
    return render(request,'expenditure/exp.html',{'exps':exps,'total':total,})'''

class Explist(ListView):
    model = Exp
    template_name = 'expenditure/exp.html'
    context_object_name ='exps'
    ordering =['-cdate']

class ExpDetail(DetailView):
    model = Exp
    template_name = 'expenditure/detail.html'
    context_object_name = 'exp'
    pk_url_kwarg ='pk'

class Expupdate(UpdateView):
    model = Exp
    fields =['name','amount','note']
    success_url = reverse_lazy('exp')
    template_name = 'expenditure/update.html'

class ExpDelete(DeleteView):
    model = Exp
    template_name = 'expenditure/delete.html'
    context_object_name = 'exp'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('exp')

def expAdd(request):
    expa=Exp.objects.all().order_by('-date')
    if request.method=="POST":
        date=strtodate(request.POST['date'])
        name=request.POST['name']
        amt=request.POST['amount']
        note=request.POST['note']
        e = Exp(date=date,name=name,amount=amt,note=note)
        e.save()
        exp,ttl =getExp(date)
        return render(request,'expenditure/expadd.html',{'exps':exp,'ttl':ttl,'date':date})
    return render(request,'expenditure/expadd.html',{'expa':expa})

def getExp(date):
    exps = Exp.objects.all().filter(date=date).order_by('-amount')
    total = exps.aggregate(Sum('amount'))
    return exps,total
