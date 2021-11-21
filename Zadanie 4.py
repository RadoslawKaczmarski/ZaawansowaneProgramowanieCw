'''Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
jako typ logiczny bool'''

def CoWieksze(liczba1:int,liczba2:int,liczba3:int)-> bool:
    if liczba1+liczba2 >= liczba3:
        return True
    else:
        return False

print(CoWieksze(1,2,1))
