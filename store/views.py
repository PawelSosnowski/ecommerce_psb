from django.shortcuts import render
from django.http import HttpResponse

from .models import Uzytkownik
from .models import Producent
from .models import Produkt
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
    return render(request, 'store/magazyn.html', context)


def zamowienia_klientow(request):
    query = 'SELECT * FROM podsumowanie_zamowien_klientow_v'
    context = {'zamowienia_klientow': Zamowienie.objects.raw(query)}
    return render(request, 'store/zamowienia_klientow.html', context)


def zamowienia_magazynu(request):
    context = {}
    return render(request, 'store/zamowienia_magazynu.html', context)

def store(request):
    context = {}
    return render(request, 'store/store.html', context)
