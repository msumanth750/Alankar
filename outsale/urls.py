from django.urls import path
from outsale import views

urlpatterns = [
    path('',views.indexview,name='outsale'),
    path('pdf',views.PdfView.as_view(),name='salepdf'),
    path('mrp',views.mrpview,name='mrpview'),
    path('salesheet',views.dailysheet,name='dailysheet'),
    path('add',views.outsaleAdd,name='outsaleadd'),
    path('delete/<int:pk>',views.outsaleDelete,name='outsaledelete')

]
