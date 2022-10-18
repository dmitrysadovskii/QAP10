class Investment:

    INVESTMENT_PERCENT = 10

    def __init__(self, summa: float, period: int):
        self.summa = summa
        self.period = period


class Bank:

    @staticmethod
    def deposit_info(n, r):
        invest.summa = n
        for i in range(1, r * 12 + 1):
            n = n + (n * Investment.INVESTMENT_PERCENT / 1200)
        return n - invest.summa


invest = Investment(10000, 1)
wallet = Bank
print(f'Total profit: {wallet.deposit_info(invest.summa, invest.period)}')
