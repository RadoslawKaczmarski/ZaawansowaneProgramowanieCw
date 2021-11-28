# Stworzyć funkcję, która przyjmuje 2 argumenty
# typu list i zwraca wynik typu list .
# Funkcja ma za zadanie złączyć przekazane
# listy w jedną, usunąć duplikaty, każdy
# element podnieść do potęgi 3 stopnia,
# a następnie zwrócić powstałą listę.'''


def listazada6(l1: list, l2: list) -> list:
    l1.extend(l2)
    return list(set([i ** 3 for i in l1]))


print(listazada6([1, 3, 3], [4, 5, 7]))
