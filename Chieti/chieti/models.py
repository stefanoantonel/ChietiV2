from django.db import models


class product(models.Model):
	#UNIT_CHOICES = (('k','Kg'),('u','Unit'),)
	#measureUnit = models.CharField(max_length=3 ,choices=UNIT_CHOICES,)
	measureUnit = models.CharField(max_length=3)
	pub_date = models.DateTimeField(auto_now=True)
	salePrice=models.DecimalField(max_digits=7, decimal_places=2)
	name=models.CharField(max_length=50)
	def getPrice(self):
		return self.salePrice
	class Meta:
		#abstract = True
		pass


class user (models.Model):
	name=models.CharField(max_length=50)
	lastName=models.CharField(max_length=50)
	adress=models.CharField(max_length=50)
	phone=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	password=models.CharField(max_length=10)
	type= "client" #por defecto 
	
	#===========================================================================
	# def __init__(self,nam,last,addr,pho,emai,passw):	
	# 	self.id #deberia ir a buscar 
	# 	self.name=nam
	# 	self.lastName=last
	# 	self.adress=addr
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
	
	def cancelProduct(self):
		pass
	
	def __printSummary(self,summary):# elemento y cantidad
		pass
	def printOrders(self):
		order.objects.filter
		pass

class order(models.Model):
	userFK=models.ForeignKey(user)
	orderManagerFK=models.ForeignKey(orderManager)
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
		
	def cancelProduct(self,product): #clase product
		pass
	
	def printOrder(self):
		
		pass
	
class item(models.Model):
	productFK=models.ForeignKey(product)
	#promoFK=models.ForeignKey(promo)
	
	quantity=models.IntegerField()
	orderFK=models.ForeignKey(order)
	def getSubtotal(self):
		return self.productFK.salePrice*self.quantity
		pass
	




class promo(product):
	#items=None #list
	items=[]
	discountPercent=models.FloatField()

	def addDiscountPercent(self,mount):
		self.discountPercent=mount

	def addItem(self,item):
		self.items.append(item)
		
		
class singleProduct(product):
	buyPrice=models.FloatField()
	def addBuyPrice(self,price):
		self.buyPrice=price	 
	


	

