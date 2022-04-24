from django.urls import path,include
from expenditure import views

urlpatterns = [
    #path('',views.indexview,name='exp'),
    path('',views.Explist.as_view(),name='exp'),
    path('<str:pk>/detail',views.ExpDetail.as_view()),
    path('<str:pk>/update',views.Expupdate.as_view()),
    path('<str:pk>/delete',views.ExpDelete.as_view()),



]
