import logging
import urllib.request
import urllib.error
import json
from soraman import baseclient, utility, exception

''' Global カバレッジの認証を実装
'''

class global_soraman(baseclient.soraman):
    def __init__(self):
        super().__init__()
        self.API_ENDPOINT = 'https://g.api.soracom.io'

    def auth(self, email = None, password = None, authKeyId = None, authKey = None, operatorId = None, userName = None):
        return(super().auth(email, password, authKeyId, authKey, operatorId, userName))

''' Japan カバレッジの認証を実装
'''

class japan_soraman(baseclient.soraman):
    def __init__(self):
        super().__init__()
        self.API_ENDPOINT = 'https://api.soracom.io'

    def auth(self, email = None, password = None, authKeyId = None, authKey = None, operatorId = None, userName = None):
        return(super().auth(email, password, authKeyId, authKey, operatorId, userName))
