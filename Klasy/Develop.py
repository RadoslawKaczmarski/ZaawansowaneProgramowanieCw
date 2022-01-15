class Developer:
    def __init__(self, id: int, nazwa: str, miasto: str, ulica: str) -> None:
        self.id = id
        self.nazwa = nazwa
        self.miasto = miasto
        self.ulica = ulica

    @property
    def get_id(self):
        return self.id

    @property
    def get_nazwa(self):
        return self.nazwa

    @property
    def get_miasto(self):
        return self.miasto

    @property
    def get_ulica(self):
        return self.ulica

    def __str__(self) -> str:
        return f"ID:{self.id} Nazwa:{self.nazwa} " \
               f"Miasto:{self.miasto} Ulica:{self.ulica}"
