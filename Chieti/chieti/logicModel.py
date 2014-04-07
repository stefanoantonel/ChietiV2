
class item():
    product=None
    quantity=None
    
    def getSubtotal(self):
        return self.product.getPrice()*self.quantity
        pass
    
    def __init__(self, prod,quant):
        self.product=prod
        self.quantity=quant
        
        
    #===========================================================================
    # deberiamos poner todas las clases en un solo lugar, en vez de un archivo para cada una. 
    # pero para mi debemos trabajar sobre el modelo porque no podemos guardar y buscar por cosas tipo 
    # us=user(12,33,11,34,33,1)
    # prod.u=us
    # prod.save()
    # 
    # w=product.objects.filter(u=us) no lo encuentra y tampoco podemos buscar por filter(u.email="..")
    # 
    #===========================================================================

'''
Created on Apr 5, 2014

@author: - Tefo -
'''
from mimetypes import init

class order:
    
    id=None #deberia ir a la BD y buscar y ponerlo aca
    user=None #class
    items=None #list

    def getTotal(self):
        pass
    
    def addItem(self,newItem):
        self.items.append(newItem)
        pass
    
    def removeItem(self,item): #le paso el objeto item
        
        pass
    
    def cancelProduct(self,product): #clase product
        pass
    
    def __print(self):
        pass
    
    def __init__(self,idNumber,userObject):
        self.id #deberia ir a la BD y buscar y ponerlo aca
        self.user #class


'''
Created on Apr 5, 2014

@author: - Tefo -
'''

#orders #lista de ordenes
class orderManager:
    
    orders=None #lista de ordenes 
    
    def getSummaryBuy(self):
        pass #matrix
    
    def cancelProduct(self):
        pass
    
    def __printSummary(self,matrix):# elemento y cantidad 
        pass
    
    def __printOrders(self):
        pass
    

#chieti.settings

if __name__ == '__main__':
#     from MODULE import CLASES
#     >>> import types
#     >>> types.FunctionType
#         <type 'function'>
#     >>> FunctionType                   
#         error
#     >>> from types import FunctionType 
#     >>> FunctionType
#         
    pass

class product():
    id=None
    measureUnit=None #label 
    salePrice=None
    name=None
    def add(self,request):
        print "llego el req"
        pass
    
    def getPrice(self):
        return self.salePrice
        
    def __init__(self,saleP,nam,meas):
        self.measureUnit=meas
        self.salePrice=saleP
        self.name=nam
        
if __name__ == '__main__':
    pass


'''
Created on Apr 5, 2014

@author: - Tefo -
'''

class promo(object):
    items=None #list
    discountPercent=None
    
    def addDiscountPercent(self,mount):
        self.discountPercent=mount
    
    def addItem(self,item):
        self.items.append(item)
        
'''
Created on Apr 5, 2014

@author: - Tefo -
'''
class singleProduct():
    buyPrice=None
    
    
    def addBuyPrice(self,price):
        self.buyPrice=price    


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
         
    
