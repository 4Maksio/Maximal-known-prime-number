'''
(2**82589933)-1
'''
from sys import set_int_max_str_digits
import timeit as ti

set_int_max_str_digits(25000000)

print("Obliczanie oraz wykonywanie: czas obliczeń")
czas_obliczen = ti.timeit("x=2**82589933-1", number=10)
wynik = 2**82589933-1
print("Zakończono")
print(f"Czas obliczenia liczby 10 razy: {czas_obliczen} s")

print("Obliczanie oraz wykonywanie: konwersja na string")
czas_konwersji = ti.timeit("str(wynik)", globals=globals(), number=1)
wynik_str = str(wynik)
print("Zakończono")
print(f"Czas konwersji liczby 1 raz: {czas_konwersji} s")

print("Obliczanie oraz wykonywanie: zapis do pliku")
czas_zapisu = ti.timeit('with open("najwieksza_pierwsza.txt", "w") as plik: plik.write(wynik_str)', globals=globals(), number=100)
with open("najwieksza_pierwsza.txt", "w") as plik:
    plik.write(wynik_str)
print("Zakończono")
print(f"Czas zapisania liczby 100 razy: {czas_zapisu} s")

print("--- --- --- Podsumowanie --- --- ---")
print(f"Czas obliczenia liczby 10 razy: {czas_obliczen} s")
print(f"Czas konwersji liczby 1 raz: {czas_konwersji} s")
print(f"Czas zapisania liczby 100 razy: {czas_zapisu} s")