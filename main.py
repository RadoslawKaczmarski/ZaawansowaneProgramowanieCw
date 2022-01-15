from Klasy.Develop import Developer
from Klasy.Dom import Dom
from Klasy.Mieszkanie import Mieszkanie
from Klasy.Zamowienie import Zamowienie

z1 = Zamowienie()
z1.set_id = 1
z1.set_id_parceli = [3, 4, 5]
z1.set_m2 = [12, 30, 40]
z1.set_cena = [3423.34, 12321.34, 7441.13]
z1.set_wlasciciel = "Radoslaw Kaczmarski"

print(z1)
print(z1.sum_m2())
print(z1.wart_zam())

print()

d1 = Developer(2, "Nazwa1", "Katowice", "Bogucicka")
print(d1)

print()

do1 = Dom(3, 60, "Katowice", "Chorzowska", "14")
print(do1)

print()

m1 = Mieszkanie(4, 70, "Korfantego", "Katwoice")
print(m1)
