'''
b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych
liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci. Zadanie
należy wykonać w 2 wersjach:
i. Wykorzystując pętle for .
ii. Wykorzystując listę skłądaną.
'''

def PomnozLiczby_1(liczby:list):
    return [liczba*2 for liczba in liczby]

def PomnozLiczby_2(liczby:list):
    wynik=[]
    for liczba in liczby:
        wynik.append(liczba*2)
    return wynik


PomnozLiczby_1([1,2,3,4,5])
#PomnozLiczby_2([1,2,3,4,5])