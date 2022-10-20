class Investment:
    def __init__(self, amount, term, __annual_rate=0.1):
        self.sum = amount
        self.term = term
        self.APR = __annual_rate


class Bank:

    @staticmethod
    def deposit(amount, term):
        result = 0
        for _ in range(term):
            for _ in range(12):
                result += amount * invest.APR / 12

        print(amount + result)


bank = Bank
invest = Investment(1000, 3)
bank.deposit(invest.sum, invest.term)
