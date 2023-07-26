import logging
import Stock as sk
import StockGraph as stock_graph
import time as wait_time
from datetime import datetime, time


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


logging.basicConfig(filename='BotsActivity.log', level=logging.INFO, format='%(asctime)s - %(message)s')


newStock = sk.Stock('GOOG')
newStock.fetch_data()
print(newStock.company_name)

is_running = True         
while is_running:

    current_time = datetime.now().strftime("%I:%M %p")
    # Print the current time
    print("Current time:", current_time)

    if is_stock_market_open() is True:  # Change to False
        is_running = False
        print('Stock market is Closed')


    wait_time.sleep(3) # do 300 for 5 min wait

stock_graph = stock_graph.StockGraph(newStock)  # Create an instance of the StockGraph class with the stock data
#stock_graph.display_graph()  # Display the stock data in a graph
stock_graph.plot_support_resistance1()
#stock_graph.plot_candles()
print("END")



"""
msft = yf.Ticker("MSFT")

# get all stock info
stockinfo = msft.info

# get historical market data
hist = msft.history(period="1mo")

# show meta information about the history (requires history() to be called first)
msft.history_metadata

# show actions (dividends, splits, capital gains)
msft.actions
msft.dividends
msft.splits
msft.capital_gains  # only for mutual funds & etfs

# show share count
msft.get_shares_full(start="2022-01-01", end=None)

# show financials:
# - income statement
msft.income_stmt
msft.quarterly_income_stmt
# - balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet
# - cash flow statement
msft.cashflow
msft.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
msft.major_holders
msft.institutional_holders
msft.mutualfund_holders

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
msft.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# show news
msft.news

"""

