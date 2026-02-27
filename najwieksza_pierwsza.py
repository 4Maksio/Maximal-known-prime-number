'''
Program składa się z trzech zasadniczych części
1. Obliczenie liczby
2. Konwersja liczby na string
3. Zapis liczby do pliku

Sprawdzany jest czas każdej z tych operacji oraz dla porównania czas wykonania kodu w jednej linijce.

Maksymalna znana liczba pierwsza wynosi 2**82589933 - 1 i ma ~25 000 000 cyfr
'''

import timeit as ti
from sys import set_int_max_str_digits
set_int_max_str_digits(25000000)

print("---")
print("PL: Program powinien wykonywać się <5min")
print("EN: Program should be running for <5min")
print("---")

# Funkcja sprawdzająca czas, informująca użytkownika o bieżącym postępie
def measure_info(code, msg_pl, msg_en, number, repeat):
    print(f"PL: Obliczanie czasu {msg_pl} | EN: Calculating time of {msg_en}")
    czas = ti.repeat(code, globals=globals(), number=number, repeat=repeat)
    print(f"PL: Minimalny wynik dla {repeat} powtórzeń {number} wielokrotności:")
    print(f"EN: Minimal result for {repeat} repetitions of {number} cumulative runs:")
    print(f"{min(czas)} s")
    print("---")
    return min(czas)/number
    
# 1. Obliczanie
obliczanie = measure_info("x=2**82589933-1", "obliczenia", "calculation", 10, 10)

# 2. Konwersja
value = 2**82589933-1
konwersja = measure_info("str(value)", "konwersji", "conversion", 2, 2)

# 3. Zapis do pliku
value_str = str(value)
zapis = measure_info('with open("max_prime.txt", "w") as plik: plik.write(value_str)', "zapisu do pliku", "writing to file", 12, 12)

# 4. Całość w jednej linijce
calosc = measure_info('with open("max_prime.txt", "w") as plik: plik.write(str(2**82589933-1))', "jednoliniowej instrukcji", "single-line instruction", 2, 2)

# Podsumowanie
suma = obliczanie + konwersja + zapis

print("--- --- ---")
print(f"PL: Obliczenie wartości | EN: Calculating a value |: {obliczanie}s ({(obliczanie*100/suma):.2f}%)")
print(f"PL: Konwersja na string | EN: Conversion to a string |: {konwersja}s ({(konwersja*100/suma):.2f}%)")
print(f"PL: Zapis do pliku | EN: Writing to a file |: {zapis}s ({(zapis*100/suma):.2f}%)")
print(f"PL: Suma | EN: Sum |: {suma}s")
print(f"PL: Jednoliniowa instrukcja | EN: single-line instruction |: {calosc}s")