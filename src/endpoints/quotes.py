from heapq import merge
import os
from src.endpoints.endpoint import Endpoint
import pandas as pd
import datetime

__all__ = ['Quotes',]

class Quotes(Endpoint):

    endpoint = '/stocks'
    path = '/quotes'
    base_url = os.getenv('APCA_API_DATA_URI')

    def __init__(self, 
                ticker=None, 
                start=None,
                use_raw=False, 
                use_json=True):
        self.params = {
            'start': '2022-01-14',
            'limit': 100,
        }
        super().__init__(ticker, self.params, use_raw, use_json,)


    def get_uri(self, version='v2'):
        uri = f'{self.base_url}/{version}{self.endpoint}/{self.ticker}{self.path}'  
        return uri


    def to_df(self):
        resp = self.get()
        df = pd.DataFrame(resp['quotes'])
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