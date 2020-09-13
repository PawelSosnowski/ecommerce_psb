from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name="store"),
    path('store/zamow', views.zamow, name='zamow'),
    path('reports/', views.reports, name="reports"),
    path('management/', views.managements, name="managements"),
    path('reports/actionUrl', views.generate_raports, name="generate_reports"),
    path('orders/', views.reports_orders, name="reports_orders"),
    path('orders/generateOrders', views.generate_orders, name="generate_orders"),
    path('warehouse/', views.reports_warehouse, name="reports_warehouse"),
    path('warehouse/generateWR', views.generate_warehouse, name="generate_warehouse"),
    path('management/magazyn', views.magazyn, name="magazyn"),
    path('management/zamowienia_klientow', views.zamowienia_klientow, name="zamowienia_klientow"),
    path('management/zamowienia_magazynu', views.zamowienia_magazynu, name="zamowienia_magazynu"),
    path('reports/actionUrl', views.generate_raports, name="generate_reports")
]

