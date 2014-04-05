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
        
        