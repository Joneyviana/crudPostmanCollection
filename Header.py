class Header(object):
    def __init__(self,key,name,value,tipo):
        self.key = key
        self.name = name
        self.value = value
        self.type = tipo
    
    def reprJSON(self):
        return dict(key=self.key,name=self.name,value=self.value,type=self.type)    
