# Rozszerzenie Programu Accountant

Program Accountant został rozszerzony o możliwość zapisu i odczytu danych z plików. Teraz program jest wywoływany w następujący sposób:

- 1) `python saldo.py <plik> <int wartość> <str komentarz>`
- 2) `python sprzedaz.py <plik> <str identyfikator produktu> <int cena> <int liczba sprzedanych>`
- 3) `python zakup.py <plik> <str identyfikator produktu> <int cena> <int liczba zakupionych>`
- 4) `python konto.py <plik>`
- 5) `python magazyn.py <plik> <str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...`
- 6) `python przeglad.py <plik>`

Wszystkie operacje są teraz obsługiwane przez obiekt klasy Manager, a dane są przechowywane wewnątrz tego obiektu. Nie ma żadnych zmiennych globalnych.

## Interakcja

Aby korzystać z programu, uruchom odpowiedni skrypt z linii poleceń, podając odpowiednie argumenty. Program zapisuje wyniki i historię działań do pliku o nazwie `<plik>`.

```bash
python accountant.py nazwa_pliku.txt
