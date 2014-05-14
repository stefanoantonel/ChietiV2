from django.db import models
from django.contrib.auth.models import User
from decimal import *



class product(models.Model):
	measureUnit = models.CharField(max_length=10)
	pub_date = models.DateTimeField(auto_now=True)
	salePrice=models.DecimalField(max_digits=7, decimal_places=2)
	name=models.CharField(max_length=50)
	canceled=models.CharField(default='false',max_length=5)
	isPromo=models.CharField(default='false',max_length=5)
	def getPrice(self):
		return self.salePrice



class user (models.Model):
	userDj = models.OneToOneField(User) #is a django user. in order to use the password security
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
		it=item.objects.values("productFK").annotate(quantity=models.Sum('quantity'))
		vector=[]
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
		orders=order.objects.all()
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
		ordersNoDelivered=order.objects.filter(orderManagerFK=self,delivered='false')
		ordersNoDelivered.update(delivered='true')
		print 'todo ok Delivered'
		

class order(models.Model):
	userFK=models.ForeignKey(user)
	orderManagerFK=models.ForeignKey(orderManager,related_name='getOrder')
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
	quantity=models.DecimalField(max_digits=7, decimal_places=2)
	orderFK=models.ForeignKey(order)
	def getSubtotal(self):
		return round(self.productFK.salePrice*self.quantity,2)
		pass

class itemPromo(models.Model):
	productFK=models.ForeignKey(product, related_name='product')
	promoFK=models.ForeignKey(product, related_name='items')
	promoQuantity=models.IntegerField()
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

	
