import json
from controllers.component import getAllComponentsTags
from helpers.filehelper import AddPageIdToFilename
from data.environmentVariables import getDevPageId

# This file is just a stub for a potential automated creation of the json file
# A better move might be to implement the tags in Statuspage since the logic is pretty easy
# The get by tag logic is already done
pageId = getDevPageId()
componentDependencyList = []
components = getAllComponentsTags(pageId)

for c in components:
    componentDependencyList.append(
        {"id": c["id"], "name": c["name"], "tags": c["tags"]})
with open('data/componentDependenciesGenerated{}.json'.format(AddPageIdToFilename(pageId)), 'w') as outfile:
    outfile.write(json.dumps(componentDependencyList, indent=2))
print("Dependency file generated")
