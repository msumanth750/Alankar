from django.shortcuts import render
from faker import Faker
import random

fake =Faker('en_IN')
def crdr(a):
    context=[]
    for i in range(a):
        name=fake.name()
        amt = random.randrange(55,600)
        type = random.choice([1,2])
        li ={
            'name':name,
            'amt':amt,
            'type':type
            }
        context.append(li)
    return context

# Create your views here.
def homepage(request):
    context ={'datas':crdr(20)}
    return render(request,'credits_debits/home.html',context)
