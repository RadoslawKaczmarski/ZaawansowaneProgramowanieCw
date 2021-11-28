# Stworzyć klasę Student , która posiada 2 parametry
# (name i marks) oraz jedną metodę is_passed, która zwraca wartość
# logiczną, pozytywną gdy ocena jest > 50 w
# przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe
# obiekty klasy, tak aby dla pierwszego obiektu
# metoda zwracała true , a dla drugiego false.


class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.marks > 50:
            return True
        else:
            return False


a1 = Student("Radek", 30)
print(a1.is_passed())

a2 = Student("Maciej", 60)
print(a2.is_passed())
