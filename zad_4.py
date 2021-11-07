'''Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane
wykorzystanie funkcji range ), która wyświetla co drugi element.'''

def CoDrugi(liczby:list):
    for i in range(10):
        if i%2==0:
            print(liczby[i])

CoDrugi([1,2,3,4,5,6,7,8,9,10])