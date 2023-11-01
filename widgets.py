import tkinter as tk
from tkinter import ttk


def single_option_widgets(parent):
    # Input for strike price
    parent.strike_price_label = ttk.Label(parent, text="Strike Price:")
    parent.strike_price_label.pack()
    parent.strike_price_entry = ttk.Entry(parent)
    parent.strike_price_entry.pack()

    # Input for option price (premium paid)
    parent.premium_paid_label = ttk.Label(parent, text="Premium (Per Contract):")
    parent.premium_paid_label.pack()
    parent.premium_paid_entry = ttk.Entry(parent)
    parent.premium_paid_entry.pack()

    # Input for number of contracts
    parent.number_of_contracts_label = ttk.Label(parent, text="Number of Contracts:")
    parent.number_of_contracts_label.pack()
    parent.number_of_contracts_entry = ttk.Entry(parent)
    parent.number_of_contracts_entry.pack()

    # Input for current price of the underlying asset
    parent.current_price_label = ttk.Label(parent, text="Current Price:")
    parent.current_price_label.pack()
    parent.current_price_entry = ttk.Entry(parent)
    parent.current_price_entry.pack()
    
    return (parent.strike_price_label, parent.strike_price_entry,
            parent.premium_paid_label, parent.premium_paid_entry,
            parent.number_of_contracts_label, parent.number_of_contracts_entry,
            parent.current_price_label, parent.current_price_entry)