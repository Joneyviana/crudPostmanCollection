import json

class Request(object):
    def __init__(self,auth,method,header,url):
        self.auth = auth
        self.method = method
        self.header = header
        self.url = url

    def reprJSON(self):
        return dict(method=self.method,header=self.header,url=self.url)
