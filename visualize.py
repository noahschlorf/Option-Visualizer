from singleoption import BuyCallOption, BuyPutOption, SellCallOption, SellPutOption
from widgets import single_option_widgets
from inputs import single_option_input

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StrategyVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Option Strategy Visualizer')
        self.geometry('800x900')

        # Dropdown menu for selecting the strategy
        self.strategy_label = ttk.Label(self, text="Select Strategy:")
        self.strategy_label.pack()
        
        self.selected_strategy = tk.StringVar()
        self.strategies = {
            'Buy Call Option': BuyCallOption,
            'Sell Call Option': SellCallOption,
            'Buy Put Option': BuyPutOption, 
            'Sell Put Option': SellPutOption
        }
        self.strategy_menu = ttk.Combobox(self, textvariable=self.selected_strategy, values=list(self.strategies.keys()))
        self.strategy_menu.pack()
        
        # Bind the selection event to a method that handles the widget generation
        self.strategy_menu.bind('<<ComboboxSelected>>', self.on_strategy_select)

    def on_strategy_select(self, event):
        # Get the selected strategy name
        selected_strategy_name = self.selected_strategy.get()
        # Get the corresponding strategy class
        strategy_class = self.strategies[selected_strategy_name]
        # Now you can call your widget generation function
        single_option_widgets(self)
         # Button to plot graph
        self.plot_button = ttk.Button(self, text="Plot Strategy", command=self.plot_strategy)
        self.plot_button.pack()
        # Placeholder for matplotlib graph
        self.figure = plt.Figure(figsize=(6, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack()
    

    def plot_strategy(self):
        # Get the selected strategy class from the dropdown
        strategy_class = self.strategies.get(self.selected_strategy.get())

        if not strategy_class:
            tk.messagebox.showerror("Error", "Please select a valid strategy.")
            return
        
        strategy = single_option_input(self,strategy_class)

        # Assuming that each strategy class has a method to calculate the payoff
        stock_prices = np.linspace(0, self.strike_price*2, 100)
        payoff = strategy.calculate_payoff(stock_prices)

        # Call the methods to calculate max profit, max loss, and break-even
        max_profit = strategy.calculate_max_profit()
        max_loss = strategy.calculate_max_loss()
        break_even = strategy.calculate_break_even()
        current_value = strategy.calculate_current_value()
        current_profit_loss = strategy.calculate_current_profit_loss()

        # Plot the strategy payoff
        self.ax.clear()
        self.ax.plot(stock_prices, payoff, label=f'{strategy_class.__name__} Payoff')
        self.ax.axhline(0, color='lightgray', linestyle='--')  # P/L 0 line
        
        self.ax.set_title(f'{add_space_before_capitals(strategy_class.__name__)} Payoff')
        self.ax.set_xlabel('Stock Price')
        self.ax.set_ylabel('Profit/Loss (P&L)')

        # Annotate the max profit, max loss, and break-even on the plot
        # Adjust positions and formatting as necessary
        self.ax.text(0.05, 0.95, f'Max Profit: {"Unlimited" if max_profit == np.inf else max_profit}', transform=self.ax.transAxes)
        self.ax.text(0.05, 0.90, f'Max Loss: {max_loss}', transform=self.ax.transAxes)
        self.ax.text(0.05, 0.85, f'Break-even: {break_even}', transform=self.ax.transAxes)
        self.ax.text(0.05, 0.80, f'Current Intrinsic Value: {round(current_value, 2)}', transform=self.ax.transAxes)
        self.ax.text(0.05, 0.75, f'Current P/L: {round(current_profit_loss, 2)}', transform=self.ax.transAxes)

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
