from src.endpoints.endpoint import Endpoint

__all__ = ['Trades',]

class Trades(Endpoint):

    endpoint = '' # stocks
    path = '/trades'

    def __init__(self, 
                ticker=None,
                start=None,
                end=None,
                feed='IEX', 
                limit=1000,
                page=1,
                use_raw=False, 
                use_json=False):
        super().__init__(use_raw, use_json)
        self.ticker = ticker or self.__class__.__name__

    def get_uri(self, version='v2'):
        uri = f'{self._uri}{version}{self.endpoint}/{self.ticker}{self.path}'  
        return uri