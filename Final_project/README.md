# Kalendarz w django

Projekt "Kalendarz w Django" to moja ostatnia praca z zakresu programowania webowego. 
To pełnoprawna aplikacja kalendarza stworzona przy użyciu frameworku Django. 
Projekt ten jest wyjątkowy, ponieważ został stworzony od podstaw, bazując na moich pomysłach i zdobytej wiedzy podczas kursu.

# Technologie

- **Python** - Język programowania wykorzystany do tworzenia backendu aplikacji.
- **Django** - Potężny framework webowy, który umożliwił mi budowę aplikacji internetowej.
- **SQLAlchemy** - Baza danych użyta do przechowywania danych kalendarza.
- **HTML, CSS, JavaScript** - Technologie front-endowe, które pomogły w tworzeniu atrakcyjnego interfejsu użytkownika.

# Główne funkcje

1. **Zarządzanie wydarzeniami** - Użukownicy mogą tworzyć, edytować i usuwać wydarzenia w kalendarzu.
2. **Ustawianie przypomnień** - Dla ważnych wydarzeń użytkownicy mogą ustawić przypomnienia, aby nie przegapić żadnej okazji.
3. **Współdzielenie wydarzeń** - Istnieje opcja dzielenia się wydarzeniami z innymi użytkownikami.
4. **Odzyskiwanie hasła** - Jeśli użytkownik zapomni hasła, może skorzystać z funkcji odzyskiwania hasła.
5. **Wymogi hasła** - Dla zwiększenia bezpieczeństwa istnieją wymogi dotyczące tworzenia hasła.

# Uruchomienie projektu

1. Zainstaluj wymagane biblioteki i zależności, korzystając z polecenia:

   ```bash
   pip install -r requirements.txt

2. Przejdź do folderu projektu i wykonaj migracje bazy danych:

   ```bash
   python manage.py makemigrations
   python manage.py migrate

3. Uruchom serwer deweloperski Django:

   ```bash
   python manage.py runserver

4. Otwórz przeglądarkę i wejdź na adres `http://127.0.0.1:8000/`.
   
