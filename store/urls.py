from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('reports/', views.reports, name="reports"),
    path('management/', views.managements, name="managements"),
    path('reports/actionUrl', views.generate_raports, name="generate_reports"),
    path('orders/', views.reports_orders, name="reports_orders"),
    path('orders/generateOrders', views.generate_orders, name="generate_orders"),
    path('warehouse/', views.reports_warehouse, name="reports_warehouse"),
    path('warehouse/generateWR', views.generate_warehouse, name="generate_warehouse"),

]

