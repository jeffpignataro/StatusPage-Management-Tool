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
    desc = re.search("^.*?\r\nTags:", str(c["description"]))
    descWithoutTags = re.sub("\r\nTags:.?", '', desc.group(0))
    regexResult = re.search("^Tags:.*?$", str(c["description"]), re.MULTILINE)
    tagList = re.sub("^Tags:.?", '', regexResult.group(0)).split(",")
    if (not tagList.__contains__(tag)):
        tagList.append(tag)
    return updateComponent(c["id"], "{descWithoutTags}\r\n{tagList}".format(descWithoutTags=descWithoutTags, tagList=tagList), c["name"], c["status"],
                           c["showcase"], c["group_id"])


def removeTagFromComponent(componentId, tag):
    return None


print(addTagToComponent('65w9m7yqs4dl', 'OnPrem'))
