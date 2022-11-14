# Банковский вклад
class Investment:
    PERCENT = 0.1

    def __init__(self, amount, years):
        self.amount = amount  # n
        self.years = years  # r


class Bank:
    @classmethod
    def deposit(cls, n, r):
        big_money = n * (1 + Investment.PERCENT / 12) ** (r * 12)
        print(f'Вау, через {r} лет у вас на счету будет: {int(big_money)} денег')
        return big_money


c = Investment(1000, 5)
c = Bank.deposit(c.amount, c.years)
