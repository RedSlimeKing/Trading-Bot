import logging
import time as wait_time
from datetime import datetime, time
from threading import Thread
import Portfolio as pf

def is_stock_market_open():
    now = datetime.now().time()
    opening_time = time(9, 30)  # US stock market opening time is 9:30 AM Eastern Time
    closing_time = time(16, 0)  # US stock market closing time is 4:00 PM Eastern Time

    if opening_time <= now <= closing_time:
        return True
    else:
        return False

def LogActivity():
    current_time = datetime.now().strftime('%H:%M:%S')
    logging.info(f'Bot is performing an action. Current time: {current_time}')

"""         Flow
    {
        Recieve string from console command on computer
        Add command to queue in bots main loop
        Sends error message from bot
        If requesting data, send package Example:
                            { Cash_balance, Portfolio, Activity_Logs }            
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

def message_handler(commands):
    message = 'Buy'
    commands.append(message)
    return commands

def handle_commands(_commands):
    for command in _commands:
        if command == 'Buy':
            print('buy[]')
            """                                 Should pass 
                Symbol
                Quanitiy
                Order type { Market Orders, Limit Orders }
                    IF Limit Order = Limit_price

            """
        elif command == 'Sell':
            print('Sell[]')
            """                                 Should pass 
                Symbol
                Quanitiy
                Order type { Stop Orders, Trailling Stop Orders }
                Stop Price  
                    IF Trailling Stop Orders = trailing_percent

            """
        elif command == 'Add stock to watchlist':
            print('Add stock to watchlist[]')
            """                                 Should pass 
                Symbol
                
                - add to watchlist
                - analysis 
                - store prediction
                - queue to wait for right time to buy
            """
        elif command == 'Remove stock from watchlist':
            print('Remove stock from watchlist[]')
            """                                 Should pass 
                Symbol
                
                - Remove to watchlist
            """
        elif command == 'Start':
            print('Start[]')
            """                                
                Set inner status_value to true, will run between Data acqusition to Excution Monintoring
            """

        elif command == 'Stop':
            print('Stop[]')
            """                                
                Set inner status_value to false, will not run code from Data acqusition to Excution Monintoring but will still run handle_commands and portfolio management
            """
        elif command == 'Commands':
            print('Commands[]')
            """                                
                Send list of commands to dashboard
            """
        elif command == 'Update':
            print('Sending package')
            """                                
                Send a package of data to update dashboard UI, mainly send by program and not user
            """
        else:
            print('Not a recogniced command')
            """                                
                Sends message back to user on failure to understand command with what user sent
            """

def update_stock_data():
    print('update stocks data: Data Acquisition')
    # update stocks that are currently owned
    # update watched stocks
    # update stock that are waiting for time to purchase

def prep_data():
    print('prossess data: Data Processing')

def analysis():
    print('analysis')

# Start of Program
current_date = datetime.today().strftime("%d-%m-%Y")
logging.basicConfig(filename=f'Activity/Activity{current_date}.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Queue for commands by thread
commands = []

# Bot's Portfolio
portfolio = pf()

# Runs message_handler to recieve commands from console
thread = Thread(target=message_handler, args=(commands,))
thread.start()

is_running = True         
while is_running:
    #Resolve commands from dashboard
    handle_commands(commands)
    
    
    if is_stock_market_open() is True:  
        print('a')
    
        # Data Acquisition
        update_stock_data()
        # Data Processing
        prep_data()
        # Analysis and Signal Generation
        analysis()
        # Risk Management

        # Order Placement
        # Trade Excution
        # Excution Monintoring
        
    # Portfolio Management
    """

    """
    wait_time.sleep(3) # do 300 for 5 min wait

# Program has ended
print("END")


"""
    # Print the current time
    current_time = datetime.now().strftime("%I:%M %p")
    print("Current time:", current_time)
"""