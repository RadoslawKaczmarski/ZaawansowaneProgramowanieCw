
# b.Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych
# liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci. Zadanie
# należy wykonać w 2 wersjach:
# i. Wykorzystując pętle for .
# ii. Wykorzystując listę skłądaną.


def pomnozliczby_1(liczby: list):
    return [liczba*2 for liczba in liczby]


def pomnozliczby_2(liczby: list):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba*2)
    return wynik


pomnozliczby_1([1, 2, 3, 4, 5])
pomnozliczby_2([1, 2, 3, 4, 5])
