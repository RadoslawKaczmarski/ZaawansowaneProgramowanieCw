class Produkt:
    def __init__(self, nazwa: str, rodzaj: str, opakowanie: str, cena: float, gwarancja: str) -> None:
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.opakowanie = opakowanie
        self.cena = cena
        self.gwarancja = gwarancja

    @property
    def getnazwa(self):
        return self.nazwa

    @property
    def getrodzaj(self):
        return self.rodzaj

    @property
    def getopakowanie(self):
        return self.opakowanie

    @property
    def getcena(self):
        return self.cena

    @property
    def getgwarancja(self):
        return self.gwarancja

    def __str__(self) -> str:
        return f"Produkt: nazwa:{self.nazwa} ; rodzaj:{self.rodzaj} " \
               f" ; opakowanie:{self.opakowanie} ;  cena:{self.cena} ;  gwarancja:{self.gwarancja}"


class Magazyn:
    def __init__(self, produkt: str, iloshal: int, wielkosc: str, ulica: str, numerparceli: str) -> None:
        self.produkt = produkt
        self.iloschal = iloshal
        self.wielkosc = wielkosc
        self.ulica = ulica
        self.numerparceli = numerparceli

    @property
    def getprodukt(self):
        return self.produkt

    @property
    def getiloschal(self):
        return self.iloschal

    @property
    def getwielkosc(self):
        return self.wielkosc

    @property
    def getulica(self):
        return self.ulica

    @property
    def getnumerparceli(self):
        return self.numerparceli

    def __str__(self) -> str:
        return f"Magazyn: nazwa:{self.produkt} ; iloschal:{self.iloschal} " \
               f" ; wielkosc:{self.wielkosc} ;  ulica:{self.ulica} ;  numerparceli:{self.numerparceli}"


class KlientDetaliczny:
    def __init__(self, imie: str, nazwisko: str, adres: str, fax: str, telefon: str) -> None:
        self._imie = imie
        self._nazwisko = nazwisko
        self._adres = adres
        self._fax = fax
        self._telefon = telefon

    @property
    def _getimie(self):
        return self._imie

    @property
    def _getnazwisko(self):
        return self._nazwisko

    @property
    def _getadres(self):
        return self._adres

    @property
    def _getfax(self):
        return self._fax

    @property
    def _gettelefon(self):
        return self._telefon

    def __str__(self) -> str:
        return f"KlientDetaliczny: imie:{self._imie} ; nazwisko:{self._nazwisko} " \
               f" ; Adress:{self._adres} ;  fax:{self._fax} ;  telefon:{self._telefon}"


class Zamowienie:
    def __init__(self) -> None:
        self._idzamowienia = None
        self._produkt = None
        self._klient = None
        self._rodzajwyslki = None
        self._datawysylki = None

    @property
    def getid(self):
        return self._idzamowienia

    @getid.setter
    def setid(self, x):
        self._idzamowienia = x

    @property
    def getprodukt(self):
        return self._produkt

    @getprodukt.setter
    def setprodukt(self, x):
        self._produkt = x

    @property
    def getklient(self):
        return self._klient

    @getklient.setter
    def setklient(self, x):
        self._klient = x

    @property
    def getrodzajwyslki(self):
        return self._rodzajwyslki

    @getrodzajwyslki.setter
    def setrodzajwyslki(self, x):
        self._rodzajwyslki = x

    @property
    def getdata(self):
        return self._datawysylki

    @getdata.setter
    def setdata(self, x):
        self._datawysylki = x

    def adresklienta(self):
        return f"Adres klienta {self._klient}"

    def __str__(self) -> str:
        return f"KlientDetaliczny: ID:{self._idzamowienia} ; Produkt:{self._produkt} " \
               f" ; Klient:{self._klient} ;  Rodzaj:{self._rodzajwyslki} ;  Telefon:{self._datawysylki}"


class KlientBiznesowy:
    def __init__(self, imie: str, nazwisko: str, adress: str, fax: str, telefon: str) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.adress = adress
        self.fax = fax
        self.telefon = telefon

    @property
    def getimie(self):
        return self.imie

    @property
    def getnazwisko(self):
        return self.nazwisko

    @property
    def geadress(self):
        return self.adress

    @property
    def getfax(self):
        return self.fax

    @property
    def gettelefon(self):
        return self.telefon

    def __str__(self):
        return f"KlientBiznesowy: imie:{self.imie} ; nazwisko:{self.nazwisko} " \
               f" ; Adress:{self.adress} ;  fax:{self.fax} ;  telefon:{self.telefon}"


p1 = Produkt("Procesor", "Komputer", "Papier", 1509.99, "3 lata")

m1 = Magazyn(p1, 3, "1500m2", "Adamska", "13")

kd1 = KlientDetaliczny("Dariusz", "Kowlaksi", "Wolińska", "321-345-2342", "345-346-231")

kb1 = KlientBiznesowy("Kamil", "Nowak", "Kołobrzeska 7", "123-345-2341", "457-145-112")

z1 = Zamowienie()
z1.setid = 14
z1.setprodukt = p1
z1.setklient = kd1
z1.setrodzajwyslki = "Kurier"
z1.setdata = "13.07.2021"
print(z1)
print(z1.adresklienta())
