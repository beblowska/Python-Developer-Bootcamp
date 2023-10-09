# Webowa aplikacja programu Accountant

Aplikacja webowa służy do zarządzania stanem magazynowym oraz księgowością.

## Pobranie kodu

   Skopiuj dostarczony kod i zapisz go do pliku o nazwie np. `main.py`.

## Instalacja zależności

   Aplikacja korzysta z frameworka Flask oraz SQLite jako bazy danych. Upewnij się, że masz te zależności zainstalowane. Jeśli nie, możesz zainstalować je za pomocą pip:

  `pip install Flask`

   Teraz aplikacja będzie dostępna w przeglądarce pod adresem `http://localhost:5000`.

## Interakcja

   Po uruchomieniu aplikacji zostaniesz przekierowany na stronę główną. Na tej stronie znajdziesz informacje o aktualnym stanie magazynu oraz saldzie.

    - Formularz zakupu:
        Wypełnij pola: nazwa produktu, cena jednostkowa, liczba sztuk.
        Kliknij przycisk "Zakup".
        Jeśli dane są poprawne, stan magazynu zostanie zaktualizowany.

    - Formularz sprzedaży:
        Wypełnij pola: nazwa produktu, cena jednostkowa, liczba sztuk.
        Kliknij przycisk "Sprzedaż".
        Jeśli dane są poprawne, stan magazynu zostanie zaktualizowany.

    - Formularz zmiany salda:
        Wypełnij pola: komentarz, wartość (tylko liczba).
        Kliknij przycisk "Zmień saldo".
        Jeśli dane są poprawne, saldo zostanie zaktualizowane.

    - Podstrona Historia
      Aby przejść do podstrony Historia, przejdź pod adres `http://localhost:5000/historia`.

    - Wyszukiwanie po dacie:
      Możesz podać dwa opcjonalne parametry w adresie, np. `http://localhost:5000/historia/line_from/line_to`. Jeśli nie podasz tych parametrów, wyświetli się cała historia działań.

## Zapis danych

   Aplikacja zapisuje dane w bazie danych SQLite zamiast w pliku tekstowym. Baza danych zostanie utworzona automatycznie. Nie musisz dostarczać pliku bazy danych, aplikacja go zarządza.
   
