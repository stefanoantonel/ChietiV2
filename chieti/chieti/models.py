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
	buyPrice=models.DecimalField(default=0,max_digits=7, decimal_places=2)
	name=models.CharField(max_length=50)
	canceled=models.CharField(default='false',max_length=5)
	isPromo=models.CharField(default='false',max_length=5)
	category=models.ForeignKey(category, related_name='category',default=1)
	isDiscontinued=models.IntegerField(default=0)
	imgid = models.FloatField(default=0)
	def getPrice(self):
		return self.salePrice
	def multItemPromo(self,cant):
		itemsMult=[]
		for itPromo in self.items.all():
			c=itPromo.promoQuantity*cant
			p=itPromo.productFK.name
			mu=itPromo.productFK.measureUnit
			id=itPromo.productFK.id
			itemsMult.append({"prod":p,"cant":c,"mu":mu,"id":id})
		return itemsMult



class user (models.Model):
	userDj = models.OneToOneField(User,related_name='getUser') #is a django user. in order to use the password security
	address=models.CharField(max_length=50)
	#adress
	phone=models.CharField(max_length=50)
	#activated=models.CharField(default='false',max_length=5)
	
	
class orderManager(models.Model):
	#orders=None #lista de ordenes
	def getSummaryBuy(self): #imprime todo lo que tienen que comprar.

		#it=item.objects.values("productFK").annotate(quantity=models.Sum('quantity'))
		orderNotDelivered = order.objects.filter(delivered='false',confirm='true')
		it=item.objects.filter(orderFK__in=orderNotDelivered).values("productFK").annotate(quantity=models.Sum('quantity'))
		prod=product.objects.filter(isPromo='true')
		itP=it.filter(productFK__in=prod)
		

		vector=[]
		for i in it:
			prod=product.objects.get(id=i["productFK"]).name
			quant=i["quantity"]
			quant=round(quant,2)
			mu=product.objects.get(id=i["productFK"]).measureUnit
			a={"product":prod,"quantity":quant, "measureUnit":mu,"id":i["productFK"]}
			vector.append(a)
		
		#print(itP[0])	
		for a in itP:
			result=product.objects.get(id=a.get("productFK")).multItemPromo(a.get('quantity'))
			for prodItem in result:
				quant=prodItem.get('cant')
				quant=round(quant,2)
				prod=prodItem.get('prod')
				mu=prodItem.get('mu')
				id=prodItem.get('id')
				a=0
				for element in vector:
					 if element['product'] == prod:
					 	element['quantity']=element['quantity']+quant;
					 	a=1;
				if a==0:	 		
					a={"product":prod,"quantity":quant, "measureUnit":mu,"id":id}
					vector.append(a)
		v=sorted(vector)	
		return v
		pass #JSON array
	
	def printSummary(self,summary):# elemento y cantidad
		pass
	def getSummarySell(self):# ARma todas las ordenes. 
		
		orders=order.objects.filter(getItem__isnull=False,delivered='false',confirm='true').distinct()
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
				'firstName':ords.userFK.userDj.first_name,
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
		ordersNoDelivered.update(delivered='true')

	def reduceStock(self,vector):
		for i in vector:
			s=stock.objects.get(id=i['id'])
			#quant=s.get('quantity',0)
			if s: 
				print ('real',i['quantity'],' stock',s.quantity)

class order(models.Model):
	userFK=models.ForeignKey(user)
	orderManagerFK=models.ForeignKey(orderManager,related_name='getOrderManager')
	delivered=models.CharField(default='false',max_length=5)
	confirm=models.CharField(default='false',max_length=5)
	pub_date = models.DateTimeField(auto_now=True)
	def getTotal(self):

		it=item.objects.filter(orderFK=self)
		sumTotal=0
		for i in it:
			sumTotal=sumTotal+i.getSubtotal()
		return sumTotal
		pass
		
	def removeItem(self,itemId): #le paso el objeto item
		item.objects.filter(id=itemId).delete() 
		return "ok delete"
	
	def printOrder(self):
		pass
	
class item(models.Model):
	productFK=models.ForeignKey(product)
	#promoFK=models.ForeignKey(promo)
	quantity=models.DecimalField(max_digits=7, decimal_places=2,validators=[(Decimal('0.1'))])
	orderFK=models.ForeignKey(order,related_name='getItem')
	def getSubtotal(self):
		return round(self.productFK.salePrice*self.quantity,2)
		pass

class itemPromo(models.Model):
	productFK=models.ForeignKey(product, related_name='product') #que soy 
	promoFK=models.ForeignKey(product, related_name='items') #a quien me asocio
	promoQuantity=models.DecimalField(max_digits=7, decimal_places=2,validators=[(Decimal('0.1'))])
	def getPromo(self):
		return self.promoFK.primary_key;

class stock(models.Model):
	productFK=models.ForeignKey(product, related_name='products')
	quantity=models.DecimalField(max_digits=7, decimal_places=2,validators=[(Decimal('0.1'))] )
	pub_date = models.DateTimeField(auto_now=True)
	