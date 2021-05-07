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
        uri = self.API_ENDPOINT + '/v1/auth'
        self.logger.info('Request URI: %s', uri)
        
        headers = {
            'Content-Type': 'application/json',
        }

        try:
            u = urllib.request.Request(uri, reqDoc, headers, method = 'POST')
            with urllib.request.urlopen(u) as f:
                resDoc = f.read()
                resObj = json.loads(resDoc.decode('utf-8'))
                return(resObj)

        except urllib.error.HTTPError as ex:
            print(ex.read())
            raise(ex)

    ''' ルートアカウントの認証を実装 '''

    def authAsRoot(self, email, password):
        reqObj = {'email': email, 'password': password}
        reqDoc = json.dumps(reqObj).encode('utf-8')
        return(self.authRequest(reqDoc))

    ''' SAMの認証を実装 '''

    def authAsSAM(self, operatorId, userName, password):
        pass

    ''' AuthKeyによる認証を実装 '''

    def authByAuthKey(self, authKeyId, authKey):
        reqObj = {
            'authKey': authKey,
            'authKeyId': authKeyId,
            'email': '',
            'mfaOTPCode': '',
            'operatorId': '',
            'password': '',
            'tokenTimeoutSeconds': 86400,
            'userName': ''
        }
        reqDoc = json.dumps(reqObj).encode('utf-8')
        return(self.authRequest(reqDoc))

    def auth(self, email = None, password = None, authKeyId = None, authKey = None, operatorId = None, userName = None):
        # Root Account
        if(email):
            if(password):
                return(self.authAsRoot(email, password))
            else:
                raise exception.ParameterException()

        # Auth Key
        elif(authKeyId):
            if(authKey):
                return(self.authByAuthKey(authKeyId, authKey))
            else:
                raise exception.ParameterException()

        # SAM
        elif(operatorId):
            if(userName):
                if(password):
                    return(self.authAsSAM(operatorId, userName, password))
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
        return(super().auth(email, password, authKeyId, authKey, operatorId, userName))

''' Japan カバレッジの認証を実装
'''

class japan_soraman(soraman):
    def __init__(self):
        super().__init__()
        self.API_ENDPOINT = 'https://api.soracom.io'

    def auth(self, email = None, password = None, authKeyId = None, authKey = None, operatorId = None, userName = None):
        return(super().auth(email, password, authKeyId, authKey, operatorId, userName))
