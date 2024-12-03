class Wallet:
    def __init__(self):
        self.balance = 0.0

    def add_wallet(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance