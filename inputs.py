import tkinter as tk
from tkinter import ttk

def single_option_input(parent,strategy_class):
     # Get the parameters from the entries
    parent.strike_price = float(parent.strike_price_entry.get())
    parent.premium_paid = float(parent.premium_paid_entry.get())
    parent.number_of_contracts = int(parent.number_of_contracts_entry.get())
    parent.current_price = float(parent.current_price_entry.get())
        

    # Create an instance of the strategy class
    strategy = strategy_class(parent.strike_price, parent.premium_paid, parent.number_of_contracts, parent.current_price)
    return strategy
