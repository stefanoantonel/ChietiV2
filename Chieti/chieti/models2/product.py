'''
Created on Apr 8, 2014

@author: - Tefo -

'''

from django.db import models
class product(models.Model):
	measureUnit = models.CharField(max_length=22)
	#pub_date = models.DateTimeField('date published')
	salePrice=models.DecimalField(max_digits=7, decimal_places=2)
	name=models.CharField(max_length=50)
	def getp(self):
		return self.salePrice*4
	class Meta:
		app_label = 'models'
#===============================================================================
#     class Poll(models.Model):
#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
# 
#     class Choice(models.Model):
#     poll = models.ForeignKey(Poll)
#     choice = models.CharField(max_length=200)
#     votes = models.IntegerField()
#===============================================================================

#===============================================================================
# class products():
#     id=None
#     measureUnit=None #label 
#     salePrice=None
#     name=None
#     def add(self,request):
#         print "llego el req"
#         pass
#     
#     def getPrice(self):
#         return self.salePrice
#         
#     def __init__(self,saleP,nam,meas):
#         self.measureUnit=meas
#         self.salePrice=saleP
#         self.name=nam
#         
# if __name__ == '__main__':
#     pass
#===============================================================================
