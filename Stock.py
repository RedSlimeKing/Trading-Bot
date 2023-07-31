import yfinance as yf
from datetime import date,timedelta

class Stock:
   """                  Variables
        symbol =               holds stock symbol
        data   =               holds download data on stock from yahoo finance
        start_date             
        end_date               
   """
   def __init__(self, symbol):
        self.symbol = symbol
        self.company_name = None
        self.data = None
        self.start_date = (date.today()-timedelta(days=30)).isoformat()
        self.end_date = date.today().strftime('%Y-%m-%d')

   def fetch_data(self):
    self.data = yf.download(self.symbol, start = self.start_date, end = self.end_date)
    #self.data = yf.download(self.symbol, period='30d', interval='1d')
    #self.info = yf.Ticker(self.symbol).info
    #self.company_name = self.info['longName']
    self.data.head()
    self.data.reset_index(inplace=True)
    self.data.head()

   