import os
import requests

__all__ = ['AlpacaConn', ]

class AlpacaConn:

    endpoint = '/account'
    base_url = os.getenv('APCA_API_BASE_URI')

    def __init__(self, data=None, use_raw=False, use_json=True):
        self._key_id, self._secret_key, self._oauth = self.get_creds()
        self.use_raw = use_raw
        self.use_json = use_json
        self._session = requests.Session()
        self._response = None
        self.data = data

    @property
    def headers(self):
        headers = {}
        if self._oauth:
            headers['Authorization'] = f'Bearer {self._oauth}'
        else:
            headers['APCA-API-KEY-ID'] = self._key_id
            headers['APCA-API-SECRET-KEY'] = self._secret_key
        return headers

    def _request(self, method, endpoint, headers={}, data=None, version='v2'):
        endpoint = endpoint or self.endpoint
        data = data or self.data
        uri = self.get_uri() 
        opts = {
            'headers': self.headers,
            'allow_redirects': False,
        }
        if method.upper() in ['GET', 'DELETE']:
            opts['params'] = data
        else:
            opts['json'] = data
        return self._session.request(method, uri, **opts)

    def get(self, endpoint=None, data=None):
        self._response = self._request('GET', endpoint, data)
        return self.response()

    def post(self, endpoint=None, data=None):
        self._response = self._request('POST', endpoint, data)
        return self.response()

    def put(self, endpoint=None, data=None):
        self._response = self._request('PUT', endpoint, data)
        return self.response()

    def patch(self, endpoint=None, data=None):
        self._response = self._request('PATCH', endpoint, data)
        return self.response()

    def delete(self, endpoint=None, data=None):
        self._response = self._request('DELETE', endpoint, data)
        return self.response()

    def response(self):
        if self._response.text != '':
            response = self._response
            if self.use_json:
                return self._response.json()

            else:
                return response.text
        else:
            return None

    def get_uri(self, version='v2'):
        return self.base_url + version + self.endpoint

    @staticmethod
    def get_creds(key_id=None, secret_key=None, oauth=None):
        oauth = oauth or os.getenv('APCA_API_OAUTH_TOKEN')
        key_id = key_id or os.getenv('APCA_API_KEY_ID')
        secret_key = secret_key or os.getenv('APCA_API_SECRET_KEY')

        if not key_id and not oauth:
            raise ValueError('Need key_id')
        if not secret_key and not oauth:
            raise ValueError('Need Secret Key')

        return key_id, secret_key, oauth

   
