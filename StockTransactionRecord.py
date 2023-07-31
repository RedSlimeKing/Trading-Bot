import pandas as pd

class StockTransactionRecord(object):
    """                     description of class
        Records the transaction history of the portfolio
    """
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['Date', 'Stock', 'Action', 'Quantity', 'Price', 'Total'])
        self.transactions.set_index('Date', inplace=True)

    def record_transaction(self, date, stock, action, quantity, price):
        # Calculate the total value of the transaction
        total = quantity * price

        # Append the transaction to the DataFrame
        self.transactions.loc[date] = [stock, action, quantity, price, total]

    def get_transaction_history(self):
        return self.transactions

