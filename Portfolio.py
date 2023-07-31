import Stock 
import StockTransactionRecord as record

class Performance_Data():
    def __ini__(self):
        self.portfolio_value = 0.0
        total_profit_loss = 0.0
        self.num_trades = 0
        self.transaction_record = record()

class Portfolio():
    """                             Description of class
        Owned Stocks    
        Transaction History
        Cash Balance
        Watchlist
        Risk Management Parameters
        Trading Strategy Settings
        Portfolio Reports
        Watchlist Updates
    """
    def __init__(self):
        self.owned_stocks = []
        self.watchlist = []
        self.cash_balance = 0.0
        self.performance_data = Performance_Data()

    def add_stock(self, stock):
        stock = Stock(stock)
        if stock in self.owned_stocks:
            print('In function add_stock, a stock already in the list is trying to be added')
            breakpoint()
        self.owned_stocks.append(stock)

    def remove_stock(self, stock):
        stock = Stock(stock)
        if stock in self.owned_stocks:
            print('In function remove_stock, a stock not in the list is trying to be removed')
            breakpoint()
        self.owned_stocks.remove(stock)

    def add_to_watchlist(self, stock):
        stock = Stock(stock)
        if stock in self.owned_stocks:
            print('In function add_to_watchlist, a stock already in the list is trying to be added')
            breakpoint()
        self.watchlist.append(stock)

    def remove_from_watchlist(self, stock):
        stock = Stock(stock)
        if stock in self.owned_stocks:
            print('In function remove_from_watchlist, a stock not in the list is trying to be removed')
            breakpoint()
        self.watchlist.remove(stock)

    def display_portfolio(self):
        print("Portfolio:/n")
        for stock in self.owned_stocks:
            print(stock.company_name + '/n')

    def display_watchlist(self):
        print("Watchlist: /n")
        for stock in self.watchlist:
            print(stock.company_name + '/n')


