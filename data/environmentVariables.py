import os
import json
from helpers.filehelper import getFileFromRelativePath


def getEnvironmentFile():
    environmentPathAndFile = '../config/environmentVariables.json'
    return open(getFileFromRelativePath(environmentPathAndFile), 'r')


def getDevPageId():
    environment_json = json.load(getEnvironmentFile())
    return environment_json['devPageId']


def getApiKey():
    environment_json = json.load(getEnvironmentFile())
    return environment_json['apikey']


def getPageId():
    environment_json = json.load(getEnvironmentFile())
    return environment_json['pageId']
