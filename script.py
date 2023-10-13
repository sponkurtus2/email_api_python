import requests
import json
from enum import Enum


class ApiClient:
    apiUri = 'https://api.elasticemail.com/v2'
    apiKey = '20E412E3A66F26EBACF5C280D1EF33763D983803CC63FA32ADEF420DC66BDB359F114FBF5027A1931BD02BBBF6E071BB'

    def Request(method, url, data):
        data['apikey'] = ApiClient.apiKey
        if method == 'POST':
            result = requests.post(ApiClient.apiUri + url, data=data)
        elif method == 'PUT':
            result = requests.put(ApiClient.apiUri + url, data=data)
        elif method == 'GET':
            attach = ''
            for key in data:
                attach = attach + key + '=' + data[key] + '&'
            url = url + '?' + attach[:-1]
            result = requests.get(ApiClient.apiUri + url)

        jsonMy = result.json()

        if jsonMy['success'] is False:
            return jsonMy['error']

        return jsonMy['data']


def Send(subject, EEfrom, fromName, to, bodyHtml, bodyText, isTransactional):
    return ApiClient.Request('POST', '/email/send', {
        'subject': subject,
        'from': EEfrom,
        'fromName': fromName,
        'to': to,
        'bodyHtml': bodyHtml,
        'bodyText': bodyText,
        'isTransactional': isTransactional})


print(Send("Api De Emails", "sponkurtus098@gmail.com", "Carlitos Api´s", "sponkurtus3@gmail.com",
           "<h1>Holi, api funcionando al 100!</h1>", "Text Body", True))
