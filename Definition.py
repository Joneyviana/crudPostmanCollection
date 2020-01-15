class Definition(object):
    def __init__(self,definitionJson):
        self.name = definitionJson[0]
        self.type = definitionJson[1]["type"]
        self.properties = [Property(item) for item in definitionJson[1]["properties"].items()]

class Property(object):
    def __init__(self,propertyJson):
        self.type = propertyJson[1].items()[0][1]
        