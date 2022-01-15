import os
from src.endpoints.endpoint import Endpoint
import pandas as pd

__all__ = ['Snapshot',]

class Snapshot(Endpoint):

    path = '/bars'
    base_url = os.getenv('APCA_API_DATA_URI')

    def __init__(self, 
                ticker, 
                start=None,
                end=None,
                limit=10,
                timeframe='15Min',
                adjustment=None,
                use_raw=False, 
                use_json=True):
        self.params = {
            'timeframe': timeframe
        }
        if not start:
            raise ValueError('Need to enter a start date')
        if start: self.params['start'] = start
        if end: self.params['end'] = end
        if limit: self.params['limit'] = limit
        super().__init__(ticker, self.params, use_raw, use_json,)


    def get_uri(self, version='v2'):
        uri = f'{self.base_url}/{version}{self.endpoint}/{self.ticker}{self.path}'  
        return uri


    def to_df(self):
        data = self.get()
        print(data)
        if 'bars' in data:
            df = pd.DataFrame(self.get()['bars'])
        if 'bar' in data:
            df = pd.DataFrame(self.get()['bar'])
        columns = {
            't': 'Timestamp',
            'o': 'OpenPrice',
            'h': 'HighNumber',
            'l': 'LowNumber',
            'c': 'ClosePrice',
            'v': 'Volume', 
            'n': 'NumberOfTrades',
            'vw': 'WeightedAvgPrice'
        }
        df.rename(columns=columns, inplace=True) 
        return df