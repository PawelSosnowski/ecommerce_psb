from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('reports/', views.reports, name="reports"),
    path('management/', views.managements, name="managements"),
    path('management/magazyn', views.magazyn, name="magazyn"),
    path('management/zamowienia_klientow', views.zamowienia_klientow, name="zamowienia_klientow"),
    path('management/zamowienia_magazynu', views.zamowienia_magazynu, name="zamowienia_magazynu"),
    path('reports/actionUrl', views.generate_raports, name="generate_reports")

]

