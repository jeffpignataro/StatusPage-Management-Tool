from controllers.component import getComponent, updateComponent
from helpers.taghelper import getDescriptionWithoutTags, getTagListFromDescription
import re


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
    c = getComponent(componentId)
    try:
        descWithoutTags = getDescriptionWithoutTags(str(c["description"]))
        tagList = getTagListFromDescription(str(c["description"]))
        for i in tagList:
            if (tag.lower() == i.lower()):
                tagList.remove(i)
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
