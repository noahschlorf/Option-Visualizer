import numpy as np

class BuyCallOption:
    def __init__(self, strike_price, premium_paid, number_of_contracts, current_price):
        self.strike_price = strike_price
        self.premium_paid = premium_paid
        self.number_of_contracts = number_of_contracts
        self.current_price = current_price

    def calculate_payoff(self, stock_prices):
        return self.number_of_contracts * (np.maximum(stock_prices - self.strike_price, 0) - self.premium_paid)

    def calculate_max_profit(self):
        return np.inf

    def calculate_max_loss(self):
        return -self.premium_paid * self.number_of_contracts

    def calculate_break_even(self):
        return self.strike_price + self.premium_paid
    
    def calculate_current_value(self):
        intrinsic_value = max(self.current_price - self.strike_price, 0)
        return intrinsic_value * self.number_of_contracts

    def calculate_current_profit_loss(self):
        return self.calculate_current_value() - (self.premium_paid * self.number_of_contracts)

class BuyPutOption:
    def __init__(self, strike_price, premium_paid, number_of_contracts, current_price):
        self.strike_price = strike_price
        self.premium_paid = premium_paid
        self.number_of_contracts = number_of_contracts 
        self.current_price = current_price 

    def calculate_payoff(self, stock_prices):
        return self.number_of_contracts * (np.maximum(self.strike_price - stock_prices, 0) - self.premium_paid)

    def calculate_max_profit(self):
        return self.number_of_contracts * (self.strike_price - self.premium_paid)

    def calculate_max_loss(self):
        return -self.premium_paid * self.number_of_contracts

    def calculate_break_even(self):
        return self.strike_price - self.premium_paid
    
    def calculate_current_value(self):
        intrinsic_value = max(self.strike_price - self.current_price, 0)
        return intrinsic_value * self.number_of_contracts

    def calculate_current_profit_loss(self):
        return self.calculate_current_value() - (self.premium_paid * self.number_of_contracts)

class SellCallOption:
    def __init__(self, strike_price, premium_received, number_of_contracts, current_price):
        self.strike_price = strike_price
        self.premium_received = premium_received
        self.number_of_contracts = number_of_contracts
        self.current_price = current_price

    def calculate_payoff(self, stock_prices):
        return self.number_of_contracts * (self.premium_received - np.maximum(stock_prices - self.strike_price, 0))

    def calculate_max_profit(self):
        return self.premium_received * self.number_of_contracts

    def calculate_max_loss(self):
        return -np.inf

    def calculate_break_even(self):
        return self.strike_price + self.premium_received
    
    def calculate_current_value(self):
        intrinsic_value = max(self.current_price - self.strike_price, 0)
        return intrinsic_value * self.number_of_contracts

    def calculate_current_profit_loss(self):
        return (self.premium_received * self.number_of_contracts) - self.calculate_current_value()

class SellPutOption:
    def __init__(self, strike_price, premium_received, number_of_contracts, current_price):
        self.strike_price = strike_price
        self.premium_received = premium_received
        self.number_of_contracts = number_of_contracts
        self.current_price = current_price

    def calculate_payoff(self, stock_prices):
        return self.number_of_contracts * (self.premium_received - np.maximum(self.strike_price - stock_prices, 0))

    def calculate_max_profit(self):
        return self.premium_received * self.number_of_contracts

    def calculate_max_loss(self):
        return self.number_of_contracts * (self.strike_price - self.premium_received)

    def calculate_break_even(self):
        return self.strike_price - self.premium_received
    
    def calculate_current_value(self):
        intrinsic_value = max(self.strike_price - self.current_price, 0)
        return intrinsic_value * self.number_of_contracts

    def calculate_current_profit_loss(self):
        return (self.premium_received * self.number_of_contracts) - self.calculate_current_value()
