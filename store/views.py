from django.shortcuts import render
from django.http import HttpResponse
from .models import Producent
from .models import Produkt


# Create your views here.


def reports(request):
    lista_producentow = Producent.objects.order_by('idproducent')
    # output = ', '.join([p.nazwa for p in lista_producentow])
    context = {}
    return render(request, 'store/reports.html', context)


def generate_raports(request):
    context = {}
    return render(request, 'store/generate_report.html', context)


def managements(request):
    query = '''
    SELECT
        produkt.idProdukt AS idProdukt,
        produkt.Nazwa AS produktNazwa,
        kategoria.Nazwa AS kategoriaNazwa,
        producent.Nazwa AS producentNazwa,
        produkt.IloscMagazynowa AS ilosc
    FROM
        produkt
            JOIN
        producent ON produkt.idProducentaProduktu = producent.idProducent
            JOIN
        kategoria ON produkt.idKategoriiProduktu = kategoria.idKategoria
    WHERE
        NOT produkt.CzyArchiwalny
    '''
    context = {'products': Produkt.objects.raw(query)}
    return render(request, 'store/management.html', context)


def store(request):
    context = {}
    return render(request, 'store/store.html', context)
