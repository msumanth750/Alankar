from django.shortcuts import render
from .models import Exp
from .forms import ExpForm
from django.urls import reverse_lazy


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.db.models import Avg, Max, Min, Sum

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
