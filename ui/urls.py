from django.urls import path,include
from ui import views


urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='dashboard'),
    path('sales',views.sales,name='sales'),
    path('expenses',views.expenses,name='expenses'),
    path('loans',views.loans,name='loans'),
    path('brands',views.brands,name='brands'),
    path('profile',views.profile,name='profile'),
    path('staff',views.staff,name='staff'),
    path('partners',views.partners,name='partners'),


    path('base/',views.viewbase)
]
