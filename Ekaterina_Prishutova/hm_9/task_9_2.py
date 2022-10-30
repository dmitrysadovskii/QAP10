class Investment:

    def __init__(self, investment_amount, term):
        self.investment_amount = investment_amount
        self.term = term

    def invest_deposit(self, percent):
        return Bank.deposit(self.investment_amount, self.term, percent)


class Bank:

    @staticmethod
    def deposit(n, r, percent):
        return n * (1 + percent/1200) ** r


inv = Investment(350000, 9)
print(inv.invest_deposit(10))
