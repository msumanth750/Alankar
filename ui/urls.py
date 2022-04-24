from django.urls import path,include
from ui import views


urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index),
    path('base/',views.viewbase)
]
