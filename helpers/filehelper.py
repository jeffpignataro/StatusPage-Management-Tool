import os


def getFileFromRelativePath(pathAndFileName):
    current_path = os.path.dirname(__file__)
    return os.path.join(current_path, pathAndFileName)


def AddPageIdToFilename(pageId):
    return '-' + pageId if pageId != '' else ''
