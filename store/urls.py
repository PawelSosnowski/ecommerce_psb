from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('raports/', views.raports, name="raports"),
    path('management/', views.managements, name="managements"),
]

