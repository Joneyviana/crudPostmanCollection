class Auth(object):
    def __init__(self,token):
        self.type = "bearer"
        self.bearer = [Bearer(token)]
    
    def reprJSON(self):
        return dict(type=self.type, beared=self.bearer)

class Bearer(object):
    def __init__(self,token):
        self.key = "token"
        self.value = token
        self.type = "string"
    def reprJSON(self):
        return dict(key=self.key, value=self.value, type=self.type)
  

