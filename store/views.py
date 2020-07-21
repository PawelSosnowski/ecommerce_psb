from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect

from .models import Uzytkownik
from .models import Producent
from .models import Produkt
from .models import Magazyn
from .models import Zamowienie

# Create your views here.


def reports(request):
    lista_producentow = Producent.objects.order_by('idproducent')
    # output = ', '.join([p.nazwa for p in lista_producentow])
    return render(request, 'store/reports.html')



def generate_raports(request):
    lista_uzytkownikow = Uzytkownik.objects.raw('SELECT idUzytkownik, Imie, Nazwisko, Email, ifnull(LiczbaZamowien, 0 ) as LiczbaZamowien from v_rklienciliczba')
    context = {"uzytkownicy": lista_uzytkownikow}
    return render(request, 'store/generate_report.html', context)


def managements(request):
    context = {}
    return render(request, 'store/management.html', context)


def magazyn(request):
    #query = '''
    #SELECT * FROM magazyn_v
    #'''
    #products = Produkt.objects.raw(query)
    #products_json = serializers.serialize('json', products)
    #context = {'products': products, 'products_json': products_json}
    products = Magazyn.objects.all()
    products_json = serializers.serialize('json', products)
    context = {'products': products, 'products_json': products_json}
    return render(request, 'store/magazyn.html', context)

@csrf_protect
def zamowienia_klientow(request):
    query = 'SELECT * FROM podsumowanie_zamowien_klientow_v'
    context = {'zamowienia_klientow': Zamowienie.objects.raw(query)}
    ctx_json = serializers.serialize('json', context['zamowienia_klientow'])
    context['json'] = ctx_json
    return render(request, 'store/zamowienia_klientow.html', context)

@csrf_protect
def zamowienia_magazynu(request):
    context = {}
    return render(request, 'store/zamowienia_magazynu.html', context)

def store(request):
    context = {}
    return render(request, 'store/store.html', context)
