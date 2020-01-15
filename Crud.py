from Auth import Auth
from Header import Header
from Request import Request
from Url import Url
class Item(object):
    def __init__(self,request,name):
        self.request = request
        self.name = name
        
    def reprJSON(self):
        return dict(request=self.request,name=self.name)

class Crud(object):
    def __init__(self,urlBase,name,token):
        self.name = name
        self.token = token
        self.urlBase = urlBase
        self.auth = Auth(self.token)
        self.header = [Header("Content-Type","Content-Type","application/json","text")]

    def getAll(self):
        return Item(Request(self.auth,"GET",self.header, 
            Url(self.urlBase,self.name+"/")),"list " + self.name) 
    
    def search(self):        
       return Item(Request(self.auth,"GET",self.header, 
            Url(self.urlBase,self.name+"/search")),"search " + self.name) 

    def getById(self):
        return Item(Request(self.auth,"GET",self.header, 
        Url(self.urlBase,self.name+"/1")),"get " + self.name)

    def post(self):
        return Item(Request(self.auth,"POST",self.header, 
            Url(self.urlBase,self.name+ "/")),"post " + self.name)    

    def put(self):
        return Item(Request(self.auth,"PUT",self.header, 
            Url(self.urlBase,self.name+"/1")) ,"put " + self.name)  

    def patch(self):
        return Item(Request(self.auth,"PATCH",self.header, 
            Url(self.urlBase,self.name+"/1")),"patch " + self.name) 
    
    def delete(self):
        return Item(Request(self.auth,"DELETE",self.header, 
            Url(self.urlBase,self.name+"/1")),"delete "  + self.name) 
    
    def getItems(self):
        return [self.getAll(),
                self.search(),
                self.getById(),
                self.post(),
                self.put(),
                self.patch(),
                self.delete()]