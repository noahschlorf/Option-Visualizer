import tkinter as tk
from tkinter import ttk


def single_option_widgets(parent):
    if not hasattr(parent, 'current_widgets'):
        parent.current_widgets = []
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

    parent.current_widgets.append(parent.strike_price_label)
    parent.current_widgets.append(parent.strike_price_entry)
    parent.current_widgets.append(parent.premium_paid_label)
    parent.current_widgets.append(parent.premium_paid_entry)
    parent.current_widgets.append(parent.number_of_contracts_label)
    parent.current_widgets.append(parent.number_of_contracts_entry)
    parent.current_widgets.append(parent.current_price_label)
    parent.current_widgets.append(parent.current_price_entry)
    
    return (parent.strike_price_label, parent.strike_price_entry,
            parent.premium_paid_label, parent.premium_paid_entry,
            parent.number_of_contracts_label, parent.number_of_contracts_entry,
            parent.current_price_label, parent.current_price_entry)

def bear_call_spread_widgets(parent):
    if not hasattr(parent, 'current_widgets'):
        parent.current_widgets = []

    # Input for short strike price
    parent.sell_strike_label = ttk.Label(parent, text="Sell Strike Price:")
    parent.sell_strike_label.pack()
    parent.sell_strike_entry = ttk.Entry(parent)
    parent.sell_strike_entry.pack()

    # Input for long strike price
    parent.buy_strike_label = ttk.Label(parent, text="Buying Strike Price:")
    parent.buy_strike_label.pack()
    parent.buy_strike_entry = ttk.Entry(parent)
    parent.buy_strike_entry.pack()

    # Input for premium received
    parent.premium_received_label = ttk.Label(parent, text="Premium Received (Per Contract):")
    parent.premium_received_label.pack()
    parent.premium_received_entry = ttk.Entry(parent)
    parent.premium_received_entry.pack()

    # Input for premium paid
    parent.premium_paid_label = ttk.Label(parent, text="Premium Paid (Per Contract):")
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

    parent.current_widgets.append(parent.sell_strike_label)
    parent.current_widgets.append(parent.sell_strike_entry)
    parent.current_widgets.append(parent.buy_strike_label)
    parent.current_widgets.append(parent.buy_strike_entry)
    parent.current_widgets.append(parent.premium_received_label)
    parent.current_widgets.append(parent.premium_received_entry)
    parent.current_widgets.append(parent.premium_paid_label)
    parent.current_widgets.append(parent.premium_paid_entry)
    parent.current_widgets.append(parent.number_of_contracts_label)
    parent.current_widgets.append(parent.number_of_contracts_entry)
    parent.current_widgets.append(parent.current_price_label)
    parent.current_widgets.append(parent.current_price_entry)

    return (parent.sell_strike_label, parent.sell_strike_entry,
            parent.buy_strike_label, parent.buy_strike_entry,
            parent.premium_received_label, parent.premium_received_entry,
            parent.premium_paid_label, parent.premium_paid_entry,
            parent.number_of_contracts_label, parent.number_of_contracts_entry,
            parent.current_price_label, parent.current_price_entry)