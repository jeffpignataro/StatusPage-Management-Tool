import re
import json
import os
from warnings import warn
from helpers.taghelper import getTagStringFromDescription
from helpers.gethelper import getRequest
from helpers.patchhelper import patchRequest
from helpers.posthelper import postRequest
from helpers.filehelper import getFileFromRelativePath
from helpers.jsonhelper import sterilizeJsonStrings, pretty, prettyprint
from enums.status import status as statusEnum


def createComponent(description, name, status, showcase, groupId='None', pageId=''):
    payload = {}
    payload["component"] = {}
    payload["component"]["description"] = description
    payload["component"]["status"] = status
    payload["component"]["name"] = name
    payload["component"]["only_show_if_degraded"] = "false"
    if(str(groupId) != "None"):
        payload["component"]["group_id"] = groupId
    payload["component"]["showcase"] = "{showcase}".format(
        showcase=showcase).lower()
    return postRequest("components", '', str(payload), pageId=pageId)


def getComponents(pageId=''):
    return getRequest("components", pageId=pageId)


def getComponentsWithoutGroups(pageId=''):
    components = getComponents(pageId)
    for c in components:
        if (str(c["group"]).lower() == 'true'):
            # this doesn't remove from the list for some reason....
            components.remove(c)
    return components


def getComponent(id, pageId=''):
    return getRequest("components", id, pageId)


def updateComponent(componentId, description, name, status, showcase, groupId, pageId=''):
    payload = {}
    payload["component"] = {}
    payload["component"]["description"] = description
    payload["component"]["status"] = status
    payload["component"]["name"] = name
    payload["component"]["only_show_if_degraded"] = "false"
    if(str(groupId) != "None"):
        payload["component"]["group_id"] = groupId
    payload["component"]["showcase"] = "{showcase}".format(
        showcase=showcase).lower()
    return patchRequest("components", componentId, payload, pageId=pageId)


def updateComponentStatus(componentId, status, pageId=''):
    component = getComponent(componentId, pageId)
    if("components" in component):
        return "Cannot update status of group component {name}".format(name=component["name"])
    return updateComponent(componentId, component["description"],
                           component["name"], status, component["showcase"], component["group_id"], pageId)


def getComponenetDependenciesFile():
    componenetDependenciesPathAndFile = '../data/componentDependencies.json'
    return open(getFileFromRelativePath(componenetDependenciesPathAndFile), 'r')


def getComponentDependencies():
    componenetDependencies_json = json.load(getComponenetDependenciesFile())
    return componenetDependencies_json


def getComponentsByDependencies(tag):
    c = getComponentDependencies()
    apps = []
    for comp in c:
        for dependency in comp["tags"]:
            if (tag.lower() == dependency.lower()):
                apps.append(comp)
    return apps


def getComponentsByTag(tag, pageId=''):
    regexResults = getAllComponentsTags(pageId)
    returnList = []
    for result in regexResults:
        for tagResult in result["tags"]:
            if (tagResult.strip().lower() == tag.strip().lower()):
                returnList.append(result)
    return returnList


def getAllComponentsTags(pageId=''):
    # Groups shouldn't ever be tagged because they don't have statuses
    components = getComponentsWithoutGroups(pageId)
    regexResults = []
    for c in components:
        regexResults.append(
            {"id": c["id"], "name": c["name"], "tags": [i.strip() for i in getTagStringFromDescription(str(c["description"])).group(2).split(",")]})
    return regexResults
