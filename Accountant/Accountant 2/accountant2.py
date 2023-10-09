import sys

class Accountant:
    def __init__(self, file_path):
        self.warehouse = {}
        self.logs = []
        self.available_actions = {"saldo": 2, "zakup": 3, "sprzedaż": 3, "stop": 0}
        self.balance = 0
        self.file_path = file_path
        self.history = self.read_file()

    def change_balance(self, product_price, comment):
        self.balance += int(product_price)
        print(comment)
        print(product_price)
        print(self.logs)

    def sell(self, product_name, product_price, product_qty):
        if product_name not in self.warehouse:
            print("Brak produktu w magazynie")
            return
        if int(product_price) < 0:
            print("Nieprawidłowa cena")
            return
        if int(product_qty) < 0:
            print("Nieprawidłowa ilość sztuk")
            return
        self.balance += int(product_price) * int(product_qty)
        print(product_name)
        print(product_price)
        print(product_qty)
        print(self.logs)

    def buy(self, product_name, product_price, product_qty):
        if product_name not in self.warehouse:
            print("Dodaję nowy produkt")
            self.warehouse[product_name] = product_qty
        if int(product_price) < 0:
            print("Nieprawidłowa cena")
            return
        if int(product_qty) <= 0:
            print("Nieprawidłowa ilość produktów")
            return
        if int(product_price) * int(product_qty) >= self.balance:
            print("Brak środków na koncie")
            return
        if int(product_price) * int(product_qty) <= self.balance:
            self.balance -= int(product_price) * int(product_qty)
        self.balance -= int(product_price) * int(product_qty)
        self.warehouse[product_name] += product_qty
        print(self.logs)
        print(product_name)
        print(product_price)
        print(product_qty)

    def account(self):
        print("Stan konta wynosi: {} gr".format(self.balance))
        print(f"Podane parametry: {sys.argv[1:]}")

    def get_warehouse(self):
        for i in sys.argv[2:]:
            print(f"{i}: {self.warehouse.get(i, 0)} sztuk")
            print("Stan magazynu: {}".format(self.warehouse))

    def sum_up(self):
        for i in int(sys.argv[2]) - 1, sys.argv[3], 1:
            print(self.logs[1])
        print(f"polecenia z linii rozkazu: {sys.argv[1:]}")

    def read_file(self):
        lista =[]
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                lista.append(line.strip())
        return lista

    def change_list(self):
        new_list = []
        idx = 0
        while idx < len(self.history):
            action = self.history[idx]
            qty = self.available_actions[action]
            idx += 1
            params = self.history[idx: idx + qty]
            new_list.append([action, params])
            idx += qty
        return new_list

    def run_all(self):
        new_list = self.change_list()
        for i in new_list:
            if i[0] == "saldo":
                self.change_balance(*i[1])
            if i[0] == "sprzedaż":
                self.sell(*i[1])
            if i[0] == "zakup":
                self.buy(*i[1])

    def write_to_file(self):
       history = sys.argv[2:]
        file = open(self.file_path, "a", encoding="utf-8")
        for line in history:
            file.writelines("\n" + line)
        file.close()

zmienna = Accountant(sys.argv[1])
zmienna.run_all()
zmienna.write_to_file()
print(zmienna.history)
