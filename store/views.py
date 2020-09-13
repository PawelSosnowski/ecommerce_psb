from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
import datetime
import json

from .models import Uzytkownik
from .models import Producent
from .models import Produkt
from .models import Magazyn
from .models import Zamowienie
from .models import ZamowieniaProdukty
from .models import PodsumowanieZamowienMagazynu
from .models import Store


def reports(request):
    lista_producentow = Producent.objects.order_by('idproducent')
    # output = ', '.join([p.nazwa for p in lista_producentow])
    return render(request, 'store/reports.html')


def generate_raports(request):
    lista_uzytkownikow = Uzytkownik.objects.raw('SELECT idUzytkownik, Imie, Nazwisko, Email, '
                                                'ifnull(LiczbaZamowien, 0 ) as LiczbaZamowien from v_rklienciliczba')
    context = {"uzytkownicy": lista_uzytkownikow}
    return render(request, 'store/generate_report.html', context)


def managements(request):
    context = {}
    return render(request, 'store/management.html', context)


def magazyn(request):
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
def zamow(request: HttpRequest):
    if request.method == 'POST':
        cart = json.loads(request.POST['cart'])
        if cart:
            owner_id = cart['ownerID']
            items = {int(k): int(v) for k, v in cart['items'].items()}
            zam = Zamowienie()
            zam.save()
            owner: Uzytkownik = Uzytkownik.objects.get(pk=owner_id)
            zam.idskladajacegouzytkownika = owner
            zam.datazlozenia = datetime.datetime.now()
            zam.dostawa_adresdostawy_miasto = owner.adres_miasto
            zam.dostawa_adresdostawy_kodpocztowy = owner.adres_kodpocztowy
            zam.dostawa_adresdostawy_ulica = owner.adres_ulica
            zam.czyoplacone = False

            zamowienia_produkty = [ZamowieniaProdukty.create(idZamowienia=zam,
                                                             idProduktu=Produkt.objects.get(pk=item_id),
                                                             liczbaSztuk=amount)
                                   for item_id, amount
                                   in items.items()]

            for record in zamowienia_produkty:
                record.save()

            price = sum([Produkt.objects.get(pk=item_id).cena * amount
                         for item_id, amount
                         in items.items()])
            zam.cena = price
            zam.save()

    context = {}
    return render(request, 'store/zamow.html', context)


def zamowienia_magazynu(request):
    zamowienia = PodsumowanieZamowienMagazynu.objects.all()
    context = {'zamowienia': zamowienia}
    return render(request, 'store/zamowienia_magazynu.html', context)


def store(request):
    products = Store.objects.all()
    products_json = serializers.serialize('json', products)
    context = {'products': products, 'products_json': products_json}
    return render(request, 'store/store.html', context)

