from controllers.component import getComponentsByDependencies, updateComponentStatus
from data.environmentVariables import getDevPageId
from enums.status import status
from enums.dependency import dependency


components = getComponentsByDependencies(dependency.onprem.name)

for c in components:
    print(updateComponentStatus(
        c["id"], status.operational.name))
    break
