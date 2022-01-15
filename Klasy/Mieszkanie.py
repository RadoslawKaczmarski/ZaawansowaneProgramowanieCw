class Mieszkanie:
    def __init__(self, id: int, m2: int, ulica: str, miasto: str) -> None:
        self.id = id
        self.m2 = m2
        self.ulica = ulica
        self.miasto = miasto

    @property
    def get_id(self):
        return self.id

    @property
    def get_m2(self):
        return self.m2

    @property
    def get_ulica(self):
        return self.ulica

    @property
    def get_miasto(self):
        return self.miasto

    def __str__(self) -> str:
        return f"ID:{self.id} M2:{self.m2} " \
               f"Ulica:{self.ulica} Miasto:{self.miasto}"
