
class product():
    id=None
    measureUnit=None #label 
    salePrice=None
    name=None
    
    
    def getPrice(self):
        return self.salePrice
        
    def __init__(self,saleP,nam,meas):
        self.measureUnit=meas
        self.salePrice=saleP
        self.name=nam
        
if __name__ == '__main__':
    pass

        