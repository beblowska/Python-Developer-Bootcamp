# Prosty System Księgowy i Rozszerzenia

Ten zestaw projektów skupia się na projektach z zakresu zarządzania finansami oraz magazynem, które korzystają z różnych technologii i oferują różne możliwości. 
Oto krótka prezentacja każdego z projektów:

## Prosty System Księgowy

**Prosty System Księgowy** (Accountant1) to niewielki program do zarządzania saldem konta i magazynem produktów. 
Pozwala na dodawanie wpłat, zakup produktów oraz ich sprzedaż. Program obsługuje komunikaty błędów i rejestruje historię działań.

### Interakcja

Aby uruchomić program, po prostu uruchom go w terminalu lub konsoli. Program obsługuje następujące akcje:

- **saldo** - Pozwala na wprowadzenie zmiany na koncie oraz dodanie komentarza. Wyświetla bieżący stan salda.
- **zakup** - Pozwala na zakup produktów. Podaje się nazwę produktu, cenę jednostkową i ilość sztuk. Program odejmuje odpowiednią kwotę od salda i aktualizuje stan magazynu.
- **sprzedaż** - Pozwala na sprzedaż produktów. Podaje się nazwę produktu, cenę jednostkową i ilość sztuk. Program dodaje odpowiednią kwotę do salda i aktualizuje stan magazynu.
- **stop** - Zatrzymuje program.

## Przykładowe uruchomienie

python program.py saldo "Wpłata gotówki" 100

## Rozszerzenie Programu Accountant

**Rozszerzenie Programu Accountant** (Accountant2) to projekt rozszerzający możliwości Prostego Systemu Księgowego. 
Teraz program obsługuje różne operacje za pomocą komend wywołanych z linii poleceń. Program zapisuje wyniki i historię działań do pliku.

## Przykładowe uruchomienie

python saldo.py moj_plik.txt 100 "Wpłata gotówki"
python sprzedaz.py moj_plik.txt Laptop 1500 3

## Rozszerzenie Programu Accountant z Plikiem

**Rozszerzenie Programu Accountant** (Accountant3) z dodatkową możliwością zapisu i odczytu danych z plików. 
Teraz program jest wywoływany w taki sposób:

- python saldo.py <plik> <wartość> <komentarz>
- python sprzedaz.py <plik> <nazwa_produktu> <cena> <liczba_sprzedanych>
- python zakup.py <plik> <nazwa_produktu> <cena> <liczba_zakupionych>
- python konto.py <plik>
- python magazyn.py <plik> <nazwa_produktu1> <nazwa_produktu2> <nazwa_produktu3> ...
- python przeglad.py <plik>

## Przykładowe uruchomienie

python accountant.py nazwa_pliku.txt

## Webowa aplikacja programu Accountant

**Webowa aplikacja programu Accountant** (Flask) służy do zarządzania stanem magazynowym oraz księgowością za pomocą interfejsu webowego. 
Pobranie kodu, instalacja zależności i interakcja z aplikacją są dokładnie opisane w dokumentacji projektu.


Każdy z tych projektów ma swoje unikalne cechy i funkcje, a jednocześnie skupia się na zarządzaniu finansami i magazynem. 
Możesz wybrać projekt, który najlepiej odpowiada Twoim potrzebom i zapoznać się z jego dokumentacją, aby dowiedzieć się więcej. 
Wszystkie projekty oferują możliwość obsługi różnych operacji księgowych i zarządzania magazynem.

