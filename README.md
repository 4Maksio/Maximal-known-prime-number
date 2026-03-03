[PL] Język polski niżej

# [EN] Bottleneck detection

## on example of calculating, conversion and saving to file a maximal known prime number in Python

Maximal known prime number equals **2<sup>82589933</sup>-1** and has about _25 000 000_ digits.  

### The Goal

The base of a project is a simple python program that looks like this:

```py
with open("max_prime.txt", "w") as file:
    file.write(str(2**82589933-1))
```

It is made of three basic operations:
1. Calculating the number
    ```py
    2**82589933-1
    ```
2. Converting the number to string
    ```py
    str(...)
    ```
3. Writing down a string into a file
    ```py
    with open(file, mode) as name:
        name.write(...)
    ```
Created python script measures time of executing each step separately and a whole operation together for a comparison.

### The Execution

Python library ***timeit*** contain _timeit_ function returning time of _n_ execution of a given command. Library ***timeit*** also contain _repeat_ function which works as _timeit_ function but returns an array of *k* results of *n* continuous executions of a given command. Default number of execution is *1 000 000*.

For the sake of this project the number of repeats and executions is highly narrowed. It is due to long time of measurement a large number of operations the script is prepared to execute in about **5 minutes**. Numbers in script are as follows:

- calculating gets 10 repeats of 10 continuous executions;
- converting gets 2 repeats of 2 continuous executions;
- saving to file gets 12 repeats of 12 continuous executions;

As you can notice, the values are roots of 100 for calculating, 4 for converting and 144 for saving. For any scientific use the number of repetition should not be less than 30 as this is the smallest number considered as large in statistics. Number of continuous executions should be large for minimizing the averaging error, yet not too large to keep time of execution the test reasonable.

### The Results

Of all the results of repetitions, the smallest value is considerate the most valid because we aim for value closest to executing purely only the given code. The mean value of the chosen result estimates the real time of execution of the given code.

The final results from the script may differ depending on the computer and version of Python. Below are example outcomes that will be discussed in the summary.

---

Result of running the **original** script:

```
Calculating a value    |:  0.3431771900010062s  ( 1.63%)
Conversion to a string |: 20.606563099994673s   (97.63%)
Writing to a file      |:  0.15693291666684672s ( 0.74%)
Sum                    |: 21.106673206662528s
Whole instruction      |: 21.03366484999424s
```
`Time of execution: ~5min`

---

Result of running the script **modified** to run 30 repetitions of 10 continuous executions:

```
Calculating a value    |:  0.33947381999751086s ( 1.65%)
Conversion to a string |: 20.120145090000005s   (97.57%)
Writing to a file      |:  0.16159139999945182s ( 0.78%)
Sum                    |: 20.621210309996968s
Whole instruction      |: 20.595720189998975s
```
`Time of execution: ~4h`

---

Result of running the script **modified** to run a single execution:

```
Calculating a value    |:  0.4070445999968797s  ( 1.69%)
Conversion to a string |: 23.41581349997432s    (97.31%)
Writing to a file      |:  0.23963540000841022s ( 1.00%)
Sum                    |: 24.06249349997961s
Whole instruction      |: 23.442269999999553s
```
`Time of execution: ~1min`

---

### Summary

The bottleneck of the program is converting to string as it takes more than **97%** of program execution time. Number of repetitions and continuous runs to be done depend on the goal of time measurement.

- **Sanity check**: One run for every command or module is enough to see if time of execution is not excessive. Particularly useful in API performance testing;
- **Comparison of the solutions**: Many continuous runs should be done to ensure reliable comparison based on average time to execute. A few repetitions should be done to avoid compering non-reliable times;
- **Optimization or research**: At least 30 repetitions of as many as time allows continuous executions are needed to ensure the highest possible reliability and minimum error.

The `Sum` of the average code execution times from the fastest repetition contains cumulative averaging errors. The execution time of the entire program in comparison with the sum shows that the deviation of the sum of the average times of individual instructions decreases hyperbolically in relation to the average execution time of the whole program. This indicates that measurement errors are minimized by increasing the number of repetitions and/or successive executions. _I will leave it for later to investigate which factor is more important_.

The example of `30` repetitions of measuring the time of `100` continuous executions is generally the most accurate of the results presented. In it, the difference between the sum of the average times of the fastest measurements of individual elements and the average time of the fastest measurement of the whole is `0.03s`. For comparison, the same difference for a single execution in the example is `0.62s`. The ratio of these differences is approximately `1 : 21`, which means that the proportion of execution times for individual instructions when counting 30 results of 100 repetitions is **21 times more accurate** than for a single measurement. This is not important when finding such an obvious bottleneck, but it is worth noting for cases of recording more uniform measurements in a program. 

---
---

# [PL] Identyfikacja wąskiego gardła

## na przykładzie obliczania, konwersji i zapisu największej znanej liczby pierwszej in Pythonie

Największa znana liczba pierwsza wynosi **2<sup>82589933</sup>-1** i składa się z około _25 000 000_ cyfr.  

### Cel

Podstawą projektu jest prosty program wyglądający następująco:

```py
with open("max_prime.txt", "w") as file:
    file.write(str(2**82589933-1))
```

Składają się na niego:
1. Obliczenie wartości
    ```py
    2**82589933-1
    ```
2. Konwersja na łańcuch znaków
    ```py
    str(...)
    ```
3. Zapisanie do pliku
    ```py
    with open(file, mode) as name:
        name.write(...)
    ```

Stworzony skrypt mierzy czas wykonania każdego kroku z osobna oraz całości dla porównania.

