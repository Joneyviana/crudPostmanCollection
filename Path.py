from Crud import Item
from Request import Request
from Header import Header
from Url import Url
class Path(object):
    def __init__(self, pathJson,host):
        self.path = pathJson[0]
        self.host = host
        self.method = pathJson[1].items()[0][0]
        self.collect_information(pathJson[1].items()[0][1])

    def getItem(self):
        return Item(Request(None,self.method,
        [Header("Content-Type","Content-Type","application/json","text")],
         Url(self.host,self.path)),self.path)   

    def  collect_information(self, methodJson):
        self.sumary = methodJson["summary"] 
        if(methodJson.has_key("parameters")):
            self.parameters = [Parameter(item) for item in methodJson["parameters"]]

class Parameter(object):
    def __init__(self, parameterJson):
        self.type = parameterJson["in"]
        if(parameterJson.has_key("schema")):
            self.schema = parameterJson["schema"].items()[0][1]        