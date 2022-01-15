from src.endpoints import Endpoint, Trades, Quotes



stock = Quotes('DOCN').to_df()
print(stock)