### Wykonanie

Biblioteka Python ***timeit*** zawiera funkcję _timeit_, która zwraca czas *n* wykonań danego polecenia. Biblioteka ***timeit*** zawiera również funkcję _repeat_, która działa jak funkcja _timeit_, ale zwraca tablicę _k_ wyników _n_ wykonań danego polecenia. Domyślna liczba wykonań wynosi _1 000 000_.

Na potrzeby tego projektu ilość powtórzeń oraz wykonań jest mocno ograniczona, aby skrypt wykonał się w około **5 minut**. Ilość wykonań poszczególnych operacji w skrypcie wygląda następująco:

- obliczenia mają 10 powtórzeń po 10 wykonań;
- konwersja ma 2 powtórzenia po 2 wykonania;
- zapis ma 12 powtórzeń po 12 wykonań;

Jak można zauważyć, wartości są pierwiastkami 100 dla obliczeń, 4 dla konwersji oraz 144 dla zapisu. Dla wartości naukowej, liczba powtórzeń nie powinna być mniejsza niż 30, jako że jest to najmniejsza wartość uznawana w statystyce jako duża. Ilość wykonań powinna być duża w celu minimalizacji błędów uśredniania, ale nie zbyt duża, żeby utrzymać sensowny czas wykonania.

### Wyniki

Spośród wszystkich serii wykonań wybierany jest najniższy czas ze względu na chęć uzyskania czasu najbliższego wykonaniu tylko i wyłącznie zadanego kodu. Średnia wartość wybranego wyniku serii przybliża rzeczywisty czas wykonania kodu.

Ostateczny wynik skryptu będzie różnił się w zależności od komputera i wersji Pythona. Poniższe wyniki zostaną omówione w podsumowaniu.

---

Wyniki uruchomienia **oryginalnego** skryptu:

```
Obliczenie wartości |:  0.3431771900010062s  ( 1.63%)
Konwersja na string |: 20.606563099994673s   (97.63%)
Zapis do pliku      |:  0.15693291666684672s ( 0.74%)
Suma                |: 21.106673206662528s
Całość              |: 21.03366484999424s
```
`Czas wykonania: ~5min`

---

Wyniki uruchomienia skryptu **zmodyfikowanego**, mierzącego 30 powtórzeń po 10 wykonań:

```
Obliczenie wartości |:  0.33947381999751086s ( 1.65%)
Konwersja na string |: 20.120145090000005s   (97.57%)
Zapis do pliku      |:  0.16159139999945182s ( 0.78%)
Suma                |: 20.621210309996968s
Całość              |: 20.595720189998975s
```
`Czas wykonania: ~4h`

---

Wyniki uruchomienia skryptu **zmodyfikowanego**, mierzącego pojedyncze wykonanie:

```
Obliczenie wartości |:  0.4070445999968797s  ( 1.69%)
Konwersja na string |: 23.41581349997432s    (97.31%)
Zapis do pliku      |:  0.23963540000841022s ( 1.00%)
Suma                |: 24.06249349997961s
Całość              |: 23.442269999999553s
```
`Czas wykonania: ~1min`

---

### Podsumowanie

Wąskim gardłem programu jest konwersja na string, która zajmuje więcej niż **97%** czasu wykonania. Ilość powtórzeń oraz kolejnych wykonań zależy od celu mierzenia czasu.

- **Sprawdzanie poprawności**: Pojedyncze wykonanie każdej komendy w module lub całego sprawdzanego polecenia jest wystarczające, aby zauważyć nadmierny czas wykonywania. Szczególnie przydatne przy testach wydajnościowych API;
- **Porównywanie rozwiązań**: Wiele kolejnych uruchomień powinno zostać wykonanych, aby zapewnić rzetelne porównanie na podstawie średniego czasu wykonania. Kilka przebiegów powinno zostać wykonanych, aby uniknąć porównywania niemiarodajnych wyników;
- **Optymalizacja lub badania**: Co najmniej 30 powtórzeń tylu kolejnych wykonań, na ile czas pozwoli zapewni możliwie największą dokładność i najmniejszy błąd.

`Suma` średnich czasów wykonywania kodu z najszybszego powtórzenia zawiera skumulowane błędy uśredniania. Czas wykonania programu w całości w zestawieniu z sumą pozwala zauważyć, że odchylenie sumy uśredniania czasów pojedynczych instrukcji maleje hiperbolicznie względem średniego czasu wykonania programu. Wskazuje to na fakt minimalizacji błędów pomiarowych przez zwiększanie ilości powtórzeń i/lub kolejnych wykonań. _Który czynnik ma większe znaczenie zostawiam do zbadania innym razem_.

Przykład `30` powtórzeń mierzenia czasu `100` wykonań jest w ogólności najdokładniejszy z przedstawionych wyników. W nim samym różnica między sumą średnich czasów najszybszych pomiarów poszczególnych elementów, a średnim czasem najszybszego pomiaru całości wynosi `0.03s`. Dla porównania, ta sama różnica dla przykładowego pojedynczego wykonania wynosi `0.62s`. Stosunek tych różnic wynosi w przybliżeniu `1 : 21`, a znaczy tyle, że proporcja czasów wykonywania poszczególnych instrukcji w przypadku liczenia 30 wyników 100 powtórzeń jest **21 razy dokładniejsza** od pojedynczego pomiaru. Nie ma to znaczenia w przypadku znalezienia tak oczywistego wąskiego gardła, ale jest warte odnotowania dla przypadków rejestrowania bardziej jednolitych pomiarów w jakimś programie. 
