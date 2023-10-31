import numpy as np

class CallOption:
    def __init__(self, strike_price, premium_paid):
        self.strike_price = strike_price
        self.premium_paid = premium_paid

    def calculate_payoff(self, stock_prices):
        return np.maximum(stock_prices - self.strike_price, 0) - self.premium_paid

    def calculate_max_profit(self):
        # For a call option, maximum profit is theoretically unlimited.
        return np.inf

    def calculate_max_loss(self):
        # Maximum loss for a call option is limited to the premium paid.
        return -self.premium_paid

    def calculate_break_even(self):
        # Break-even point for a call option is the strike price plus the premium paid.
        return self.strike_price + self.premium_paid

class PutOption:
    def __init__(self, strike_price, premium_paid):
        self.strike_price = strike_price
        self.premium_paid = premium_paid

    def calculate_payoff(self, stock_prices):
        return np.maximum(self.strike_price - stock_prices, 0) - self.premium_paid

    def calculate_max_profit(self):
        # For a put option, maximum profit is limited to the strike price minus the premium paid.
        return self.strike_price - self.premium_paid

    def calculate_max_loss(self):
        # Maximum loss for a put option is limited to the premium paid.
        return -self.premium_paid

    def calculate_break_even(self):
        # Break-even point for a put option is the strike price minus the premium paid.
        return self.strike_price - self.premium_paid
