class Investment:

    INVESTMENT_PERCENT = 10

    def __init__(self, summa: float, period: int):
        self.summa = summa
        self.period = period


class Bank:

    @staticmethod
    def deposit_info():
        for i in range(1, invest.period * 12 + 1):
            invest.summa = invest.summa + (invest.summa * Investment.INVESTMENT_PERCENT / 1200)
        return invest.summa


invest = Investment(10000, 18)
wallet = Bank
print(f'Total money: {wallet.deposit_info()}')
