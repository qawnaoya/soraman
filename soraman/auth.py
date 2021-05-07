import logging
import urllib.request
import urllib.error
import json
from soraman import exception

''' カバレッジタイプに依存しない認証を実装
'''

class soraman():
    API_ENDPOINT = None
    logger = None

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def authRequest(self, reqDoc):
        uri = self.API_ENDPOINT + '/auth'
        self.logger.info('Request URI: %s', uri)
        
        headers = {
            'Content-Type': 'application/json',
        }

        try:
            u = urllib.request.Request(uri, reqDoc, headers, method = 'POST')
            with urllib.request.urlopen(u) as f:
                print(f.read())
        except urllib.error.HTTPError as ex:
            print(ex)
            print(ex.filename)
            raise(ex)

    ''' ルートアカウントの認証を実装 '''

    def authAsRoot(self, email, password):
        reqObj = {'email': email, 'password': password}
        reqDoc = json.dumps(reqObj).encode('utf-8')
        self.authRequest(reqDoc)

    ''' SAMの認証を実装 '''

    def authAsSAM(self, operatorId, userName, password):
        pass

    ''' AuthKeyによる認証を実装 '''

    def authByAuthKey(self, authKeyId, authKey):
        reqObj = {'authKeyId': authKeyId, 'authKey': authKey}
        reqDoc = json.dumps(reqObj).encode('utf-8')
        self.authRequest(reqDoc)

    def auth(self, email = None, password = None, authKeyId = None, authKey = None, operatorId = None, userName = None):
        # Root Account
        if(email):
            if(password):
                self.authAsRoot(email, password)
            else:
                raise exception.ParameterException()

        # Auth Key
        elif(authKeyId):
            if(authKey):
                self.authByAuthKey(authKeyId, authKey)
            else:
                raise exception.ParameterException()

        # SAM
        elif(operatorId):
            if(userName):
                if(password):
                    self.authAsSAM(operatorId, userName, password)
                else:
                    raise exception.ParameterException()
            else:
                raise exception.ParameterException()

        # else
        else:
            raise Exception()

''' Global カバレッジの認証を実装
'''

class global_soraman(soraman):
    def __init__(self):
        super().__init__()
        self.API_ENDPOINT = 'https://g.api.soracom.io'

    def auth(self, email = None, password = None, authKeyId = None, authKey = None, operatorId = None, userName = None):
        super().auth(email, password, authKeyId, authKey, operatorId, userName)

''' Japan カバレッジの認証を実装
'''

class japan_soraman(soraman):
    def __init__(self):
        super().__init__()
        self.API_ENDPOINT = 'https://api.soracom.io'

    def auth(self, email = None, password = None, authKeyId = None, authKey = None, operatorId = None, userName = None):
        super().auth(email, password, authKeyId, authKey, operatorId, userName)
