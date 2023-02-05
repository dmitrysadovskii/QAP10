class Investment:
    def __init__(self, amount, term):
        self.amount = amount
        self.term = term


class Bank:
    def deposit(self, investment: Investment):
        interest_rate = 0.1 / 12
        total_amount = investment.amount
        for i in range(investment.term * 12):
            total_amount *= (1 + interest_rate)
        return total_amount


investment = Investment(100000, 5)
bank = Bank()
print(bank.deposit(investment))
