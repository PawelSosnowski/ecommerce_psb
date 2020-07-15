from django.shortcuts import render
from django.http import HttpResponse
from .models import Producent
# Create your views here.

def raports(request):
    lista_producentow = Producent.objects.order_by('idproducent')
    output = ', '.join([p.nazwa for p in lista_producentow])
    return HttpResponse(output, )
    # return render(request, 'store/raports.html', context)

def managements(request):
    context = {}
    return render(request, 'store/management.html', context)

def store(request):
    context = {}
    return render(request, 'store/store.html', context)