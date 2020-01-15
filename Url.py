class Url(object):
    def __init__(self,base,prefixo):
        if(base[len(base)-1] == "/"):
            base = base[:len(base)-1]
        self.raw = base + prefixo
        if(prefixo[len(prefixo)-1] == "/"):
            prefixo = prefixo[:len(prefixo)-1]
        if(prefixo[0] == "/"):
            prefixo = prefixo[1:]    
        prefixo = prefixo.replace("{","") 
        prefixo = prefixo.replace("}","")
        prefixo = prefixo.replace("id","15")   
        self.protocol ="http"
        self.host = ["154","127","52","231"]
        self.port = "8181"
        self.path = ["theguestapi",prefixo,""]
    def reprJSON(self):
        return dict(raw=self.raw,protocol=self.protocol,host=self.host,port=self.port,path=self.path)