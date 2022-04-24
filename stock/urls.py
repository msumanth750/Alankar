from django.urls import path
from stock import views

urlpatterns = [
    path('',views.dashboard),
    path('brand/',views.brands),
    path('stocks/',views.stock,name='stock'),
    path('receits/',views.receit),
    path('receits/rpdf/',views.PdfReceit.as_view(),name="receitpdf")
]
