from src.conn import AlpacaConn

__all__ = ['Endpoint',]

class Endpoint(AlpacaConn):
    
    endpoint = '/stocks' # stocks
    path = '' # trades

    def __init__(self, ticker=None, params=None, use_raw=False, use_json=False, ):
        self.ticker = ticker or self.__class__.__name__
        super().__init__(params, use_raw, use_json)

