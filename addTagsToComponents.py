from controllers.component import getComponents, getComponent, updateComponent
from controllers.tag import addTagToComponent, removeTagFromComponent


def addTagsTextToAllComponents():
    # This will likely never be run again, but it helped to add the tag stubs for all the components
    components = getComponents()
    for c in components:
        desc = str(c["description"])
        if ("Tags:" not in desc):
            desc += "\nTags: "
            print(updateComponent(c["id"], desc, c["name"],
                                  c["status"], c["showcase"], c["group_id"]))


def addTagsTextToSingleComponents(id):
    # This will likely never be run again, but it helped to add the tag stubs for all the components
    c = getComponent(id)
    desc = str(c["description"])
    if ("Tags:" not in desc):
        desc += "\nTags: "
        print(updateComponent(c["id"], desc, c["name"],
                              c["status"], c["showcase"], c["group_id"]))


#print(removeTagFromComponent("mmhsvy7tvvty", "OnPrem"))
#print(addTagToComponent("xc7569m4pr6q", "OnPrem"))

print(getComponent)
