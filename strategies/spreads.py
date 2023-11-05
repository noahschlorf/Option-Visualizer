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
        return (self.long_strike - self.short_strike - self.net_premium) * self.number_of_contracts

    def calculate_break_even(self):
        # The break-even is the short strike plus the net premium received
        return self.short_strike + self.net_premium

class BullCallSpread:
    def __init__(self, sell_call_strike,buy_call_strike, premium_paid, premium_received, number_of_contracts, current_price):
        self.sell_call_strike = sell_call_strike
        self.buy_call_strike = buy_call_strike
        self.premium_paid = premium_paid
        self.premium_received = premium_received
        self.number_of_contracts = number_of_contracts
        self.current_price = current_price
        self.net_premium = self.premium_received - self.premium_paid 

    def calculate_payoff(self, stock_prices):
        # The payoff from the long call (bought call)
        long_call_payoff = np.maximum(stock_prices - self.buy_call_strike, 0) * self.number_of_contracts
        # The payoff from the short call (sold call)
        short_call_payoff = np.maximum(stock_prices - self.sell_call_strike, 0) * self.number_of_contracts   
        # Total payoff for the bull call spread strategy
        total_payoff = (long_call_payoff - self.premium_paid * self.number_of_contracts) - \
                    (short_call_payoff - self.premium_received * self.number_of_contracts)
        return total_payoff


    def calculate_max_profit(self):
        # The maximum profit is the difference in strike prices minus the net premium, multiplied by number of contracts
        return ((self.sell_call_strike - self.buy_call_strike) - (self.net_premium))*self.number_of_contracts

    def calculate_max_loss(self):
        # The maximum loss is the net premium paid
        return self.net_premium * self.number_of_contracts

    def calculate_break_even(self):
        # The break-even is the buy call strike plus the net premium paid per share
        return self.buy_call_strike + (self.net_premium / self.number_of_contracts)

 
        

    