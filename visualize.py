from strategies.singleoption import BuyCallOption, BuyPutOption, SellCallOption, SellPutOption
from strategies.spreads import BearCallSpread, BullCallSpread, BearPutSpread, BullPutSpread
from widgets import single_option_widgets, spread_widgets
from inputs import single_option_input, spread_input

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StrategyVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.current_widgets = []
        self.title('Option Strategy Visualizer')
        self.geometry('800x900')

        # Dropdown menu for selecting the strategy
        self.strategy_label = ttk.Label(self, text="Select Strategy:")
        self.strategy_label.pack()
        self.selected_strategy = tk.StringVar()
        # List of total strategies the user can pick from
        self.strategies = {
            'Buy Call Option': BuyCallOption,
            'Sell Call Option': SellCallOption,
            'Buy Put Option': BuyPutOption, 
            'Sell Put Option': SellPutOption,
            'Bear Call Spread': BearCallSpread,
            'Bull Call Spread': BullCallSpread,
            'Bear Put Spread': BearPutSpread,
            'Bull Put Spread': BullPutSpread
        }
        self.strategy_menu = ttk.Combobox(self, textvariable=self.selected_strategy, values=list(self.strategies.keys()))
        self.strategy_menu.pack()
        
        # Bind the selection event to a method that handles the widget generation
        self.strategy_menu.bind('<<ComboboxSelected>>', self.on_strategy_select)

         # Button to plot graph
        self.plot_button = ttk.Button(self, text="Plot Strategy", command=self.plot_strategy)
        self.plot_button.pack()
        # Placeholder for matplotlib graph
        self.figure = plt.Figure(figsize=(6, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack()

    def clear_widgets(self):
        # Clear all the widgets currently displayed
        for widget in getattr(self, 'current_widgets', []):
            widget.destroy()
        self.current_widgets = []  # Reset the widget list
    
    def on_strategy_select(self, event):
        self.clear_widgets()

        # Use a separate condition for each strategy instead of a compound condition
        selected_strategy = self.selected_strategy.get()
        if selected_strategy == 'Buy Call Option' or selected_strategy == 'Sell Call Option' or selected_strategy == 'Buy Put Option' or selected_strategy == 'Sell Put Option':
            single_option_widgets(self)
        elif selected_strategy == 'Bear Call Spread' or selected_strategy == 'Bull Call Spread' or selected_strategy == 'Bear Put Spread' or selected_strategy == 'Bull Put Spread':
            spread_widgets(self)


    def plot_strategy(self):
        # Get the selected strategy class from the dropdown
        strategy_class = self.strategies.get(self.selected_strategy.get())

        if not strategy_class:
            tk.messagebox.showerror("Error", "Please select a valid strategy.")
            return

        if self.selected_strategy.get() in ('Buy Call Option', 'Sell Call Option', 'Buy Put Option', 'Sell Put Option'):
            strategy = single_option_input(self, strategy_class)
            stock_prices = np.linspace(0, self.strike_price*2, 100)
            payoff = strategy.calculate_payoff(stock_prices)
            current_profit_loss = strategy.calculate_current_profit_loss()
        if self.selected_strategy.get() in ('Bear Call Spread', 'Bull Call Spread', 'Bear Put Spread', 'Bull Put Spread'):
            strategy = spread_input(self, strategy_class)
            if isinstance(strategy, BearCallSpread):
                lower_limit = strategy.short_strike - (strategy.short_strike - strategy.long_strike)
                upper_limit = strategy.long_strike + (strategy.short_strike - strategy.long_strike)
            elif isinstance(strategy, BullCallSpread):
                lower_limit = strategy.buy_call_strike - (strategy.sell_call_strike - strategy.buy_call_strike)
                upper_limit = strategy.sell_call_strike + (strategy.sell_call_strike - strategy.buy_call_strike)
            elif isinstance(strategy, BearPutSpread):
                lower_limit = strategy.buy_put_strike - (strategy.buy_put_strike - strategy.sell_put_strike)
                upper_limit = strategy.sell_put_strike + (strategy.buy_put_strike - strategy.sell_put_strike)
            elif isinstance(strategy, BullPutSpread):
                lower_limit = strategy.buy_put_strike - (strategy.sell_put_strike - strategy.buy_put_strike)
                upper_limit = strategy.sell_put_strike + (strategy.sell_put_strike - strategy.buy_put_strike)
                
            stock_prices = np.linspace(lower_limit-20, upper_limit+20, 100)
            payoff = strategy.calculate_payoff(stock_prices)
                
        # Call the methods to calculate max profit, max loss, and break-even
        max_profit = strategy.calculate_max_profit()
        max_loss = strategy.calculate_max_loss()
        break_even = strategy.calculate_break_even()

        # Plot the strategy payoff
        self.ax.clear()
        self.ax.plot(stock_prices, payoff, label=f'{strategy_class.__name__} Payoff')
        self.ax.axhline(0, color='lightgray', linestyle='--')  # P/L 0 line
        
        self.ax.set_title(f'{add_space_before_capitals(strategy_class.__name__)} Payoff')
        self.ax.set_xlabel('Stock Price')
        self.ax.set_ylabel('Profit/Loss (P&L)')

        # Annotate the max profit, max loss, and break-even on the plot
        # Adjust positions and formatting as necessary
        self.ax.text(0.05, 0.95, f'Max Profit: {"Unlimited" if max_profit == np.inf else round(max_profit, 2)}', transform=self.ax.transAxes)
        self.ax.text(0.05, 0.90, f'Max Loss: {round(max_loss, 2)}', transform=self.ax.transAxes)
        self.ax.text(0.05, 0.85, f'Break-even: {round(break_even, 2)}', transform=self.ax.transAxes)
        if self.selected_strategy.get() in ('Buy Call Option', 'Sell Call Option', 'Buy Put Option', 'Sell Put Option'):
            self.ax.text(0.05, 0.80, f'Current P/L: {round(current_profit_loss, 2)}', transform=self.ax.transAxes)


        self.canvas.draw()

def add_space_before_capitals(text):
    # This function adds a space before each capital letter found in the input string
    new_text = ""
    for i, char in enumerate(text):
        # If the character is uppercase and it's not the first character, add a space before it
        if char.isupper() and i != 0:
            new_text += " "
        new_text += char
    return new_text

if __name__ == "__main__":
    app = StrategyVisualizer()
    app.mainloop()
