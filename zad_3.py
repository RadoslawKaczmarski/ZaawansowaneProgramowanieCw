# c. Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane
# wykorzystanie funkcji range ), która wyświetla jedynie parzyste elementy.


def parzyste(liczby: list):
    for i in range(10):
        if liczby[i] % 2 == 0:
            print(liczby[i])


parzyste([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
