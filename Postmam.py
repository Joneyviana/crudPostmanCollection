import json
import uuid 
from Crud import Crud
from ApiDocs import ApiDocs
class Postman(object):
    def __init__(self,projeto,items):
        self.item = items
        self.info = Info(projeto)

    def reprJSON(self):
        return dict(item=self.item,info=self.info)

class Info(object):
    def __init__(self,projeto):
        self._postman_id = str(uuid.uuid1())
        self.name = projeto
        self.schema = "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    def reprJSON(self):
        return dict(_postman_id=self._postman_id,name=self.name,schema=self.schema)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


#entidades = ["politica","termos","colaborador","denuncia","entrada","viagem","noticia","reembolso"]
#postmam = Postman("ascenty",
#[item for entidade in entidades for item in 
 #Crud("http://154.127.52.231:8181/ascentyapi/api/",entidade,"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbkBnbWFpbC5jb20iLCJjcmVhdGVkIjoxNTczMDU5OTAxMjQ5LCJleHAiOjE1NzM2NjQ3MDF9.em5z7LEFBDvyq3QpESROCnDjr7J76V_Y5JbbnsHlMP7iodZqOg01Q93n0YlO5rDt8rzEDpWlNN_h-AFA7-hAyg").getItems()]
#)
#result = json.dumps(postmam.reprJSON(),cls=ComplexEncoder) 
def mapper_Postman(apiDocs):
    items = [path.getItem() for path in apiDocs.paths]
    return Postman("theGuest",items)

arquivo = open("ApiDocs.txt","r+")
apiDocs = ApiDocs(json.loads(arquivo.read())) 
result = json.dumps(mapper_Postman(apiDocs).reprJSON(),cls=ComplexEncoder)
print(result)