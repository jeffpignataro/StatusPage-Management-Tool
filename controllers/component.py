import re
import json
import os
from helpers.gethelper import getRequest
from helpers.patchhelper import patchRequest
from helpers.posthelper import postRequest
from helpers.filehelper import getFileFromRelativePath
from enums.status import status as statusEnum


def createComponent(description, name, status, showcase, groupId, pageId=''):
    payload = {}
    payload["component"] = {}
    payload["component"]["description"] = description
    payload["component"]["status"] = status
    payload["component"]["name"] = name
    payload["component"]["only_show_if_degraded"] = "false"
    payload["component"]["group_id"] = groupId
    payload["component"]["showcase"] = "{showcase}".format(
        showcase=showcase).lower()
    if (pageId != ''):
        return postRequest("components", '', str(payload), pageId=pageId).json()
    return postRequest("components", '', str(payload)).json()


def getComponents(pageId=''):
    if (pageId != ''):
        return getRequest("components", pageId=pageId).json()
    return getRequest("components", pageId=pageId).json()


def getComponent(id, pageId=''):
    if (pageId != ''):
        return getRequest("components", id, pageId=pageId).json()
    return getRequest("components", id).json()


def updateComponent(componentId, description, name, status, showcase, groupId, pageId=''):
    payload = {}
    payload["component"] = {}
    payload["component"]["description"] = description
    payload["component"]["status"] = status
    payload["component"]["name"] = name
    payload["component"]["only_show_if_degraded"] = "false"
    payload["component"]["group_id"] = groupId
    payload["component"]["showcase"] = "{showcase}".format(
        showcase=showcase).lower()
    if (pageId != ''):
        return patchRequest("components", componentId, str(payload), pageId=pageId).json()
    return patchRequest("components", componentId, str(payload)).json()


def updateComponentStatus(componentId, status, pageId=''):
    component = getComponent(componentId, pageId)
    if("components" in component):
        return "Cannot update status of group component {name}".format(name=component["name"])
    return updateComponent(componentId, component["description"],
                           component["name"], status, component["showcase"], component["group_id"], pageId)


def getComponenetDependenciesFile():
    componenetDependenciesPathAndFile = '../data/componentDependencies.json'
    return open(getFileFromRelativePath(componenetDependenciesPathAndFile), 'r')


def getComponenetDependencies():
    componenetDependencies_json = json.load(getComponenetDependenciesFile())
    return componenetDependencies_json


def getComponentsByDependencies(dependency):
    c = getComponenetDependencies()
    onPremApps = []
    for comp in c:
        for dependency in comp["dependency"]:
            if (dependency == dependency.lower()):
                onPremApps.append(comp)
    return onPremApps


def getComponentByTag(tag):
    components = getComponents()
    regexResults = []
    returnList = []
    for c in components:
        regexResult = re.search(
            "^Tags:.*?$", str(c["description"]), re.MULTILINE)
        if (str(regexResult) != "None"):
            regexResults.append(
                {"id": c["id"], "name": c["name"], "dependency": regexResult.group(0).replace("Tags: ", "").split(",")})
    for result in regexResults:
        for tagResult in result["dependency"]:
            if (tagResult.strip().lower() == tag.strip().lower()):
                returnList.append(result)
                break
    return returnList
