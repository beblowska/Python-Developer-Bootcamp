
class Acc:
    def __init__(self):
        self.balance = 0
        self.warehouse = {}
        self.actions = {}

    def open(self, path):
        with open(path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                line = line.split(" ")
                action = line[0]
                if action == "saldo":
                    amount = line[1]
                    self.balance += int(amount)
                elif action == "zakup":
                    product_name, product_price, product_qty = line[1:]
                    self.balance -= int(product_price) * int(product_qty)
                    if product_name in self.warehouse:
                        self.warehouse[product_name] += int(product_qty)
                    else:
                        self.warehouse[product_name] = int(product_qty)
                elif action == "sprzedaz":
                    product_name, product_price, product_qty = line[1:]
                    self.balance += int(product_price) * int(product_qty)
                    self.warehouse[product_name] -= int(product_qty)
                    if self.warehouse[product_name] == 0:
                        del self.warehouse[product_name]
                else:
                    continue

    def save(self, path, object):
        with open(path, "a", encoding="utf-8") as file:
            file.write(object + "\n")

    def add(self, name):
        def decorate(m):
            self.actions[name] = m
        return decorate

    def run(self, name, *args):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self, *args)
