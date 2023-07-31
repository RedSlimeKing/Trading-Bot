import logging
import Stock as sk
import StockGraph as stock_graph
import time as wait_time
from datetime import datetime, time


"""                 Plan
    loop {
        Resolve commands from dashboard
        Data Acquisition
        Data Processing
        Analysis and Signal Generation
        Risk Management
        Order Placement
        Trade Excution and Monintoring
        Portfolio Management
    }

    Asynchronously Recieve command from Desktop Dashboard
    Excute commands

                    TO DO
     - Figure out how using fake money to test strategies will work into this
 """

def is_stock_market_open():
    now = datetime.now().time()
    opening_time = time(9, 30)  # US stock market opening time is 9:30 AM Eastern Time
    closing_time = time(16, 0)  # US stock market closing time is 4:00 PM Eastern Time

    if opening_time <= now <= closing_time:
        return True
    else:
        return False

def LogActivity():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    logging.info(f'Bot is performing an action. Current time: {current_time}')

"""         Flow
    {
        Recieve string from console command on computer
        Add command to queue in bots main loop
        Sends error message to bot
        If requesting data, send package Example:
                            { Cash_balance, Portfolio Performance, watchlist, owned_stocks, transaction_history, Activity_Logs }            
    }
    {
        Resolve commands from dashboard (Function)
            if statments that will buy,sell, add stock to watchlist, remove stock from watchlist,
                start, stop(cease transaction function until turned on), run analysis and return prediction on stock (Test/Back Test),
        Data Acquisition
            when stock is created it will gather info for 30 days, this function will refresh data for 5 min intervals or faster if deemed nessauray
        Data Processing
            Calculate daily returns (Daily_Return) based on the closing prices.
            Compute 50-day and 200-day Simple Moving Averages (SMA_50 and SMA_200) for the closing prices.
            Generate a Moving Average Crossover Signal (Signal) based on the SMA_50 and SMA_200.
            Identify days with high volume compared to the average volume (High_Volume).
            Identify days where the stock price increased (Price_Increase).
            Calculate the Maximum Drawdown (Drawdown) based on the cumulative returns.
        Analysis and Signal Generation
            run strategies and create signals for buying or selling
        Risk Management
            Determine a risk %
            Calculate the stop loss amount
            Other technique to look into { position sizing, diversification, trailing stop-loss orders, and setting maximum daily or overall loss limits }
        Order Placement
            we can use Questrade API
        Trade Excution
            Market Orders: These are orders executed immediately at the current market price. 
            Limit Orders: Specify a price at which you are willing to buy or sell.
            Stop Orders: Stop orders are used to trigger a market order once a certain price level is reached.
            Trailing Stop Orders: Trailing stops automatically adjust the stop price as the market price moves in your favor, 
                                  helping lock in profits while giving room for the position to grow.
        Excution Monintoring
            -
        Portfolio Management
            Update the internal portfolio data
            Position Sizing: Determine the size of each trade based on the bot's risk management rules and account size.
            Performance Monitoring
            If using more than one strategy, should gauge the preformance and determine if a new strategy is need
    }
"""

# Start of Program
current_time = datetime.datetime.now().strftime('%H:%M:%S')
logging.basicConfig(filename=f'Activity{current_time}.log', level=logging.INFO, format='%(asctime)s - %(message)s')


newStock = sk.Stock('ABVC')
newStock.fetch_data()

is_running = True         
while is_running:

    current_time = datetime.now().strftime("%I:%M %p")
    # Print the current time
    print("Current time:", current_time)

    if is_stock_market_open() is False:  # Change to False
        is_running = False
        print('Stock market is Closed')


    wait_time.sleep(3) # do 300 for 5 min wait

# Create an instance of the StockGraph class with the stock data
stock_graph = stock_graph.StockGraph(newStock)  
# Display the stock data in a graph
stock_graph.display_graph() 



# Program has ended
print("END")