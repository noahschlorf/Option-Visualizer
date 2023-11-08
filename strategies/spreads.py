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
        return (self.premium_received - short_call_payoff) + (long_call_payoff - self.premium_paid)

    def calculate_max_profit(self):
        return self.net_premium * self.number_of_contracts

    def calculate_max_loss(self):
        return (self.long_strike - self.short_strike - self.net_premium) * self.number_of_contracts

    def calculate_break_even(self):
        return self.short_strike + self.net_premium

class BullCallSpread:
    def __init__(self, sell_call_strike, buy_call_strike, premium_paid, premium_received, number_of_contracts, current_price):
        self.sell_call_strike = sell_call_strike
        self.buy_call_strike = buy_call_strike
        self.premium_paid = premium_paid
        self.premium_received = premium_received
        self.number_of_contracts = number_of_contracts
        self.current_price = current_price
        self.net_premium = self.premium_received - self.premium_paid 

    def calculate_payoff(self, stock_prices):
        long_call_payoff = np.maximum(stock_prices - self.buy_call_strike, 0) * self.number_of_contracts
        short_call_payoff = np.maximum(stock_prices - self.sell_call_strike, 0) * self.number_of_contracts
        total_payoff = (long_call_payoff - short_call_payoff) - (self.net_premium * self.number_of_contracts)
        return total_payoff

    def calculate_max_profit(self):
        return ((self.sell_call_strike - self.buy_call_strike) - (self.net_premium))*self.number_of_contracts

    def calculate_max_loss(self):
        return self.net_premium * self.number_of_contracts

    def calculate_break_even(self):
        return self.buy_call_strike + (self.net_premium)
    
class BearPutSpread:
    def __init__(self, sell_put_strike, buy_put_strike, premium_received, premium_paid, number_of_contracts, current_price):
        self.sell_put_strike = sell_put_strike
        self.buy_put_strike = buy_put_strike
        self.premium_paid = premium_paid
        self.premium_received = premium_received
        self.number_of_contracts = number_of_contracts
        self.current_price = current_price
        self.net_premium = self.premium_received - self.premium_paid 

    def calculate_payoff(self, stock_prices):
        long_put_payoff = np.maximum(self.buy_put_strike - stock_prices, 0) * self.number_of_contracts
        short_put_payoff = np.maximum(self.sell_put_strike - stock_prices, 0) * self.number_of_contracts
        total_payoff = (long_put_payoff - self.premium_paid*self.number_of_contracts) -  (short_put_payoff - self.premium_received*self.number_of_contracts)
        return total_payoff
         
    def calculate_max_profit(self):
        return ((self.buy_put_strike - self.sell_put_strike) - (self.premium_paid-self.premium_received))*self.number_of_contracts

    def calculate_max_loss(self):
        return (self.premium_paid-self.premium_received)*self.number_of_contracts

    def calculate_break_even(self):
        return self.buy_put_strike - (self.premium_paid-self.premium_received)
    
class BullPutSpread:
    def __init__(self, sell_put_strike, buy_put_strike, premium_received, premium_paid, number_of_contracts, current_price):
        self.sell_put_strike = sell_put_strike
        self.buy_put_strike = buy_put_strike
        self.premium_paid = premium_paid
        self.premium_received = premium_received
        self.number_of_contracts = number_of_contracts
        self.current_price = current_price
        self.net_premium = self.premium_received - self.premium_paid

    def calculate_payoff(self, stock_prices):
        short_put_payoff = np.maximum(self.sell_put_strike - stock_prices, 0) * self.number_of_contracts
        long_put_payoff = np.maximum(self.buy_put_strike - stock_prices, 0) * self.number_of_contracts
        total_payoff = (short_put_payoff - self.premium_received * self.number_of_contracts) - (long_put_payoff - self.premium_paid * self.number_of_contracts)
        return total_payoff

    def calculate_max_profit(self):
        return self.net_premium * self.number_of_contracts
    
    def calculate_max_loss(self):
        return (self.sell_put_strike - self.buy_put_strike - self.net_premium) * self.number_of_contracts
    
    def calculate_break_even(self):
        return self.sell_put_strike - self.net_premium
    


        

    