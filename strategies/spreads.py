import numpy as np

class BearCallSpread:
    def __init__(self, short_strike, long_strike, premium_received, premium_paid, number_of_contracts, current_price):
        self.short_strike = short_strike
        self.long_strike = long_strike
        self.premium_received = premium_received
        self.premium_paid = premium_paid
        self.number_of_contracts = number_of_contracts
        self.current_price = current_price
        self.net_premium = premium_received - premium_paid

    def calculate_payoff(self, stock_prices):
        # When the stock price is above the short strike, the short call loses money
        # When the stock price is above the long strike, the long call gains money
        short_call_payoff = np.maximum(stock_prices - self.short_strike, 0) * self.number_of_contracts
        long_call_payoff = np.maximum(stock_prices - self.long_strike, 0) * self.number_of_contracts
        return (self.premium_received - short_call_payoff) + (long_call_payoff - self.premium_paid)

    def calculate_max_profit(self):
        # The maximum profit for a bear call spread is the net premium received
        return self.net_premium * self.number_of_contracts

    def calculate_max_loss(self):
        # The maximum loss is the difference in strike prices minus the net premium, multiplied by number of contracts and contract size
        return (self.short_strike - self.long_strike - self.net_premium) * self.number_of_contracts

    def calculate_break_even(self):
        # The break-even is the short strike plus the net premium received
        return self.short_strike + self.net_premium

    def calculate_current_value(self):
        # Calculate the current intrinsic value of the short call and the long call
        short_call_intrinsic_value = max(self.short_strike - self.current_price, 0)
        long_call_intrinsic_value = max(self.current_price - self.long_strike, 0)
        # The current value is the intrinsic value of the long call minus the short call
        return (long_call_intrinsic_value - short_call_intrinsic_value) * self.number_of_contracts

    def calculate_current_profit_loss(self):
        # The current profit or loss is the net premium minus the current value
        return (self.net_premium * self.number_of_contracts * 100) - self.calculate_current_value()
