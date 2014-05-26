from decimal import *

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class category(models.Model):
	number=models.IntegerField()
	description= models.CharField(max_length=10)

class product(models.Model):
	measureUnit = models.CharField(max_length=10)
	pub_date = models.DateTimeField(auto_now=True)
	salePrice=models.DecimalField(max_digits=7, decimal_places=2)
	buyPrice=models.DecimalField(max_digits=7, decimal_places=2)
	name=models.CharField(max_length=50)
	canceled=models.CharField(default='false',max_length=5)
	isPromo=models.CharField(default='false',max_length=5)
	category=models.ForeignKey(category, related_name='category',default=1)
	def getPrice(self):
		return self.salePrice
	def multItemPromo(self,cant):
		itemsMult=[]
		print ("self.items",self.items.all())
		for itPromo in self.items.all():
			c=itPromo.promoQuantity*cant
			p=itPromo.productFK.name
			itemsMult.append({"prod":p,"cant":c})
		return itemsMult



class user (models.Model):
	userDj = models.OneToOneField(User,related_name='getUser') #is a django user. in order to use the password security
	address=models.CharField(max_length=50)
	#adress
	phone=models.CharField(max_length=50)
	activated=models.CharField(default='false',max_length=5)
	

class Employee(models.Model):
	user = models.OneToOneField(User)
	department = models.CharField(max_length=100)
	
	#===========================================================================
	# def __init__(self,nam,last,addr,pho,emai,passw):	
	# 	self.id #deberia ir a buscar 
	# 	self.name=nam
	# 	self.lastName=last
	# 	self.address=addr
	# 	self.phone=pho
	# 	self.email=emai
	# 	self.password=passw
	#===========================================================================
	
class orderManager(models.Model):
	#orders=None #lista de ordenes
	def getSummaryBuy(self):

		#it=item.objects.values("productFK").annotate(quantity=models.Sum('quantity'))
		orderNotDelivered = order.objects.filter(delivered='false')
		it=item.objects.filter(orderFK__in=orderNotDelivered).values("productFK").annotate(quantity=models.Sum('quantity'))
		prod=product.objects.filter(isPromo='true')
		itP=it.filter(productFK=prod)
		
		
		vector=[]
		for a in itP:
			print(product.objects.get(id=a.get("productFK")).name)
			result=product.objects.get(id=a.get("productFK")).multItemPromo(a.get('quantity'))
			print("itemPromo:",result)
			for prodItem in result:
				quant=prodItem.get('cant')
				prod=prodItem.get('prod')
				a={"product":prod,"quantity":quant, "measureUnit":'Unidad'}
				vector.append(a)
		

		for i in it:
			prod=product.objects.get(id=i["productFK"]).name
			quant=i["quantity"]
			mu=product.objects.get(id=i["productFK"]).measureUnit
			a={"product":prod,"quantity":quant, "measureUnit":mu}
			vector.append(a)
		return vector
		pass #JSON array
	
	def printSummary(self,summary):# elemento y cantidad
		pass
	def getSummarySell(self):# elemento y cantidad
		
		#orders=order.objects.filter(orderManagerFK=1)
		#orders=order.objects.all()
		
		#orders=order.objects.filter(getItem=items,delivered='false').distinct() #if item is in order, order is not empty
		orders=order.objects.filter(getItem__isnull=False,delivered='false').distinct()
		#------------
		#i = item.objects.all()
		#orders=order.objects.filter(id__in=i)
		#print ("orders",orders)
		#-------------
		orderManagerArray=[]
		for ords in orders:
			items=item.objects.filter(orderFK=ords)
			productArray=[]
			for it in items:
				prod={'productName':it.productFK.name, 
					'quantity':it.quantity,
					'salePrice':it.productFK.salePrice, 
					'subTotal':it.getSubtotal(),
					'canceled':it.productFK.canceled,}
				productArray.append(prod)
			orde={'userName':ords.userFK.userDj.username,
				'lastName':ords.userFK.userDj.last_name,
				'address':ords.userFK.address,
				'orderNumber':ords.id,
				'products':productArray,
				'totalPrice':ords.getTotal(),}
			orderManagerArray.append(orde)
		return orderManagerArray
		pass
	
	def printOrders(self):
		pass
	def markDelivered(self):
		ordersNoDelivered=order.objects.filter( delivered='false') | order.objects.filter( delivered__isnull=True)
		print ordersNoDelivered.query
		ordersNoDelivered.update(delivered='true')
		print 'todo ok Delivered'
		

class order(models.Model):
	userFK=models.ForeignKey(user)
	orderManagerFK=models.ForeignKey(orderManager,related_name='getOrderManager')
	delivered=models.CharField(default='false',max_length=5)
	#deliver=models.BinaryField(default='false')
	#oro=models.ManyToOneRel(orderManager)
	# items 
	
	def getTotal(self):
		## for each item get subtotal
		it=item.objects.filter(orderFK=self)
		sumTotal=0
		for i in it:
			sumTotal=sumTotal+i.getSubtotal()
		return sumTotal
		pass
		
	def addItem(self,newItem): ## no va mas porque la FK esta del otro lado
		self.items.append(newItem)
		pass
	
	def removeItem(self,itemId): #le paso el objeto item
		item.objects.filter(id=itemId).delete() 
		return "ok delete"
	
	def printOrder(self):
		pass
	
class item(models.Model):
	productFK=models.ForeignKey(product)
	#promoFK=models.ForeignKey(promo)
	quantity=models.DecimalField(max_digits=7, decimal_places=2,validators=[(Decimal('0.01'))])
	orderFK=models.ForeignKey(order,related_name='getItem')
	def getSubtotal(self):
		return round(self.productFK.salePrice*self.quantity,2)
		pass

class itemPromo(models.Model):
	productFK=models.ForeignKey(product, related_name='product')
	promoFK=models.ForeignKey(product, related_name='items')
	promoQuantity=models.DecimalField(max_digits=7, decimal_places=2,validators=[(Decimal('0.01'))])
	def getPromo(self):
		return self.promoFK.primary_key;
	

#===============================================================================
# class promo(product):
#	 #items=None #list
#	 items=[]
#	 discountPercent=models.FloatField()
# 
#	 def addDiscountPercent(self,mount):
#		 self.discountPercent=mount
# 
#	 def addItem(self,item):
#		 self.items.append(item)
#		 
#		 
# class singleProduct(product):
#	 buyPrice=models.FloatField()
#	 def addBuyPrice(self,price):
#		 self.buyPrice=price	 
#	 
#===============================================================================

	
