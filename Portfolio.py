import Stock 

class Portfolio():
    """description of class"""
    def __init__(self):
        self.stocks = []
        self.watchlist = []

    def add_stock(self, stock):
        stock = Stock(stock)
        if stock in self.stocks:
            print('In function add_stock, a stock already in the list is trying to be added')
            breakpoint()
        self.stocks.append(stock)

    def remove_stock(self, stock):
        stock = Stock(stock)
        if stock in self.stocks:
            print('In function remove_stock, a stock not in the list is trying to be removed')
            breakpoint()
        self.stocks.remove(stock)

    def add_to_watchlist(self, stock):
        stock = Stock(stock)
        if stock in self.stocks:
            print('In function add_to_watchlist, a stock already in the list is trying to be added')
            breakpoint()
        self.watchlist.append(stock)

    def remove_from_watchlist(self, stock):
        stock = Stock(stock)
        if stock in self.stocks:
            print('In function remove_from_watchlist, a stock not in the list is trying to be removed')
            breakpoint()
        self.watchlist.remove(stock)

    def display_portfolio(self):
        print("Portfolio:/n")
        for stock in self.stocks:
            print(stock.company_name + '/n')

    def display_watchlist(self):
        print("Watchlist: /n")
        for stock in self.watchlist:
            print(stock.company_name + '/n')


