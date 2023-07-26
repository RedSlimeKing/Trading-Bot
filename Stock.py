import yfinance as yf
from datetime import date,timedelta

class Stock:
   """  Variables
        ticker = ''             holds stock symbol
        data   =                Downloaded data on stock 
   """
   def __init__(self, symbol):
        self.symbol = symbol
        self.company_name = None
        self.data = None
        self.start_date = (date.today()-timedelta(days=30)).isoformat()
        self.end_date = date.today().strftime('%Y-%m-%d')
        self.news = 'no news'
        self.purchase_price = 0.0
        self.info = None

   def fetch_data(self):
    #self.data = yf.download(self.symbol, start = self.start_date, end = self.end_date)
    self.data = yf.download(self.symbol, period='30d', interval='1d')
    self.info = yf.Ticker(self.symbol).info
    self.company_name = self.info['longName']
    self.data.head()
    self.data.reset_index(inplace=True)
    self.data.head()


    def get_news(self):
        self.news = yf.Ticker(self.symbol).news()
        return self.news



    def extend_range(self, new_date):
        if self.start_date < self.end_date:
         self.start_date = new_date

   