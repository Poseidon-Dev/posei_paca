# Poseidon - Algo Trader

Poseidon Algo Trader is a wrapper around the Alpaca API
Future iterations will include different methodologies for trading

## Authors

**[Johnny Whitworth (@Poseidon-dev)](https://github.com/poseidon-dev)** 

## How to use 
The endpoint package will include all variations of Alpaca Endpoints
Currently includes:
[x] = Quotes
[ ] = Trades
[ ] = Bars

Basic Quote call
```python
stock = Quotes('AAPL').to_df()
```

Otherwise, you can create a ticker class enheriting from endpoints
Advanced Scenario
```python
class AAPL(Quotes):

    def __str__(self):
        return self.ticker

stock = AAPL().to_df()
```

Both instances will return the dataframe with basic params


## Support

If you need some help for something, please reach out to me directly or submit an issue and I'll get to it as soon as I can

## Site

https://poseidon-dev.github.io/ecms-api/
