def build_header(apiKey, token):
    headers = {
        'X-Soracom-API-Key': apiKey,
        'X-Soracom-Token': token
    }

    return headers

