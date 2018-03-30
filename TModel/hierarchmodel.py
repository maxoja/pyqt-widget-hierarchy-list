class HierarchicalModel:
    def __init__(self):
        self.connection = dict()
        self.itemDict = dict()
        self.unmatched = []

    def add(self, id, parentId=None, **item):
        assert( 'name' in item )
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

    def getTree(self, rootId, getIdOnly=False):
        if getIdOnly:
            return rootId, [self.getTree(i, getIdOnly) for i in self.connection[rootId]]

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
        if id not in self.itemDict:
            return

        self.itemDict.pop(id)
        for parent, childList in self.connection.items():
            if id in childList :
                childList.remove(id)

        children = self.connection[id][::]
        self.connection.pop(id)

        for childId in children:
            self.removeById(childId)


    def getIds(self):
        return self.itemDict.keys()

    def hasChildren(self, id):
        return self.connection[id]

    def getItemOf(self, id):
        return self.itemDict[id]

    def getNameOf(self, id):
        return self.itemDict[id]['name']


if __name__ == '__main__' :
    tree = HierarchicalModel()
    tree.add(0, name="root")
    tree.add(1, 0, name="3D models")
    tree.add(2, 1, name="Weapons")
    tree.add(3, 2, name="Guns")
    tree.add(4, 2, name="Melees")
    tree.add(5, 2, name="Bombs")
    tree.add(6, 1, name="Vehicles")
    tree.add(7, 6, name="Boats")
    tree.add(8, 6, name="Bikes")
    tree.add(9, 1, name="Trees")
    tree.add(10, 0, name="Sprite Sheets")
    tree.add(11, 10, name="Characters")
    tree.add(12, 10, name="Effects")

    print('V connection V')
    print(tree.connection,'\n')

    print('V tree at folder root V')
    print(tree.getTree(0, getIdOnly=True),'\n')

    print('V tree at folder Weapons V')
    print(tree.getTree(2),'\n')

    # print('V tree at root removed 3D models V')
    tree.removeById(1)
    print(tree.getTree(0, getIdOnly=True))
    print(tree.connection)