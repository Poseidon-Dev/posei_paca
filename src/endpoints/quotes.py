import os
from src.endpoints.endpoint import Endpoint
import pandas as pd

__all__ = ['Quotes',]

class Quotes(Endpoint):

    path = '/quotes'
    base_url = os.getenv('APCA_API_DATA_URI')

    def __init__(self, 
                ticker, 
                start=None,
                end=None,
                limit=10,
                latest=False,
                use_raw=False, 
                use_json=True):
        self.params = {}
        self.latest = latest
        if not latest:
            if not start:
                raise ValueError('If not looking at the lastest value, need to enter a start date')
            if start: self.params['start'] = start
            if end: self.params['end'] = end
            if limit: self.params['limit'] = limit
        super().__init__(ticker, self.params, use_raw, use_json,)


    def get_uri(self, version='v2'):
        uri = f'{self.base_url}/{version}{self.endpoint}/{self.ticker}{self.path}'  
        if self.latest:
            uri += '/latest'
        return uri


    def to_df(self):
        data = self.get()
        if 'quotes' in data:
            df = pd.DataFrame(self.get()['quotes'])
        if 'quote' in data:
            df = pd.DataFrame(self.get()['quote'])
        columns = {
            't': 'Timestamp',
            'ax': 'AskExchange',
            'ap': 'AskPrice',
            'as': 'AskSize',
            'bx': 'BidExchange',
            'bp': 'BidPrice', 
            'bs': 'BidSize',
            'c': 'QuoteConditions'
        }
        df.rename(columns=columns, inplace=True) 
        return df