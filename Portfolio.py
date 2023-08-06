import Stock 
import StockTransactionRecord as record

class Performance_Data():
    def __ini__(self):
        self.portfolio_value = 0.0
        self.total_profit_loss = 0.0
        self.num_trades = 0

class API_Setting():
    def __init__(self):
        self.api_base_url = None
        self.access_token = None
        self.account_number = None

class Owned_Stock():
    def __init__(self):
        self.stock = None
        self.purchase_price = 0.0
        self.quanitiy = 0
        self.total_value = 0.0
        self.current_price = 0.0

    def update_value():
        # Get Current Value of stock
        self.current_price = 0.0 #Get stock current price
        self.total_value = self.current_value * self.quanitiy

class Potental_Stock():
    def __init__(self):
        self.stock = None
        self.ideal_price = 0.0
        self.current_price = 0.0

    def update_value():
        # Get Current Value of stock
        self.current_price = 0.0 #Get stock current price
      

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
        self.owned_stocks = {}
        self.watchlist = []
        self.potental_stocks = []
        self.cash_balance = 0.0
        self.performance_data = Performance_Data()
        self.transaction_record = record()
        self.api_settings = API_Setting()

    def add_stock(self, _stock):
        
        if _stock.stock.company_name in self.owned_stocks:
            print('In function add_stock, a stock already in the list is trying to be added')
        else:
            self.owned_stocks[_stock.stock.company_name] = _stock

    def remove_stock(self, _stock):
        if _stock.stock.company_name in self.owned_stocks:
            del self.owned_stocks[_stock.stock.company_name]
        else:
            print('In function remove_stock, a stock not in the list is trying to be removed')

    def add_to_watchlist(self, stock):
        stock = Stock(stock)
        if stock in self.owned_stocks:
            print('In function add_to_watchlist, a stock already in the list is trying to be added')
        self.watchlist.append(stock)

    def remove_from_watchlist(self, stock):
        stock = Stock(stock)
        if stock in self.owned_stocks:
            print('In function remove_from_watchlist, a stock not in the list is trying to be removed')
        self.watchlist.remove(stock)

    def display_watchlist(self):
        print("Watchlist: /n")
        for stock in self.watchlist:
            print(stock.company_name + '/n')

    def Set_API_Setting(self, _api_base_url, _access_token, _account_number):
         self.api_settings.api_base_url = _api_base_url
         self.api_settings.access_token = _access_token
         self.api_settings.account_number = _account_number




