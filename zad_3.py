'''3. Stworzyć następujące klasy:
Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
area
rooms (int)
price
address


House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola:
    plot (rozmiar działki, int)
Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola:
    floor
Dodatkowo:
Każda z klas dziedziczących ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt.
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.
Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić.'''


class Property:
    def __init__(self,area,rooms:int,price,address):
        self.area=area
        self.rooms=rooms
        self.price=price
        self.address=address

    def __str__(self):
        return f"AREA: {self.area} ; ROOMS: {self.rooms} ; PRICE: {self.price} ; ADDRESS: {self.address}"

class House(Property):
    def __init__(self,plot:int,area,rooms:int,price,address):
        super().__init__(area,rooms,price,address)
        self.plot=plot

    def __str__(self):
        return f"PLOT:{self.plot} AREA: {self.area} ; ROOMS: {self.rooms} ; PRICE: {self.price} ; ADDRESS: {self.address}"

class Flat(Property):
    def __init__(self,floor,area,rooms:int,price,address):
        super().__init__(area,rooms,price,address)
        self.floor=floor

    def __str__(self):
        return f"FLOOR:{self.floor} AREA: {self.area} ; ROOMS: {self.rooms} ; PRICE: {self.price} ; ADDRESS: {self.address}"

H1=House(20,"A1",4,"100 000","Konopicka")
F1=Flat(2,"A1",4,"100 000","Konopicka")

print(H1)
print(F1)
