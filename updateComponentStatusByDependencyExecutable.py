import sys
from updateComponentStatusByDependency import updateComponentStatusByDependency

updateComponentStatusByDependency(tag=sys.argv[1], status=sys.argv[2])
