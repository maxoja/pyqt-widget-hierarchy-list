class HierarchicalModel:
    def __init__(self):
        self.connection = dict()
        self.itemDict = dict()
        self.unmatched = []

    def add(self, id, parentId=None, item=None):
        self.itemDict[id] = item
        self.connection[id] = []

        found = False

        if parentId is not None:
            for k in self.connection:
                if k == parentId :
                    self.connection[k].append(id)
                    found = True
                    break

            if not found:
                self.unmatched.append(id)

        if self.unmatched:
            for i in self.unmatched[::]:
                if id == self.itemDict[i].parentId:
                    self.connection[id].append(i)
                    self.unmatched.remove(i)

    def getTree(self, rootId):
        return self.itemDict[rootId], [self.getTree(i) for i in self.connection[rootId]]

    def getChildrenOf(self, parentId, getIdOnly=False):
        if getIdOnly :
            return self.connection[parentId][::]

        return [self.itemDict[i] for i in self.connection[parentId]]

    def parentOf(self, childId):
        for parent, childList in self.connection.items() :
            if childId in childList :
                return parent

        return None

    def hasParent(self, childId):
        return self.parentOf(childId) is not None

    def removeById(self, id):
        if id not in self.itemDict :
            return

        self.itemDict.pop(id)
        for parent, childList in self.connection.items() :
            if id in childList :
                childList.remove(id)

    def getIds(self):
        return self.itemDict.keys()

    def hasChildren(self, id):
        return self.connection[id]

    def getItemOf(self, id):
        return self.itemDict[id]

    def getNameOf(self, id):
        try: return self.itemDict[id].name
        except: pass

        try: return self.itemDict[id]['name']
        except: pass

        return str(self.itemDict[id])


if __name__ == '__main__' :
    tree = HierarchicalModel()
    tree.add(0, item="root")
    tree.add(1, 0, item="3D models")
    tree.add(2, 1, item="Weapons")
    tree.add(3, 2, item="Guns")
    tree.add(4, 2, item="Melees")
    tree.add(5, 2, item="Bombs")
    tree.add(6, 1, item="Vehicles")
    tree.add(7, 6, item="Boats")
    tree.add(8, 6, item="Bikes")
    tree.add(9, 1, item="Trees")
    tree.add(10, 0, item="Sprite Sheets")
    tree.add(11, 10, item="Characters")
    tree.add(12, 10, item="Effects")

    print(tree.connection)
    print(tree.getTree(0))