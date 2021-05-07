import urllib
import json
from soraman import exception

''' カバレッジタイプに依存しない認証を実装
'''

class soraman():
    API_ENDPOINT = None

    ''' ルートアカウントの認証を実装 '''

    def authAsRoot(self, email, password):
        reqObj = {'email': email, 'password': password}
        reqDoc = json.dumps(reqObj)

    ''' SAMの認証を実装 '''

    def authAsSAM(self, operatorId, userName, password):
        pass

    ''' AuthKeyによる認証を実装 '''


    def authByAuthKey(self, authKeyId, authKey):
        pass

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
        self.API_ENDPOINT = ''

    def auth(self, email = None, password = None, authKeyId = None, authKey = None, operatorId = None, userName = None):
        super().auth(email, password, authKeyId, authKey, operatorId, userName)

''' Japan カバレッジの認証を実装
'''

class japan_soraman(soraman):
    def __init__(self):
        self.API_ENDPOINT = ''

    def auth(self, email = None, password = None, authKeyId = None, authKey = None, operatorId = None, userName = None):
        super().auth(email, password, authKeyId, authKey, operatorId, userName)
