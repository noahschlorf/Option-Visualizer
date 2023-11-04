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
        short_call_payoff = np.maximum(stock_prices - self.short_strike, 0) * self.number_of_contracts
        long_call_payoff = np.maximum(stock_prices - self.long_strike, 0) * self.number_of_contracts
        return (self.net_premium * 100) - short_call_payoff + long_call_payoff

    def calculate_max_profit(self):
        return self.net_premium * self.number_of_contracts * 100

    def calculate_max_loss(self):
        return (self.long_strike - self.short_strike - self.net_premium) * self.number_of_contracts * 100

    def calculate_break_even(self):
        return self.short_strike + self.net_premium

    def calculate_current_value(self):
        short_call_intrinsic_value = max(self.short_strike - self.current_price, 0)
        long_call_intrinsic_value = max(self.current_price - self.long_strike, 0)
        return (long_call_intrinsic_value - short_call_intrinsic_value) * self.number_of_contracts * 100

    def calculate_current_profit_loss(self):
        return (self.net_premium * self.number_of_contracts * 100) - self.calculate_current_value()

class BullCallSpread:
    def __init__(self, short_strike, long_strike, premium_received, premium_paid, number_of_contracts, current_price):
        self.short_strike = short_strike
        self.long_strike = long_strike
        self.premium_received = premium_received
        self.premium_paid = premium_paid
        self.number_of_contracts = number_of_contracts
        self.current_price = current_price
        self.net_premium = premium_received - premium_paid

    def calculate_payoff(self, stock_prices):
        long_call_payoff = np.maximum(stock_prices - self.long_strike, 0) * self.number_of_contracts
        short_call_payoff = np.maxium(stock_prices - self.short_strike, 0) * self.number_of_contracts
        return (long_call_payoff - self.premium_paid * 100) - (short_call_payoff - self.premium_received * 100)

    def calculate_max_profit(self):
        return (self.long_strike - self.short_strike - self.net_premium) * self.number_of_contracts * 100

    def calculate_max_loss(self):
        return self.net_premium * self.number_of_contracts * 100

    def calculate_break_even(self):
        return self.long_strike + self.net_premium

    def calculate_current_value(self):
        long_call_intrinsic_value = max(self.current_price - self.long_strike, 0)
        short_call_intrinsic_value = max(self.short_strike - self.current_price, 0)
        return (long_call_intrinsic_value - short_call_intrinsic_value) * self.number_of_contracts * 100

    def calculate_current_profit_loss(self):
        return self.calculate_current_value() - (self.net_premium * self.number_of_contracts * 100)

    def calculate_current_value(self):
    

    