import json


def sterilizeJsonStrings(string):
    return string.replace("'", "\\'")
