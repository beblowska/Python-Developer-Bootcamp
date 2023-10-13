# Weather.py

Program "Weather" służy do sprawdzania, czy danego dnia będzie padać deszcz. Program korzysta z dostępnych API do prognoz pogody.

# Interakcja

1. Uruchom program za pomocą polecenia:

   ```bash
   `python weather.py <<klucz_api>> [data]`

  Gdzie `<<klucz_api>>` to Twój klucz API do usługi prognoz pogody, a `data` (opcjonalne) to data w formacie "YYYY-MM-DD". Jeśli nie podasz daty, program automatycznie użyje następnego dnia.

2. Program sprawdzi prognozę pogody na podstawie dostarczonej daty i klucza API.

**Możliwe odpowiedzi programu:**

- "Będzie padać": Jeśli prognoza wskazuje, że tego dnia będzie deszcz.
- "Nie będzie padać": Jeśli prognoza mówi, że nie będzie opadów tego dnia.
- "Nie wiem": Jeśli program nie może określić prognozy lub napotkał problem z API.

**Zachowanie programu:**

- Program nie przechowuje klucza API w kodzie. Klucz API powinien być dostarczany jako argument wiersza poleceń.

- Aby uniknąć nadmiernego korzystania z limitu zapytań do API, program zapamiętuje wyniki prognoz w pliku tekstowym. Jeśli wynik dla danej daty jest już znany, program użyje zapisanej prognozy zamiast pytać ponownie API.

**Pliki w rozwiązaniu:**

Rozwiązanie powinno zawierać plik `weather.py`, który jest głównym programem, oraz plik `requirements.txt`, który zawiera zależności programu.

Upewnij się, że dostarczyłeś własny klucz API do usługi prognoz pogody jako argument uruchomieniowy programu. Program będzie działać zgodnie z dostarczonymi danymi i zwróci odpowiedź na podstawie prognozy pogody.


