from data.environmentVariables import getPageId, getApiKey
import requests
from time import sleep


def getRequest(apiTopic, topicId='', payload='', pageId=''):
    if (pageId == ''):
        pageId = getPageId()
    apiKey = getApiKey()
    headers = {
        'Authorization': "Oauth {}".format(apiKey),
        'Host': "api.statuspage.io",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    sleep(.5)
    return requests.get("https://api.statuspage.io/v1/pages/{}/{}/{}".format(pageId, apiTopic, topicId), data=payload, headers=headers)
