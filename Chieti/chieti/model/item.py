
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
    #===========================================================================