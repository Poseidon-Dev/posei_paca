from src.endpoints import Endpoint, Trades, Quotes

stock = Quotes('AAPL').to_df()
print(stock)
