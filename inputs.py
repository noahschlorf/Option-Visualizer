import tkinter as tk
from tkinter import ttk
import numpy as np 

def single_option_input(parent,strategy_class):
     # Get the parameters from the entries
    parent.strike_price = float(parent.strike_price_entry.get())
    parent.premium_paid = float(parent.premium_paid_entry.get())
    parent.number_of_contracts = int(parent.number_of_contracts_entry.get())
    parent.current_price = float(parent.current_price_entry.get())
        

    # Create an instance of the strategy class
    strategy = strategy_class(parent.strike_price, parent.premium_paid, parent.number_of_contracts, parent.current_price)
    return strategy

def bear_call_spread_input(parent, strategy_class):
    # Get the parameters from the entries and set them as attributes of the parent
    parent.sell_strike = float(parent.sell_strike_entry.get())
    parent.buy_strike = float(parent.buy_strike_entry.get())
    parent.premium_received = float(parent.premium_received_entry.get())
    parent.premium_paid = float(parent.premium_paid_entry.get())
    parent.number_of_contracts = int(parent.number_of_contracts_entry.get())
    parent.current_price = float(parent.current_price_entry.get())
     
    # Ensure the parameters are passed in the correct order
    strategy = strategy_class(parent.sell_strike, parent.buy_strike, parent.premium_received, parent.premium_paid, parent.number_of_contracts, parent.current_price)
    
    parent.bear_call_spread_strategy = strategy

    return strategy


