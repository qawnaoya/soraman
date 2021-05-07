import unittest
from soraman import auth
from soraman import exception
import configparser as cp

class GlobalAuthTest(unittest.TestCase):
    config = cp.ConfigParser()
    config.read('soracom.config')
    authKeyId = config['soracom']['authKeyId']
    authKey = config['soracom']['authKey']

    def test_except(self):
        soraman = auth.japan_soraman()

        try:
            soraman.auth(authKeyId=self.authKeyId)
            raise Exception
        except exception.ParameterException:
            pass

    def test_auth(self):
        soraman = auth.global_soraman()

        print(soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey))
    
    def test_getsub(self):
        soraman = auth.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        print(soraman.getSubscribers())

    def test_getgroups(self):
        soraman = auth.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        print(soraman.getGroups())

if __name__ == "__main__":
    unittest.main()
