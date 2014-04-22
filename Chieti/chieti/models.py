from django.db import models


class product(models.Model):

	#UNIT_CHOICES = (('k','Kg'),('u','Unit'),)
	#measureUnit = models.CharField(max_length=3 ,choices=UNIT_CHOICES,)
	measureUnit = models.CharField(max_length=3)
	pub_date = models.DateTimeField(auto_now=True)
	salePrice=models.DecimalField(max_digits=7, decimal_places=2)
	name=models.CharField(max_length=50)
	canceled=models.BinaryField(default='false')
	def getPrice(self):
		return self.salePrice
	


class user (models.Model):
	name=models.CharField(max_length=50)
	lastName=models.CharField(max_length=50)
	adress=models.CharField(max_length=50)
	phone=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	password=models.CharField(max_length=10)
	type= models.CharField(max_length=10, default='"client"') #por defecto 
	activated=models.BinaryField(default='false')
	
	
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
	
	#===========================================================================
	# def cancelProduct(self,productId,checked):
	# 	orders=order.objects.filter(orderManagerFK=self)
	# 	for oo in orders:
	# 		oo.cancelProduct(productId,checked) 
	# 	pass
	# 
	#===========================================================================
	
	def getSummarySell(self):# elemento y cantidad
		orders=order.objects.filter(orderManagerFK=1)
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
			orde={'userName':ords.userFK.name,
				'orderNumber':ords.id,
				'products':productArray,
				'totalPrice':ords.getTotal(),}
			orderManagerArray.append(orde)
		return orderManagerArray
		pass
	
	

class order(models.Model):
	userFK=models.ForeignKey(user)
	orderManagerFK=models.ForeignKey(orderManager)
	deliver=models.BinaryField(default='false')
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
		#Lo hace el propio item en addToOrder
		pass
	
	def removeItem(self,itemId): #le paso el objeto item
		item.objects.filter(id=itemId).delete() 
		return "ok delete"
		
	#===========================================================================
	# def cancelProduct(self,productId,checked): 
	# 	#le paso el prodId y el estaso (true, false) porque es con ajax
	# 	#y me lo hace cada vez que cambio el checkbox
	# 	product.objects.filter(id=productId).update(canceled=checked)
	# 	pass
	#===========================================================================
	
	
	
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
	


	

