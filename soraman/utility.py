'''ヘッダ生成'''
def build_header(apiKey, token):
    headers = {
        'X-Soracom-API-Key': apiKey,
        'X-Soracom-Token': token
    }

    return headers

'''MQTT 設定'''
def build_Beam_MQTT_configuration(
    destination,
    enabled = True,
    addEquipmentHeader = False,
    addSignature = False,
    addSubscriberHeader = False,
    addSimIdHeader = False,
    customHeaders = {},
    skipStatusCode = False,
    useClientCert = False,
    useAzureIoT = False,
    azureIoTCentral = {
        '$credentialsId': 'AzureIoT'
    }
):
    configuration = {}

    configuration['key'] = 'mqtt://beam.soracom.io:1883'
    value = {}
    value['enabled'] = enabled
    value['name'] = 'MQTT'
    value['addEquipmentHeader'] = addEquipmentHeader
    value['addSignature'] = addSignature
    value['addSubscriberHeader'] = addSubscriberHeader
    value['addSimIdHeader'] = addSimIdHeader
    value['customHeaders'] = customHeaders
    value['skipStatusCode'] = skipStatusCode
    value['useClientCert'] = useClientCert
    value['useAzureIoT'] = useAzureIoT
    value['azureIoTCentral'] = azureIoTCentral
    value['destination'] = destination
    configuration['value'] = value

    return  configuration

def build_Beam_HTTP_configuration(
    path,
    destination,
    enabled = True,
    addEquipmentHeader = False,
    addSignature = False,
    addSubscriberHeader = False,
    addSimIdHeader = False,
    addMsisdnHeader = False,
    customHeaders = {},
    skipStatusCode = False,
    useClientCert = False,
    useClientCredentials = False,
    replaceTopic = False,
    psk = {
        '$credentialsId': 'AzureIoT'
    }
):
    configuration = {}

    configuration['key'] = 'http://beam.soracom.io:8888/{0}'.format(path)
    value = {}
    value['enabled'] = enabled
    value['name'] = 'HTTP'
    value['addEquipmentHeader'] = addEquipmentHeader
    value['addSignature'] = addSignature
    value['addSubscriberHeader'] = addSubscriberHeader
    value['addSimIdHeader'] = addSimIdHeader
    value['addMsisdnHeader'] = addMsisdnHeader
    value['psk'] = psk
    value['customHeaders'] = customHeaders
    value['skipStatusCode'] = skipStatusCode
    value['useClientCert'] = useClientCert
    value['useClientCredentials'] = useClientCredentials
    value['destination'] = destination
    value['replaceTopic'] = replaceTopic
    configuration['value'] = value

    return  configuration

def build_AzureIoTCentral(cert):
    azureIoTCentral = {
        '$credentialsId': cert
    }

    return azureIoTCentral

def build_PresharedKey(cert):
    azureIoTCentral = {
        '$credentialsId': cert
    }

    return azureIoTCentral
