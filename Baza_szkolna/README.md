# Baza Szkolna

Program "Baza Szkolna" umożliwia zarządzanie danymi szkolnymi dla trzech typów użytkowników: Wychowawcy, Nauczyciela i Ucznia.

# Intreakcja

1. Uruchom program za pomocą polecenia:

   ```bash
   python bazaszkolna.py <phrase>

  Gdzie `<phrase>` to jedno z poniższych poleceń: "uczeń", "nauczyciel", "wychowawca" lub "koniec".

2. Wprowadź typ użytkownika i Imię i Nazwisko. Możliwe typy użytkowników to:
- "uczeń": Wprowadź jedną linię z nazwą klasy (np. "3C").
- "nauczyciel": Wprowadź linię z nazwą przedmiotu, a następnie w kolejnych liniach nazwy klas, aż do otrzymania pustej linii.
- "wychowawca": Wprowadź w kolejnych liniach nazwy klas, które prowadzi wychowawca, aż do pustej linii.
- "koniec": Zakończ program.

3. Program zinterpretuje wprowadzone dane i wykona odpowiednie polecenie, w zależności od `<phrase>`.

# Przykłady użycia

- `python bazaszkolna.py uczeń`
Program zapyta o nazwę klasy, a następnie wyświetli wychowawcę i uczniów tej klasy.

- `python bazaszkolna.py nauczyciel`
Program zapyta o nazwę przedmiotu i klasy prowadzone przez nauczyciela, a następnie wyświetli wychowawców tych klas.

- `python bazaszkolna.py wychowawca`
Program zapyta o klasy prowadzone przez wychowawcę, a następnie wyświetli uczniów tych klas.

- `python bazaszkolna.py koniec`
Program zakończy działanie.
