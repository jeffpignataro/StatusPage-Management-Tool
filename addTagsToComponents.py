from controllers.component import getComponents, getComponent, getComponentsByDependencies, updateComponent
from data.environmentVariables import getDevPageId
from helpers.taghelper import getDescriptionWithoutTags, getTagListFromDescription
import re


def addTagsTextToAllComponents():
    # This will likely never be run again, but it helped to add the tag stubs for all the components
    components = getComponents()
    for c in components:
        desc = str(c["description"])
        if ("Tags:" not in desc):
            desc += "\nTags: "
            print(updateComponent(c["id"], desc, c["name"],
                                  c["status"], c["showcase"], c["group_id"]))


def addTagsTextToSingleComponents(id):
    # This will likely never be run again, but it helped to add the tag stubs for all the components
    c = getComponent(id)
    desc = str(c["description"])
    if ("Tags:" not in desc):
        desc += "\nTags: "
        print(updateComponent(c["id"], desc, c["name"],
                              c["status"], c["showcase"], c["group_id"]))


def addTagToComponent(componentId, tag):
    c = getComponent(componentId)
    try:
        descWithoutTags = getDescriptionWithoutTags(str(c["description"]))
        tagList = getTagListFromDescription(str(c["description"]))
        if (tag not in tagList):
            tagList.append(tag)
        if (len(tagList) > 1 and len(tagList[0]) > 0):
            # if there's already tags
            strTagList = ", ".join(tagList)
        else:
            # if there's no existing tags
            strTagList = "".join(tagList)
        return updateComponent(c["id"], "{descWithoutTags}\nTags: {tagList}".format(descWithoutTags=descWithoutTags, tagList=strTagList), c["name"], c["status"],
                               c["showcase"], c["group_id"])
    except:
        return "Group Component - No tag to set"


def removeTagFromComponent(componentId, tag):
    return None


print(addTagToComponent('mmhsvy7tvvty', 'SSO'))
