class Investment:
    Percent = 4

    def __init__(self, amount, term):
        self.amount = amount
        self.term = term

class Bank:
    @classmethod
    def deposit(cls, n, r):
        money = n * (1 + Investment.Percent / 1200) ** (r * 12)
        print(f'After {r} years your Bank Account will have: {int(money)} $')
        return money
invest = Investment(300, 2)
invest = Bank.deposit(invest.amount, invest.term)
