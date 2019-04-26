import re


def getDescriptionWithoutTags(desc):
    desc = re.search("(^.*?)(\nTags:)", desc)
    try:
        return desc.group(1)
    except:
        return ""


def getTagListFromDescription(desc):
    regexResult = re.search(
        "(^Tags:)(.*?$)", desc, re.MULTILINE)
    try:
        return [x.strip() for x in regexResult.group(2).split(",")]
    except:
        return []
