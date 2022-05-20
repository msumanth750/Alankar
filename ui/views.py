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
    lis=[50, 120, 105, 110, 95, 105, 90, 100, 80, 95, 70, 120]
    return render(request,'blackdashboard/dashboard.html',{'lis':lis})
def sales(request):
    return render(request,'blackdashboard/sales.html')
def expenses(request):
    return render(request,'blackdashboard/expenses.html')
def loans(request):
    return render(request,'blackdashboard/loans.html')
def brands(request):
    return render(request,'blackdashboard/brands.html')
def partners(request):
    return render(request,'blackdashboard/partners.html')
def staff(request):
    return render(request,'blackdashboard/staff.html')
def profile(request):
    return render(request,'blackdashboard/profile.html')
