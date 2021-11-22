'''2. Stworzyć następujące klasy:


Library (klasa opisująca bibliotekę), posiadająca pola:
city
street
zip_code
open_hours (str)
phone
'''




class Library:
    def __init__(self,city,street,zip_code,open_hours:str,phone):
        self.city=city
        self.street=street
        self.zip_code=zip_code
        self.open_hours=open_hours
        self.phone=phone

    def __str__(self):
        return f"CITY: {self.city} ; STREET: {self.street} ; ZIP_CODE: {self.zip_code} ; OPEN_HOURS: {self.open_hours} ; PHONE:{self.phone}\n"

'''Order (klasa opisująca zamówienie), posiadająca pola:
employee
student
books
order_date'''

class Order:
    def __init__(self,employee,student,books,order_date):
        self.employee=employee
        self.student=student
        self.books=books
        self.order_date=order_date

    def __str__(self):
        return f"EMPLOYEE {self.employee} ; STUDENT: {self.student} ; BOOKS: {self.books} ; ORDER_DATE: {self.order_date}\n"

'''Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
first_name
last_name
hire_date
birth_date
city
street
zip_code
phone'''


class Employee:
    def __init__(self,first_name,last_name,hire_date,birth_date,city,street,zip_code,phone):
        self.first_name=first_name
        self.last_name=last_name
        self.hire_date=hire_date
        self.birth_date=birth_date
        self.city=city
        self.street=street
        self.zip_code=zip_code
        self.phone=phone

    def __str__(self):
        return f"F_NAME: {self.first_name} ; L_NAME: {self.last_name} ; H_DATE: {self.hire_date} ; B_DATE: {self.birth_date} ; PHONE:{self.phone} " \
                      f"CITY: {self.city} ; STREET: {self.street} ; ZIP_CODE: {self.zip_code} ; PHONE:{self.phone}\n"


'''Book (klasa opisująca książkę), posiadająca pola
library
publication_date
author_name
author_surname
number_of_pages'''

class Book:
    def __init__(self,library,publication_date,author_name,author_surname,number_of_pages):
        self.library=library
        self.publication_date=publication_date
        self.author_name=author_name
        self.author_surname=author_surname
        self.number_of_pages=number_of_pages

    def __str__(self):
        return f"LIBRARY: {self.library} ; PUB_DATE: {self.publication_date} ; AUTOR_NAME: {self.author_name} ;AUTOR_SURNAME: {self.author_surname} ; NUMER_OF_PAGES:{self.number_of_pages}\n"

'''Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3 studentów, oraz 2 zamówienia.
Wyświetlić oba zamówienia ( print )'''

lib1=Library("Katowice","Zamkowa","41-910","10","32-286-34-22")
print(lib1)
lib2=Library("Bytom","Do koła","41-910","12","32-286-34-22")
print(lib2)

ks1=Book(lib1,"10.10.2000","Jan","Kowalski","100")
print(ks1)
ks2=Book(lib1,"10.10.2001","Maciej","Kowalski","120")
print(ks2)
ks3=Book(lib2,"10.10.2003","Mikołaj","Nowak","80")
print(ks3)
ks4=Book(lib2,"10.10.2009","Jan","Adam","70")
print(ks4)
ks5=Book(lib1,"10.10.2012","Artur","Mróz","140")
print(ks5)

pr1=Employee("Mikołaj","Mróz","10.10.2014","08.03.1990","Bytom","Do koła","41-902","345-236-129")
pr2=Employee("Adam","Nowak","10.11.2014","14.05.1992","Bytom","Kołobrzeska","41-902","367-123-127")
pr3=Employee("Kamil","Kowalski","10.12.2014","10.06.1993","Bytom","Chorzowska","41-902","395-798-800")
print(pr1)
print(pr2)
print(pr3)

class Student:
    def __init__(self,name:str,marks:int):
        self.name=name
        self.marks=marks

    def is_passed(self):
        if self.marks>50:
            return True
        else:
            return False
    def __str__(self):
        return f"NAME: {self.name} ; MARKS :{self.marks}\n"

stud1=Student("Radek",40)
stud2=Student("Wojtek",70)
stud3=Student("Jan",90)
print(stud1)
print(stud2)
print(stud3)


zam1=Order(pr1,stud1,ks1,"10.07.2021")
zam2=Order(pr2,stud2,ks4,"03.04.2022")

print(zam1)
print(zam2)
