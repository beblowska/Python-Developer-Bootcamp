# Prosty System Księgowy

Prosty System Księgowy to niewielki program do zarządzania saldem konta i magazynem produktów. Pozwala na dodawanie wpłat, zakup produktów oraz ich sprzedaż.
Program obsługuje komunikaty błędów i rejestruje historię działań.

## Intreakcja

Aby uruchomić program, po prostu uruchom go w terminalu lub konsoli. Program obsługuje następujące akcje:

1. **saldo** - Pozwala na wprowadzenie zmiany na koncie oraz dodanie komentarza. Wyświetla bieżący stan salda.

2. **zakup** - Pozwala na zakup produktów. Podaje się nazwę produktu, cenę jednostkową i ilość sztuk. Program odejmuje odpowiednią kwotę od salda i aktualizuje stan magazynu.

3. **sprzedaż** - Pozwala na sprzedaż produktów. Podaje się nazwę produktu, cenę jednostkową i ilość sztuk. Program dodaje odpowiednią kwotę do salda i aktualizuje stan magazynu.

4. **stop** - Zatrzymuje program.

Możesz również korzystać z programu z linii poleceń, podając odpowiednie argumenty, np.:

```bash
python program.py zakup "Produkt A" 10 5
