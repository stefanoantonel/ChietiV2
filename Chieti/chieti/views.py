from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.

from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext, loader
from django.template import Context, Template

from chieti.models import product,orderManager,order,user,item
# Create your tests here.
def home(request):
	fp = open('./chieti/templates/chieti/homePage.html')
	t = Template(fp.read())
	fp.close()
	c=Context()
	html = t.render(c)
	
	#om=orderManager()
	#om.save()
	
	#u=user(name="Florencia",lastName="Bon",adress="Libertad 1833",phone="3133312212",email="122@hotmail.com",password="12")
	#u=user(name="Stefano",lastName="Ant",adress="Roma 33",phone="3133312212",email="122@hotmail.com",password="12")
	#u.save()
	
	om=orderManager.objects.get(id=1)
	#u=user.objects.get(name="Stefano")
	u=user.objects.get(name="Florencia")
	#o=order(userFK=u,orderManagerFK=om)
	#o.save()
	
	#request.session["orderManager"] = om.id
	#request.session["user"] = u.id
	
	#o=order.objects.get(userFK=request.session["user"],orderManagerFK=request.session["orderManager"])
	#request.session["order"]=o.id
	
	#oro=model
	return HttpResponse(html)

##todo es de prueba... 
def addProd(request):
	fp = open('./chieti/templates/chieti/addProduct.html')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context())
	return HttpResponse(html)




def addProd2(request):
	nam=request.POST.get('name')
	pri=request.POST.get('sellPrice','')
	meas=request.POST.get('mu','')
	pr=product(measureUnit = meas,salePrice=pri,name=nam)
	pr.save()
	return redirect(addProd)



def showProduct(request):
	fp = open('./chieti/templates/chieti/productsTemplate.html')
	t = Template(fp.read())
	fp.close()
	todo=product.objects.all()
	c=Context({'todos':todo})
	html = t.render(c)
	return HttpResponse(html)
	#return render_to_response(fp,{'todos',todo})

def changePrice(request):
	fp = open('./chieti/templates/chieti/changePrice.html')
	t = Template(fp.read())
	fp.close()
	todo=product.objects.all()
	c=Context({'todos':todo})
	html = t.render(c)
	return HttpResponse(html)

def changePrice2(request):
	#ids=request['ids']
	ids=request.POST.getlist("ids")
	new=request.POST.getlist("newPrice")
	#pri=request.POST.get('product11')
	#pr=product(measureUnit ='kg',salePrice=pri,name=nam)
	#pr.save()
	i=0
	for each in ids:
		product.objects.filter(id=each).update(salePrice=new[i])
		i=i+1
	c=(ids,new)
	return HttpResponse(c)

def addToOrder(request):
	ids=request.POST.get('ids')
	quant=request.POST.get('quantity')
	
	#p=product.object.get(id=ids) 
	#q=quant
	#o=order.objects.filter(id=1)
	
	
	i=item(productFK=product.objects.get(id=ids), 
		quantity=quant,
		orderFK=order.objects.get(id=request.session["order"]) )
	i.save()
	c=(ids,quant)
	return HttpResponse(c)

def changeOrder(request):
	fp = open('./chieti/templates/chieti/changeOrder.html')
	t = Template(fp.read())
	fp.close()
	todo=item.objects.filter(orderFK=request.session["order"])
	c=Context({'todos':todo})
	html = t.render(c)
	return HttpResponse(html)
	#return HttpResponse(request.session["order"])
def changeOrder2(request):
	#ids=request['ids']
	itemId=request.POST.getlist("itemId")
	productId=request.POST.getlist("productId")
	quant=request.POST.getlist("quantity")
	#pri=request.POST.get('product11')
	#pr=product(measureUnit ='kg',salePrice=pri,name=nam)
	#pr.save()
	for i in range(0,len(itemId)):
		item.objects.filter(id=itemId[i]).update(quantity=quant[i])
	
	#c=(itemId,productId)
	#return HttpResponse(c)
	return redirect(showProduct)

def removeItem(request):
	itemId=request.POST.get("itemId")	
	ordId=request.session["order"]
	c=order.objects.get(id=ordId).removeItem(itemId)
	
	
	return HttpResponse(c)

def summaryBuy(request):
	
	#Te da JSON array
	#a={"product":prod,"quantity":quant, "measureUnit":mu}
	fp = open('./chieti/templates/chieti/summaryBuy.html')
	t = Template(fp.read())
	fp.close()
	summary=orderManager.objects.get(id=request.session["orderManager"]).getSummaryBuy()
	c=Context({'todos':summary})
	html = t.render(c)
	return HttpResponse(html)
	
	

def printOrders(request):
	
	fp = open('./chieti/templates/chieti/printOrders.html')
	t = Template(fp.read())
	fp.close()
	#===========================================================================
	# 
	# orders=order.objects.filter(orderManagerFK=1)
	# for ords in orders:
	# 	print ords.userFK.name, " Numero de Orden:",ords.id
	# 	items=item.objects.filter(orderFK=ords)
	# 	for it in items:
	# 		print it.productFK.name, it.quantity, it.productFK.salePrice, it.getSubtotal()
	# 	print ords.getTotal()
	# 
	#===========================================================================
	orders=order.objects.filter(orderManagerFK=1)
	orderManagerArray=[]
	for ords in orders:
		items=item.objects.filter(orderFK=ords)
		productArray=[]
		for it in items:
			prod={'productName':it.productFK.name, 
				'quantity':it.quantity,
				'salePrice':it.productFK.salePrice, 
				'subTotal':it.getSubtotal(),}
			productArray.append(prod)
		orde={'userName':ords.userFK.name,
			'orderNumber':ords.id,
			'products':productArray,
			'totalPrice':ords.getTotal(),}
		orderManagerArray.append(orde)
	pass
	c=Context({'orderManagerArray':orderManagerArray})
	html = t.render(c)
	return HttpResponse(html)


def cancelProduct(request):
	fp = open('./chieti/templates/chieti/cancelProduct.html')
	t = Template(fp.read())
	fp.close()
	products=product.objects.all()
	c=Context({'todos':products})
	html = t.render(c)
	return HttpResponse(html)
	

def cancelProduct2(request):
	productId=request.POST.get('productId')
	checked=request.POST.get('checked')

	product.objects.filter(id=productId).update(canceled=checked)
	return HttpResponse(checked)
	