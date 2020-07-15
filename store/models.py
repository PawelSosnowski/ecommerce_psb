from django.db import models

# Create your models here.


class Kategoria(models.Model):
    idkategoria = models.IntegerField(db_column='idKategoria', primary_key=True)
    nazwa = models.CharField(db_column='Nazwa', max_length=45, blank=True, null=True)
    idnadkategorii = models.ForeignKey('self', models.DO_NOTHING, db_column='idNadkategorii', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kategoria'


class PracownikMagazynu(models.Model):
    idpracownik_magazynu = models.IntegerField(db_column='idPracownik_Magazynu', primary_key=True)
    imie = models.CharField(db_column='Imie', max_length=45, blank=True, null=True)
    nazwisko = models.CharField(db_column='Nazwisko', max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pracownik_magazynu'


class Producent(models.Model):
    idproducent = models.IntegerField(db_column='idProducent', primary_key=True)
    nazwa = models.CharField(db_column='Nazwa', max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'producent'


class Produkt(models.Model):
    idprodukt = models.IntegerField(db_column='idProdukt', primary_key=True)
    nazwa = models.CharField(db_column='Nazwa', max_length=45, blank=True, null=True)
    cena = models.FloatField(db_column='Cena', blank=True, null=True)
    iloscmagazynowa = models.IntegerField(db_column='IloscMagazynowa', blank=True, null=True)
    czyarchiwalny = models.IntegerField(db_column='CzyArchiwalny', blank=True, null=True)
    idproducentaproduktu = models.ForeignKey(Producent, models.DO_NOTHING, db_column='idProducentaProduktu', blank=True, null=True)
    idkategoriiproduktu = models.ForeignKey(Kategoria, models.DO_NOTHING, db_column='idKategoriiProduktu', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'produkt'


class Uzytkownik(models.Model):
    iduzytkownik = models.IntegerField(db_column='idUzytkownik', primary_key=True)
    login = models.CharField(db_column='Login', max_length=45, blank=True, null=True)
    haslo = models.CharField(db_column='Haslo', max_length=45, blank=True, null=True)
    imie = models.CharField(db_column='Imie', max_length=45, blank=True, null=True)
    nazwisko = models.CharField(db_column='Nazwisko', max_length=45, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)
    adres_ulica = models.CharField(db_column='Adres_Ulica', max_length=45, blank=True, null=True)
    adres_kodpocztowy = models.IntegerField(db_column='Adres_KodPocztowy', blank=True, null=True)
    adres_miasto = models.CharField(db_column='Adres_Miasto', max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'uzytkownik'


class ZamowieniaMagazynuProdukty(models.Model):
    idzamowieniamagazynu = models.OneToOneField('ZamowienieMagazynu', models.DO_NOTHING, db_column='idZamowieniaMagazynu', primary_key=True)
    idproduktuzm = models.ForeignKey(Produkt, models.DO_NOTHING, db_column='idProduktuZM')
    liczbasztuk = models.IntegerField(db_column='LiczbaSztuk', blank=True, null=True)
    cena = models.FloatField(db_column='Cena', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'zamowienia_magazynu_produkty'
        unique_together = (('idzamowieniamagazynu', 'idproduktuzm'),)


class ZamowieniaProdukty(models.Model):
    idzamowienia = models.OneToOneField('Zamowienie', models.DO_NOTHING, db_column='idZamowienia', primary_key=True)
    idzamowionegoproduktu = models.ForeignKey(Produkt, models.DO_NOTHING, db_column='idZamowionegoProduktu')
    liczbasztuk = models.IntegerField(db_column='LiczbaSztuk', blank=True, null=True)
    cena = models.FloatField(db_column='Cena', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'zamowienia_produkty'
        unique_together = (('idzamowienia', 'idzamowionegoproduktu'),)


class Zamowienie(models.Model):
    idzamowienia = models.IntegerField(db_column='idZamowienia', primary_key=True)
    cena = models.FloatField(db_column='Cena', blank=True, null=True)
    stan = models.CharField(db_column='Stan', max_length=45, blank=True, null=True)
    datazlozenia = models.DateTimeField(db_column='DataZlozenia', blank=True, null=True)
    czyoplacone = models.IntegerField(db_column='CzyOplacone', blank=True, null=True)
    dataskompletowania = models.DateTimeField(db_column='DataSkompletowania', blank=True, null=True)
    dostawa_cenadostawy = models.FloatField(db_column='Dostawa_CenaDostawy', blank=True, null=True)
    dostawa_numerlistuprzewozowego = models.IntegerField(db_column='Dostawa_NumerListuPrzewozowego', blank=True, null=True)
    dostawa_adresdostawy_ulica = models.CharField(db_column='Dostawa_AdresDostawy_Ulica', max_length=45, blank=True, null=True)
    dostawa_adresdostawy_kodpocztowy = models.IntegerField(db_column='Dostawa_AdresDostawy_KodPocztowy', blank=True, null=True)
    dostawa_adresdostawy_miasto = models.CharField(db_column='Dostawa_AdresDostawy_Miasto', max_length=45, blank=True, null=True)
    idskladajacegouzytkownika = models.ForeignKey(Uzytkownik, models.DO_NOTHING, db_column='idSkladajacegoUzytkownika', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'zamowienie'


class ZamowienieMagazynu(models.Model):
    idzamowienie_magazynu = models.IntegerField(db_column='idZamowienie_magazynu', primary_key=True)
    nrzamowienia = models.IntegerField(db_column='NrZamowienia', blank=True, null=True)
    wartosczamowienia = models.FloatField(db_column='WartoscZamowienia', blank=True, null=True)
    idskladajacegopracownika = models.ForeignKey(PracownikMagazynu, models.DO_NOTHING, db_column='idSkladajacegoPracownika', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'zamowienie_magazynu'
