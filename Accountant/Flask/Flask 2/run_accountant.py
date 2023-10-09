class Accountant:
    def __init__(self):
        self.balance = 0
        self.warehouse = {}
        self.actions = {}

    def add(self, name):
        def decorate(cb):
            self.actions[name] = cb
        return decorate

    def run(self, name, *args):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self, *args)
