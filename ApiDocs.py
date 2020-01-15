from Path import Path
from Definition import Definition
class ApiDocs(object):
   def __init__(self,api):
       self.basePath = api["basePath"]
       self.host = api["host"]
       self.paths = [ Path(item,self.host) for item in api["paths"].items()]
       self.definitions = [Definition(item) for item in api["definitions"].items()]