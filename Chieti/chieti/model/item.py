'''
Created on Apr 5, 2014

@author: - Tefo -
'''

class item():
    products=None
    quantity=None
    
    def getSubtotal(self):
        pass
    
    def __init__(self, prod,quant):
        self.products=prod
        self.quantity=quant
        pass
        
        
if __name__ == '__main__':
    from order import order
    o=order(1,3)
    print o.items
    
    