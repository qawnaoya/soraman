import logging
import urllib.request
import urllib.error
import json
from soraman import utility, exception

''' カバレッジタイプに依存しない認証を実装
'''

class soraman():
    API_ENDPOINT = None
    logger = None
    sessionInfo = None

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
                self.sessionInfo = resObj
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

    def getSubscribers(self):
        uri = self.API_ENDPOINT + '/v1/subscribers'
        self.logger.info('Request URI: %s', uri)
        
        headers = utility.build_header(self.sessionInfo['apiKey'], self.sessionInfo['token'])

        try:
            u = urllib.request.Request(uri, headers=headers, method='GET')
            with urllib.request.urlopen(u) as f:
                resDoc = f.read()
                resObj = json.loads(resDoc.decode('utf-8'))
                return(resObj)

        except urllib.error.HTTPError as ex:
            print(ex.read())
            raise(ex)

    def getGroups(self):
        uri = self.API_ENDPOINT + '/v1/groups'
        self.logger.info('Request URI: %s', uri)
        
        headers = {
            'X-Soracom-API-Key': self.sessionInfo['apiKey'],
            'X-Soracom-Token': self.sessionInfo['token']
        }

        try:
            u = urllib.request.Request(uri, headers=headers, method='GET')
            with urllib.request.urlopen(u) as f:
                resDoc = f.read()
                resObj = json.loads(resDoc.decode('utf-8'))
                return(resObj)

        except urllib.error.HTTPError as ex:
            print(ex.read())
            raise(ex)

    def getGroupById(self, id):
        uri = self.API_ENDPOINT + '/v1/groups/{0}'
        uri = uri.format(id)
        self.logger.info('Request URI: %s', uri)

        headers = utility.build_header(self.sessionInfo['apiKey'], self.sessionInfo['token'])

        try:
            u = urllib.request.Request(uri, headers=headers, method='GET')
            with urllib.request.urlopen(u) as f:
                resDoc = f.read()
                resObj = json.loads(resDoc.decode('utf-8'))
                return(resObj)

        except urllib.error.HTTPError as ex:
            print(ex.read())
            raise(ex)

    def getGroupsByName(self, name):
        uri = self.API_ENDPOINT + '/v1/groups?tag_name={0}&tag_value={1}'
        uri = uri.format('name', name)

        self.logger.info('Request URI: %s', uri)

        headers = utility.build_header(self.sessionInfo['apiKey'], self.sessionInfo['token'])

        try:
            u = urllib.request.Request(uri, headers=headers, method='GET')
            with urllib.request.urlopen(u) as f:
                resDoc = f.read()
                resObj = json.loads(resDoc.decode('utf-8'))
                return(resObj)

        except urllib.error.HTTPError as ex:
            print(ex.read())
            raise(ex)
    
    def getGroupIdsByName(self, name):
        groups = self.getGroupsByName(name)

        return [g['groupId'] for g in groups]

    def getConfigurationById(self, id, configuration_name):
        group = self.getGroupById(id)

        configuration = group['configuration']
        soracom_beam = configuration[configuration_name]

        return soracom_beam

    def getSoracomBeamConfigurationById(self, id, configuration_name):

        soracom_beam = self.getConfigurationById(id, 'SoracomBeam')
        beam_configuration = soracom_beam[configuration_name]

        return beam_configuration
