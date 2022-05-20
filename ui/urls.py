from django.urls import path,include
from ui import views


urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index),
    path('sales',views.sales),
    path('expenses',views.expenses),
    path('loans',views.loans),
    path('brands',views.brands),
    path('profile',views.profile),
    path('staff',views.staff),
    path('partners',views.partners),


    path('base/',views.viewbase)
]
