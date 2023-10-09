import sys
warehouse ={}
logs = []
available_actions = ["saldo", "zakup", "sprzedaż", "stop"]
balance = 0

while True:                                                                                 # SALDO INPUT
    action_type = input("Podaj akcję: ")
    if action_type not in available_actions:
        print("Błędna akcja. Dopuszczalne akcje: {}".format(available_actions))
        continue
    if action_type == "saldo":
        account_change = int(input("Zmiana na koncie w [gr]: "))
        if account_change:
            balance += account_change
        comment = str(input("Komentarz do wprowadzonych zmian: "))
        print("Saldo wynosi {}".format(balance))
        logs.append([action_type, account_change, comment])
        print(logs)

    if action_type == "zakup":                                                              # ZAKUP INPUT
        product_name = str(input("Podaj identyfikator produktu: "))
        product_price = int(input("Podaj cenę jednostkową produktu: "))
        product_qty = int(input("Podaj ilość sztuk: "))
        if product_price < 0:
            print("Nieprawidłowa cena")
            continue
        if product_qty < 0 or product_qty == 0:
            print("Nieprawidłowa ilość produktów")
            continue
        if product_price * product_qty >= balance:
            print("Brak środków na koncie")
            continue
        if product_price * product_qty <= balance:
            balance -= product_price * product_qty
            print("Saldo wynosi: {}".format(balance))
            logs.append([action_type, product_name, product_price, product_qty])
            print(logs)
            if product_name in warehouse:
                warehouse[product_name] += product_qty
            else:
                warehouse[product_name] = product_qty
        print("Stan magazynu: {}".format(warehouse))

    if action_type == "sprzedaż":                                                       # SPRZEDAŻ INPUT
        product_name = str(input("Podaj identyfikator produktu: "))
        if product_name not in warehouse:
            print("Brak produktu w magazynie")
            continue
        product_price = int(input("Podaj cenę jednostkową produktu: "))
        if product_price < 0:
            print("Nieprawidłowa cena")
            continue
        product_qty = int(input("Podaj ilość sztuk: "))
        if product_qty < 0:
            print("Nieprawidłowa ilość sztuk")
            continue
        if warehouse[product_name] - product_qty < 0:
            print("Niewystraczjąca ilość sztuk w magazynie")
            continue
        balance += product_price * product_qty
        warehouse[product_name] -= product_qty
        print("Saldo wynosi: {}".format(balance))
        print("Stan magazynu: {}".format(warehouse))
        logs.append([action_type, product_name, product_price, product_qty])
        print(logs)

    if action_type == "stop":
        break


if sys.argv[1] == "zakup":                                            # ZAKUP Z LINII POLECEŃ
    action = sys.argv[1]
    product_name = str(sys.argv[2])
    product_price = int(sys.argv[3])
    product_qty = int(sys.argv[4])
    if product_price < 0:
        print("Neiprawidłowa cena")
    if product_qty < 0 or product_qty == 0:
        print("Nieprawidłowa ilość produktów")
    if product_qty * product_price >= balance:
        print("Brak środków na koncie")
    if product_qty * product_price <= balance:
        balance -= product_price * product_qty
        print("Saldo wynosi: {}".format(balance))
    if product_name in warehouse:
        warehouse[product_name] += product_qty
    else:
        warehouse[product_name] = product_qty
    print("Saldo wynosi: {}".format(balance))
    print("Stan magazynu: {}".format(warehouse))
    logs.append([action_type, product_name, product_price, product_qty])
    print(logs)


elif sys.argv[1] == "sprzedaż":                                         # SPRZEDAŻ Z LINII POLECEŃ
    action_type = sys.argv[1]
    product_name = str(sys.argv[2])
    product_price = int(sys.argv[3])
    product_qty = int(sys.argv[4])
    if product_name not in warehouse:
        print("Brak produktu w magazynie")
    if product_price < 0:
        print("Nieprawidłowa cena")
    if product_qty < 0:
        print("Nieprawidłowa ilość sztuk")
    if warehouse[product_name] - product_qty < 0:
        print("Niewystraczjąca ilość sztuk w magazynie")
    balance += product_price * product_qty
    warehouse[product_name] -= product_qty
    print("Saldo wynosi: {}".format(balance))
    print("Stan magazynu: {}".format(warehouse))
    logs.append([action_type, product_name, product_price, product_qty])
    print(logs)


    print(f"Podane paramentry: {sys.argv[1:]}")


if sys.argv[1] == "konto":
    print("Stan konta wynosi: {} gr".format(balance))
    print(f"Podane parametry: {sys.argv[1:]}")

elif sys.argv[1] == "magazyn":
    for i in sys.argv[2:]:
        print(f"{i}: {warehouse.get(i, 0)} sztuk")
        print("Stan magazynu: {}".format(warehouse))

elif sys.argv[1] == "przegląd":
    for i in int(sys.argv[2])-1, sys.argv[3], 1:
        print(logs[1])
    print(f"polecenia z linii rozkazu: {sys.argv[1:]}")

print("historia działań: ", logs)
print("Stan konta wynosi: {} gr".format(balance))
print("Stan magazynu: {}".format(warehouse))