class Dom:
    def __init__(self, id: int, m2: int, miasto: str,
                 ulica: str, nr_domu: str) -> None:
        self.id = id
        self.m2 = m2
        self.miasto = miasto
        self.ulica = ulica
        self.nr_domu = nr_domu

    @property
    def get_id(self):
        return self.id

    @property
    def get_m2(self):
        return self.m2

    @property
    def get_miasto(self):
        return self.miasto

    @property
    def get_ulica(self):
        return self.ulica

    @property
    def get_nr_domu(self):
        return self.nr_domu

    def __str__(self) -> str:
        return f"ID:{self.id} M2:{self.m2} " \
               f"Miasto:{self.miasto} Ulica:{self.ulica} " \
               f"Nr domu: {self.nr_domu}"
