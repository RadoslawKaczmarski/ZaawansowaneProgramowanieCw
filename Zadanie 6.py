'''Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.'''

def ListaZada6(L1:list,L2:list)->list:
    L1.extend(L2)
    return list(set([i**3 for i in L1 ]))
print(ListaZada6([1,3,3],[4,5,7]))