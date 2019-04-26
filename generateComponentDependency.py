import json
import re
from controllers.component import getComponents, getComponentByTag

# This file is just a stub for a potential automated creation of the json file
# A better move might be to implement the tags in Statuspage since the logic is pretty easy
# The get by tag logic is already done
getComponentByTag("classic")

componentDependencyList = []
components = getComponents()
for c in components:
    componentDependencyList.append({"id": c["id"], "name": c["name"]})

with open('data/componentDependenciesGenerated.json', 'w') as outfile:
    outfile.write(json.dumps(componentDependencyList, indent=2))
