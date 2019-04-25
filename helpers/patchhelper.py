# https://api.statuspage.io/v1/pages/{page_id}/components/{component_id}
from data.environmentVariables import getPageId, getApiKey
import json
import requests
from time import sleep

# Payload Format
# {
#     "component": {
#         "description": "string",
#         "status": "operational",
#         "name": "string",
#         "only_show_if_degraded": true,
#         "group_id": "string",
#         "showcase": true
#     }
# }


def patchRequest(apiTopic, topicId='', payload='', pageId=''):
    if (pageId == ''):
        pageId = getPageId()
    apiKey = getApiKey()
    headers = {
        'Authorization': "Oauth {}".format(apiKey),
        'Host': "api.statuspage.io",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
        'Content-Type': 'application/json'
    }
    payload = payload.replace("'", "\"")
    sleep(1.1)
    return requests.patch("https://api.statuspage.io/v1/pages/{pageId}/{apiTopic}/{topicId}".format(pageId=pageId, apiTopic=apiTopic, topicId=topicId), data=payload, headers=headers)
