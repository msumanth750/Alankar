from django.urls import path
from credits_debits import views

urlpatterns = [
    path('',views.homepage,name='credits')
]
