# Rozszerzenie Programu Accountant

Program pozwala na zarządzanie finansami oraz magazynem i obsługuje różne operacje za pomocą komend wywołanych z linii poleceń. 
Poniżej znajdziesz instrukcje dotyczące uruchamiania i korzystania z programu:

  - 1) `python saldo.py <plik> <wartość> <komentarz>` - Dodaje lub odejmuje określoną wartość do/z salda oraz dodaje komentarz. Wartość i komentarz są opcjonalne.
  - 2) `python sprzedaz.py <plik> <nazwa_produktu> <cena> <liczba_sprzedanych>` - Rejestruje sprzedaż produktu.
  - 3) `python zakup.py <plik> <nazwa_produktu> <cena> <liczba_zakupionych>` - Rejestruje zakup produktu.
  - 4) `python konto.py <plik>` - Wyświetla aktualny stan konta.
  - 5) `python magazyn.py <plik> <nazwa_produktu1> <nazwa_produktu2> <nazwa_produktu3> ...` - Wyświetla stan magazynu.
  - 6) `python przeglad.py <plik>` - Wyświetla historię działań.

**Ważne:** Zawsze należy podać nazwę pliku jako pierwszy argument, a resztę argumentów w odpowiedniej kolejności, zgodnie z opisem powyżej.

## Intreakcja

Po wprowadzeniu komendy i jej parametrów, program zarejestruje odpowiednią operację i wyświetli wynik na ekranie. Przykłady komend:

  - `python saldo.py moj_plik.txt 100 "Wpłata gotówki"` - Dodaje 100 do salda z komentarzem.
  - `python sprzedaz.py moj_plik.txt Laptop 1500 3` - Rejestruje sprzedaż 3 sztuk laptopa po cenie 1500 jednostek.

## Zapis danych

Program zapisuje historię operacji do pliku, który został podany jako argument wywołania (nazwa_pliku.txt). Wszystkie operacje są zapisywane w formie tekstu.

Po uruchomieniu programu można również używać komendy `python przeglad.py <plik>` do przeglądania historii działań wcześniej zapisanych w pliku.
