import re


def getDescriptionWithoutTags(desc):
    desc = re.search("(^.*?)(\nTags:)", desc)
    try:
        return desc.group(1)
    except:
        return ""


def getTagStringFromDescription(desc):
    regexResult = re.search(
        "(^Tags:)(.*?$)", desc, re.MULTILINE)
    try:
        return regexResult
    except:
        return ''


def getTagListFromDescription(desc):
    try:
        return [x.strip() for x in getTagStringFromDescription(desc).group(2).split(",")]
    except:
        return []
