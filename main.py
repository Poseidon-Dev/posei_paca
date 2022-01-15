from src.endpoints import Endpoint, Trades, Quotes, Bars

stock = Bars('AAPL', start='2021-12-31').to_df()
print(stock)

