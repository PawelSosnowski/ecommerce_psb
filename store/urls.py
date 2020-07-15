from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('reports/', views.reports, name="reports"),
    path('management/', views.managements, name="managements"),
    path('reports/actionUrl', views.generate_raports, name="generate_reports")
]

