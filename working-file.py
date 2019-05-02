from controllers.component import *
from helpers.jsonhelper import prettyprint

components = getComponents()
for c in components:
    if ((str(c["name"]).__contains__("Jira") or str(c["name"]).__contains__("Confluence")) and str(c["id"]) != "c0trd0wvb0f4"):
        print(c["group_id"], end='|')
        print(c["id"], end='|')
        print(c["status"], end='|')
        print(c["showcase"], end='|')
        print(c["name"], end='|')
        print(c["description"])
        # if (not c["group_id"]):
        #     print(updateComponent(c["id"], '', c["name"],
        #                           c["status"], 'false', 'c0trd0wvb0f4'))
