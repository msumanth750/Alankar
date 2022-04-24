from django.urls import path
from brands import views

urlpatterns = [
    path('',views.brandtable,name='brand-table'),
    path('add/',views.addbrand,name='addbrand'),
    path('edit/<pk>',views.editbrand,name='editbrand')
]
