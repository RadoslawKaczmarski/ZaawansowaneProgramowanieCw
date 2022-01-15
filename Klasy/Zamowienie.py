class Zamowienie:
    def __init__(self) -> None:
        self._id = None
        self._id_parceli = None
        self._m2 = None
        self._cena = None
        self._wlasciciel = None

    @property
    def get_id(self):
        return self._id

    @get_id.setter
    def set_id(self, x):
        self._id = x

    @property
    def get_id_parceli(self):
        return self._id_parceli

    @get_id_parceli.setter
    def set_id_parceli(self, x):
        self._id_parceli = x

    @property
    def get_m2(self):
        return self._m2

    @get_m2.setter
    def set_m2(self, x):
        self._m2 = x

    @property
    def get_cena(self):
        return self._cena

    @get_cena.setter
    def set_cena(self, x):
        self._cena = x

    @property
    def get_wlasciciel(self):
        return self._wlasciciel

    @get_wlasciciel.setter
    def set_wlasciciel(self, x):
        self._wlasciciel = x

    def wart_zam(self) -> str:
        return f"Wartosc zamówiania to: {round(sum(self._cena), 2)}"

    def sum_m2(self) -> str:
        return f"Suma M2 to: {round(sum(self._m2), 2)}"

    def __str__(self) -> str:
        return f"ID:{self._id} ID_Parceli:{self._id_parceli} " \
               f"M2:{self._m2} Cena:{self._cena} " \
               f"Wlasciciel: {self._wlasciciel}"
