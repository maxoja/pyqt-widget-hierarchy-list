class DirectoryModel(list) :

    def __init__(self, id, name="unnamed folder", createdDateTime=None, parentId=None):
        list.__init__()
        self.id = id
        self.name = name
        self.createDateTime = createdDateTime
        self.parentId = parentId

|id         |name       |createdDate    |modifiedDate   |creator        |