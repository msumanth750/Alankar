from django.urls import path
from loans import views


urlpatterns=[
    path('',views.indexview,name='loan')
]
