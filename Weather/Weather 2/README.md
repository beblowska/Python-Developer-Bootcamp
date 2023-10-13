# Weather2

Program "Weather2" został stworzony w celu dostarczenia danych pogodowych na podstawie dostarczonego klucza API.
Możesz pobierać prognozy pogody dla różnych dat, a także uzyskiwać dostęp do zcache'owanych danych pogodowych oraz wylistować dostępne daty.

# Konstruktor

1. Aby urochomic program musisz przekazać swój klucz API:

   ```bash
   `wf = WeatherForecast(api_key)`

# Interakcja

Klasa Weather2 umożliwia wykorzystanie poniższych funkcjonalności:

1. **wf[date]** - Zwraca odpowiedź na temat pogody dla podanej daty.

2. **wf.items()** - Zwraca generator tupli w formacie (data, pogoda) dla już zcache’owanych rezultatów.

3. **wf** - Działa jako iterator, zwracając wszystkie daty, dla których znana jest pogoda.

# Funkcje 

1. **add_api():** Wykonuje żądanie do API pogodowego i zapisuje odpowiedź do pliku "form_api.json".

2. **json_file():** Odczytuje dane zapisane w pliku "from_api.json".

3. **read_cache(date):** Wczytuje dane pogodowe z pliku "forecast.csv" i zwraca informację o pogodzie na podaną datę.

4. **forecast_csv():** Aktualizuje plik "forecast.csv" z zcache'owanymi danymi pogodowymi.

5. **from_dict():** Odczytuje dane z pliku "from_api.json" i zapisuje do zcache'owanych danych.

6. **check_csv(date):** Sprawdza, czy dla danej daty istnieją zcache'owane dane pogodowe.

# Przykładowe użycie

```bash
`wf = WeatherForcast(api_key=sys.argv[1])

if date in wf.cached:
    wf.from_dict()
    wf[date]
else:
    if date not in wf.cached:
        wf.add_api()
        wf.from_dict()
        wf[date]
        wf.read_cache(date)

print(f"Podana data: {date}")
print("Pogoda:", wf[date])
print(wf.read_cache(date))

print("Pogoda na różne daty:")
for data, pogoda in wf.items():
    print(data, pogoda)

print("Dostępne daty z pogodą:")
for data in wf:
    print(data)`

