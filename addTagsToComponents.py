from controllers.component import getComponents, getComponent, updateComponent
from data.environmentVariables import getDevPageId
import re


def addTagsToAllComponents():
    # This will likely never be run again, but it helped to add the tag stubs for all the components
    components = getComponents()
    for c in components:
        desc = str(c["description"])
        if ("Tags: " not in desc):
            desc += "\nTags: "
            updateComponent(c["id"], desc, c["name"],
                            c["status"], c["showcase"], c["group_id"])
        print(desc)


def addTagToComponent(componentId, tag):
    # Still working on this function...
    c = getComponent(componentId, getDevPageId())
    desc = re.search("(^.*?)(\nTags:)", str(c["description"]))
    descWithoutTags = desc.group(1)
    regexResult = re.search(
        "(^Tags:)(.*?$)", str(c["description"]), re.MULTILINE)
    tagList = regexResult.group(2).split(",")
    if (not tagList.__contains__(tag)):
        tagList.append(tag)
    if (len(tagList) > 1 and len(tagList[0]) > 0):
        # if there's already tags
        strTagList = ", ".join(tagList)
    else:
        # if there's no existing tags
        strTagList = "".join(tagList)
    return updateComponent(c["id"], "{descWithoutTags}\nTags:{tagList}".format(descWithoutTags=descWithoutTags, tagList=strTagList), c["name"], c["status"],
                           c["showcase"], c["group_id"], getDevPageId())


def removeTagFromComponent(componentId, tag):
    return None


print(addTagToComponent('5cyx5tl8zwrn', 'SSO'))
