import unittest
from soraman import client
from soraman import exception
import configparser as cp
import pandas as pd

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

        gd = [pd.DataFrame(m) for m in g]
        gd = pd.concat(gd)

        print(gd)

    def test_getgroups(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        g = soraman.getGroups()

        print(g)

        gd = [pd.DataFrame(m) for m in g]
        gd = pd.concat(gd)

        print(gd)

    def test_getgroupsByName(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        g = soraman.getGroupsByName('SIMG')

        print(g)

        gd = [pd.DataFrame(m) for m in g]
        gd = pd.concat(gd)

        print(gd)
    
    def test_getgroupConfigurationByName(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        
        sorahttp = soraman.getSoracomBeamConfigurationByName('SIMG', 'http://beam.soracom.io:8888/iothub')
        print(sorahttp)

    def test_getgroupConfigurationByName1(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        
        sorahttp = soraman.getConfigurationByName('SIMG', 'SoracomBeam')
        print(sorahttp)

if __name__ == "__main__":
    unittest.main()
