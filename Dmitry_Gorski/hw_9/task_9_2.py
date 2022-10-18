class Investment:

    INVESTMENT_PERCENT = 10

    def __init__(self, summa: float, period: int):
        self.summa = summa
        self.period = period


class Bank:

    @staticmethod
    def deposit_info():
        start_invest_summa = invest.summa
        for i in range(1, invest.period * 12 + 1):
            invest.summa = invest.summa + (invest.summa * Investment.INVESTMENT_PERCENT / 1200)
        return invest.summa - start_invest_summa


invest = Investment(10000, 1)
wallet = Bank
print(f'Total profit: {wallet.deposit_info()}')
