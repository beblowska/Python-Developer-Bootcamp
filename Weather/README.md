# Zadania: Weather Forecast

W tym repozytorium znajdziesz dwa zadania związane z prognozowaniem pogody:

1. Program Weather1 - weather.py
3. Program Weather2 - weather2.py

# Program Weather1

**Opis**

Program Weather1 (weather.py) to narzędzie do sprawdzania prognozy pogody na podstawie dostępnego API. 
Możesz go uruchomić, aby dowiedzieć się, czy danego dnia będzie padać deszcz lub śnieg.

**Urochomienie**

Program można uruchomić na dwa sposoby:

1. Podając klucz API oraz datę (w formacie YYYY-MM-DD) jako argumenty wiersza poleceń. Na przykład:

   ```bash
   python weather.py <<klucz_api>> 2023-09-29
     lub
   ```bash
   python weather.py <<klucz_api>>

**Funkcje**

- Program korzysta z dostępnych API do prognozy pogody (np. z RapidAPI).
- Lokalizacja (miasto) jest wpisana na stałe w kodzie, ale można ją dostosować.
- Aby uniknąć nadmiernego zużycia kwoty zapytań do API, program zapamiętuje wynik dla już sprawdzonych dni w pliku tekstowym. Jeśli wynik jest już znany, program zwraca odpowiedź na podstawie pliku.

**Wynik**

Program wydrukuje na standardowe wyjście jedno z trzech możliwych komunikatów: 
- "Będzie padać"
- "Nie będzie padać"
- "Nie wiem"

# Program Weather2

**Opis**

Program Weather2 to moduł, który umożliwia tworzenie instancji klasy do sprawdzania prognozy pogody na podstawie dostępnego API. 
Ta klasa jest wykorzystywana w Programie Weather1.

**Funkcje**

Obiekt klasy WeatherForecast odpowiada na następujące wywołania:
- wf[date] - zwraca odpowiedź na temat pogody dla podanej daty.
- wf.items() - zwraca generator tupli w formacie (data, pogoda) dla już zcache’owanych rezultatów przy wywołaniu.
- wf - to iterator zwracający wszystkie daty, dla których znana jest pogoda.

**Wymagania**

Do uruchomienia programu potrzebujesz zainstalowanej biblioteki requests. Możesz to zrobić, używając polecenia:

```bash
pip install -r requirements.txt

