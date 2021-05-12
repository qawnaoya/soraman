import unittest
from soraman import baseclient
from soraman import client
from soraman import exception
from soraman import utility
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

    def test_getSoracomBeamConfigurationByName(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        g = soraman.getGroupIdsByName('SIMG')

        gn = g[0]

        g = soraman.getSoracomBeamConfigurationById(gn, 'http://beam.soracom.io:8888/iothub')
        print(g)

    def test_putConfiguration(self):
        soraman = client.japan_soraman()

        soraman.auth(authKeyId=self.authKeyId,authKey=self.authKey)
        g = soraman.getGroupIdsByName('SIMG')

        gn = g[0]

        azic = utility.build_AzureIoTCentral('AzureIoT')
        mqtt = utility.build_Beam_MQTT_configuration(destination='mqtts://IPRHUB.azure-devices.net:8883', addSubscriberHeader = True, customHeaders= {}, useAzureIoT=True, azureIoTCentral=azic)
        psk = utility.build_PresharedKey('M5TESTX')
        http = utility.build_Beam_HTTP_configuration('iothub', destination='https://IPRHUB.azure-devices.net/devices/M5TEST/messages/events?api-version=2018-06-30', enabled=True, addEquipmentHeader=True, addSignature=True, addSubscriberHeader=True, addSimIdHeader=False, addMsisdnHeader=True, psk = psk, replaceTopic=False)
        configurations = [mqtt, http]

        g = soraman.putConfigurationById(gn, 'SoracomBeam', configurations)
        print("Result", g)

if __name__ == "__main__":
    unittest.main()
