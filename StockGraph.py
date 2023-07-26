import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns; sns.set()
import mplcursors
import Stock as sk
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd

class StockGraph:
    def __init__(self, stock_data):
        self.stock_data = stock_data
        self.stock_data.data.to_csv("stock_data.csv")

    def display_graph(self):
        plt.figure(figsize=(14,5))
        sns.set_style("ticks")
        sns.lineplot(data=self.stock_data.data,x="Date",y='Close',color='firebrick')
        sns.despine()
        plt.title('Stock Price Over Time',size='x-large',color='blue')
        plt.grid(True)

        cursor = mplcursors.cursor(hover=True)
        cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1]:.2f}"))

        plt.show()

    def plot_support_resistance1(self, tolerance=0.05):
        """             WOP
        Plots support and resistance levels on a price chart.

        Args:
            data (pandas.DataFrame): DataFrame containing historical price data.
            tolerance (float, optional): Tolerance level for identifying support and resistance levels.

        Returns:
            None (displays the plot).
        """
        
        prices = self.stock_data.data['Close']
        support_levels = []
        resistance_levels = []

        for i in range(1, len(prices) - 1):
            prev_price = prices[i-1]
            curr_price = prices[i]
            next_price = prices[i+1]

            if curr_price < prev_price and curr_price < next_price:
                support_levels.append((i, curr_price))
            elif curr_price > prev_price and curr_price > next_price:
                resistance_levels.append((i, curr_price))

        plt.figure(figsize=(14,5))
        for level in support_levels:
            plt.axhline(level[1] - tolerance, color='green', linestyle='--')
        for level in resistance_levels:
            plt.axhline(level[1] + tolerance, color='red', linestyle='--')
        plt.title('Support and Resistance Levels')
        sns.set_style("ticks")
        sns.lineplot(data=self.stock_data.data,x="Date",y='Close',color='firebrick')
        sns.despine()

        cursor = mplcursors.cursor(hover=True)
        cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1]:.2f}"))

        plt.show()

    def plot_candles(self, tolerance=0.05):
        """             WOP
        Plots candlestick chart.

        Args:
            data (pandas.DataFrame): DataFrame containing historical price data.
            tolerance (float, optional): Tolerance level for identifying support and resistance levels.

        Returns:
            None (displays the plot).
        """
        print('Start date: ' + self.stock_data.start_date)
        print('End date: ' + self.stock_data.end_date)
        # Prepare the data for the candlestick chart
        data = self.stock_data.data#pd.read_csv('stock_data.csv')  # Replace 'stock_data.csv' with your data file
        data['Date'] = pd.to_datetime(data['Date'])
        data['Date'] = data['Date'].apply(lambda x: x.date())

        ohlc = data[['Date', 'Open', 'High', 'Low', 'Close']].copy()
        ohlc['Date'] = pd.to_datetime(ohlc['Date']).map(mdates.date2num)
        # Create the candlestick chart
        fig, ax = plt.subplots()
        candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red')

        # Set x-axis labels as dates
        ax.xaxis_date()
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)

        # Set chart title and y-axis label
        plt.title('Stock Price')
        plt.ylabel('Price')

        # Display the chart
        plt.show()
