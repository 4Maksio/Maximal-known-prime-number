'''
(2**82589933)-1
'''
from os import system
from sys import set_int_max_str_digits

def int_to_string(int):
    i = 1
    ret = ""
    while int > 0:
        if i%100==0:
            system("cls")
            print("Liczba ta ma około 25 000 000 znaków")
            print(f"Przekonwertowano {i} znaków")
        d = int % 10
        int = int//10
        match d:
            case 0:
                ret = '0'+ret
            case 1:
                ret = '1'+ret
            case 2:
                ret = '2'+ret
            case 3:
                ret = '3'+ret
            case 4:
                ret = '4'+ret
            case 5:
                ret = '5'+ret
            case 6:
                ret = '6'+ret
            case 7:
                ret = '7'+ret
            case 8:
                ret = '8'+ret
            case 9:
                ret = '9'+ret
        i+=1
    return ret


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
    print(f"Spotęgowano!")
    print(f"Zmnażanie {i}/8")
    i+=1
    wynik *= p


system("cls")
print(f"Rozpoczęto konwersję z lczby na znaki")

wynik = int_to_string(wynik)


system("cls")
print(f"Rozpoczęto zapis do pliku")

with open("najwieksza_pierwsza.txt", "a") as plik:
    plik.write(wynik)

system("cls")
print("Plik z największą znalezioną liczbą pierwszą gotowy.")