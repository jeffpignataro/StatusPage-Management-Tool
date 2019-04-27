import json


def sterilizeJsonStrings(string):
    return string.replace("'", "\\'")


def pretty(string):
    return json.dumps(string, sort_keys=True, indent=2)


def prettyprint(string):
    return print(pretty(string))
