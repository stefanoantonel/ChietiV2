
class item():
    product=None
    quantity=None
    
    def getSubtotal(self):
        return self.product.getPrice()*self.quantity
        pass
    
    def __init__(self, prod,quant):
        self.product=prod
        self.quantity=quant
        
    