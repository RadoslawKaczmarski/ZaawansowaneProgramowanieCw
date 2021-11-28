# Stworzyć funkcję, która będzie sprawdzała
# czy przekazana liczba w parametrze jest
# parzysta i zwróci tą informację jako
# typ logiczny bool ( True / False ).
# Należy uruchomić funkcję, wynik wykonania
# zapisać do zmiennej, a następnie
# wykorzystując warunek logiczny
# wyświetlić prawidłowy tekst
# "Liczba parzysta" "Liczba nieparzysta"

def czyparzysta(liczba: int) -> bool:
    if liczba % 2 == 0:
        return True
    else:
        return False


zad3 = czyparzysta(7)
if zad3 is True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
