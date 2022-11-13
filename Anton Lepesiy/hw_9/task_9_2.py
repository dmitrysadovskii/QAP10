class Investment:
    def __init__(self, investment_amount, investment_period):
        self.investment_amount = investment_amount
        self.investment_period = investment_period


class Bank:
    def __init__(self, rate):
        self.rate = rate

    def deposit(self, start_amount, period):
        rate = self.rate
        month_rate = rate / 12
        current_amount = start_amount
        for year_capital in range(period):
            for month_capital in range(12):
                month_capital = current_amount * month_rate
                current_amount += month_capital
        return print(f"Your amount after {period} years will be {current_amount} rubles")


user_investment = Investment(1000, 5)

bank = Bank(0.1)
user_start_amount = user_investment.investment_amount
user_investment_period = user_investment.investment_period

bank.deposit(user_start_amount, user_investment_period)
