class Invest:
    def __init__(self, sum, years):
        self.sum = sum
        self.years = years


class Bank:
    PERCENT = 10

    def recursive_method(self, invest):
        for _ in range(invest.years):
            invest.sum = (1 + self.PERCENT / 100) * invest.sum
        return invest.sum


invest_1 = Invest(1000, 1)
bank = Bank()

print(bank.recursive_method(invest_1))
