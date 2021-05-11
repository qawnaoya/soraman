def build_header(apiKey, token):
    headers = {
        'X-Soracom-API-Key': apiKey,
        'X-Soracom-Token': token
    }

    return headers

def build_Beam_MQTT_configuration(
    enabled = True,
    addEquipmentHeader = False,
    addSignature = False,
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
    value['addSimIdHeader'] = addSimIdHeader
    value['customHeaders'] = customHeaders
    value['skipStatusCode'] = skipStatusCode
    value['useClientCert'] = useClientCert
    value['useAzureIoT'] = useAzureIoT
    value['azureIoTCentral'] = azureIoTCentral
    configuration['value'] = value

    return  configuration

def build_Beam_HTTP_configuration(
    path,
    enabled = True,
    addEquipmentHeader = False,
    addSignature = False,
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

    configuration['key'] = 'mqtt://beam.soracom.io:8888/{0}'.format(path)
    value = {}
    value['enabled'] = enabled
    value['name'] = 'MQTT'
    value['addEquipmentHeader'] = addEquipmentHeader
    value['addSignature'] = addSignature
    value['addSimIdHeader'] = addSimIdHeader
    value['customHeaders'] = customHeaders
    value['skipStatusCode'] = skipStatusCode
    value['useClientCert'] = useClientCert
    value['useAzureIoT'] = useAzureIoT
    value['azureIoTCentral'] = azureIoTCentral
    configuration['value'] = value

    return  configuration
