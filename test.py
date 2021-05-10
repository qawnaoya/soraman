import unittest
from soraman import client
from soraman import exception
import configparser as cp

class GlobalAuthTest(unittest.TestCase):
    config = cp.ConfigParser()
    config.read('soracom.config')
    authKeyId = config['soracom']['authKeyId']
    authKey = config['soracom']['authKey']

    def test_except(self):
        soraman = client.japan_soraman()

        try:
            soraman.auth(authKeyId=self.authKeyId)
            raise Exception
        except exception.ParameterException:
            pass

    def test_auth(self):
        soraman = client.global_soraman()

        print(soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey))
    
    def test_getsub(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        g = soraman.getSubscribers()

        print(g)

    def test_getgroups(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        g = soraman.getGroups()

        print(g)

    def test_getgroupsByName(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        g = soraman.getGroupsByName('SIMG')

        print(g)
    
    def test_getGroupIdsByName(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        g = soraman.getGroupIdsByName('SIMG')

        print(g)
    
    def test_getGroupByName(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        g = soraman.getGroupIdsByName('SIMG')

        gn = g[0]

        g = soraman.getGroupById(gn)

    def test_getConfigurationByName(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        g = soraman.getGroupIdsByName('SIMG')

        gn = g[0]

        g = soraman.getConfigurationById(gn, 'SoracomBeam')
        print(g)

if __name__ == "__main__":
    unittest.main()
