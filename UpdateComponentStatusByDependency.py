from controllers.component import getComponentsByDependencies, updateComponentStatus
from data.environmentVariables import getDevPageId
from enums.status import status
from enums.dependency import dependency


def updateComponentStatusByDependency(tag, status):
    components = getComponentsByDependencies(tag)
    for c in components:
        updateComponentStatus(c["id"], status)
    print('{tag} apps updated with status {status}'.format(
        tag=tag, status=status))
