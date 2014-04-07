
class user:
    id=None
    name=None
    lastName=None
    adress=None
    phone=None
    email=None
    password=None
    type= "client" #por defecto 

    def __init__(self,nam,last,addr,pho,emai,passw):    
        self.id #deberia ir a buscar 
        self.name=nam
        self.lastName=last
        self.adress=addr
        self.phone=pho
        self.email=emai
        self.password=passw
         
    
