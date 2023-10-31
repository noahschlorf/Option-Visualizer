from strategies import CallOption, PutOption

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StrategyVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Option Strategy Visualizer')
        self.geometry('800x600')

        # Dropdown menu for selecting the strategy
        self.strategy_label = ttk.Label(self, text="Select Strategy:")
        self.strategy_label.pack()
        self.selected_strategy = tk.StringVar()
        self.strategies = {'Call Option': CallOption, 'Put Option':PutOption}  # Add more strategies as needed
        self.strategy_menu = ttk.Combobox(self, textvariable=self.selected_strategy, values=list(self.strategies.keys()))
        self.strategy_menu.pack()

        # Input for strike price
        self.strike_price_label = ttk.Label(self, text="Strike Price:")
        self.strike_price_label.pack()
        self.strike_price_entry = ttk.Entry(self)
        self.strike_price_entry.pack()

        # Input for option price (premium paid)
        self.premium_paid_label = ttk.Label(self, text="Option Price (Premium Paid):")
        self.premium_paid_label.pack()
        self.premium_paid_entry = ttk.Entry(self)
        self.premium_paid_entry.pack()

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

        # Get the parameters from the entries
        strike_price = float(self.strike_price_entry.get())
        premium_paid = float(self.premium_paid_entry.get())

        # Create an instance of the strategy class
        strategy = strategy_class(strike_price, premium_paid)

        # Assuming that each strategy class has a method to calculate the payoff
        stock_prices = np.linspace(0, strike_price*2, 100)
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
        self.ax.text(0.05, 0.95, f'Max Profit: {"Unlimited" if max_profit == np.inf else max_profit}', transform=self.ax.transAxes)
        self.ax.text(0.05, 0.90, f'Max Loss: {max_loss}', transform=self.ax.transAxes)
        self.ax.text(0.05, 0.85, f'Break-even: {break_even}', transform=self.ax.transAxes)

        #self.ax.axvline(x=break_even, color='green', linestyle='--', label='Break-even Price')

        #self.ax.legend(loc='lower left')
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

# Example usage with the string 'CallOption'
formatted_string = add_space_before_capitals('CallOption')
print(formatted_string) # This will print 'Call Option'


if __name__ == "__main__":
    app = StrategyVisualizer()
    app.mainloop()
