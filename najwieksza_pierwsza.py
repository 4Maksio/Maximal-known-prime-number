'''
(2**82589933)-1
'''
from os import system
from sys import set_int_max_str_digits
import numpy as np

def int_to_string(integer):
    counter = 1
    returning_str = ""
    zero = ord('0')
    system("cls")
    print("Liczba ta ma około 25 000 000 znaków")
    while integer > 0:
        if counter%100 == 0:
            print(f"Przekonwertowano {counter} znaków")
        d = chr(integer % 10 + zero)
        integer = integer//10
        returning_str = d+returning_str
        counter+=1
    return returning_str


set_int_max_str_digits(25000000)

wynik = i = 1

p1 = 2**3
system("cls")
print(f"Policzono {i}. rząd")
i+=1
p2 = 2**30
system("cls")
print(f"Policzono {i}. rząd")
i+=1
p3 = 2**900
system("cls")
print(f"Policzono {i}. rząd")
i+=1
p4 = 2**9000
system("cls")
print(f"Policzono {i}. rząd")
i+=1
p5 = 2**80000
system("cls")
print(f"Policzono {i}. rząd")
i+=1
p6 = 2**500000
system("cls")
print(f"Policzono {i}. rząd")
i+=1
p7 = 2**2000000
system("cls")
print(f"Policzono {i}. rząd")
i+=1
p8 = 2**80000000
system("cls")
print(f"Policzono {i}. rząd")

krotka = (p1,p2,p3,p4,p5,p6,p7,p8)
i=1

for p in krotka:
    system("cls")
    print(f"Zmnażanie {i}/8")
    i+=1
    wynik *= p

wynik -= 1

system("cls")
print(f"Rozpoczęto konwersję z liczby na znaki")

wynik_str = int_to_string(wynik)


system("cls")
print(f"Rozpoczęto zapis do pliku")

with open("najwieksza_pierwsza.txt", "w") as plik:
    plik.write(wynik_str)

system("cls")
print("Plik z największą znalezioną liczbą pierwszą gotowy.")