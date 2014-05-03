from django.contrib.messages.storage import default_storage
from django.core.files.base import ContentFile
from django.http import request, HttpResponse
from django.http import request, HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.template import RequestContext, loader
from django.test import TestCase
from django.views.decorators.csrf import csrf_protect


from chieti.models import product, orderManager, order, user, itemPromo
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string
from django.template import RequestContext, loader
from django.template import Context, Template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from chieti.models import product, orderManager, order, user, item
# Create your tests here.
def home(request):
	fp = open('./chieti/templates/chieti/homePage.html')
	t = Template(fp.read())
	fp.close()
	c = Context()
	html = t.render(c)
	#===========================================================================
	# 
	# om=orderManager()
	# #om.save()
	# 
	# # u=user(name="Florencia",lastName="Bon",adress="Libertad 1833",phone="3133312212",email="122@hotmail.com",password="12")
	# u1=User(username="Stefano Ant",email="122@hotmail.com",password="12")
	# u1.save()
	# u=user(userDj=u1,address="Roma 33",phone="3133312212")
	# u.save()
	# 
	# 
	# 
	# #print a.userDj.id
	# 
	# om = orderManager.objects.get(id=1)
	# a=User.objects.get(username='Stefano Ant')
	# u=user.objects.get(userDj=a)
	# 
	# 
	# 
	# #===========================================================================
	# # if not order.objects.filter(userFK=request.session['user']):
	# o=order(userFK=u,orderManagerFK=om)
	# o.save()
	# #===========================================================================
	# request.session['user']=u.id
	# u = user.objects.get(id=request.session['user'])
	# 
	# 
	# o=order.objects.get(userFK=request.session["user"],orderManagerFK=1)
	# request.session["order"]=o.id
	# 
	# # oro=model
	#===========================================================================
	return HttpResponse(html)
	
def init(request):
	
	om=orderManager()
	om.save()
	
	# u=user(name="Florencia",lastName="Bon",adress="Libertad 1833",phone="3133312212",email="122@hotmail.com",password="12")
	
	return HttpResponse('Order Manager OK')
def test(request):
	return HttpResponse(request.session["order"])
	

def mainHead(request):
	fp = open('./chieti/templates/chieti/mainHead.html')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context())
	return HttpResponse(html)

def auto(request):
	fp = open('./chieti/templates/chieti/autocomplete.html')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context())
	return HttpResponse(html)

# #todo es de prueba... 
def addProd(request):

	fp = open('./chieti/templates/chieti/addProduct.html')
	t = Template(fp.read())
	fp.close()
	prod = product.objects.all()
	print "prod"
	print prod
	c = Context({'todosLosProd':prod})
	html = t.render(Context())
	return HttpResponse(html)

def addProd2(request):
	nam = request.POST.get('name')
	pri = request.POST.get('sellPrice', '')
	meas = request.POST.get('mu', '')
	isP = request.POST.get('promo', '')
	pr = product(measureUnit=meas, salePrice=pri, name=nam,isPromo=isP)
	pr.save()
	im= request.FILES['image'] 
	ids=pr.id
	path = default_storage.save('./chieti/static/chieti/productImages/'+ str(ids)+ '.jpg', ContentFile(im.read()))
	tmp_file = os.path.join(settings.MEDIA_ROOT, path)
	return redirect(addProd)


def showProduct(request):
	fp = open('./chieti/templates/chieti/productsTemplate.html')
	t = Template(fp.read())
	fp.close()
	todo = product.objects.all()
	c = Context({'todos':todo})
	html = t.render(c)
	return HttpResponse(html)
	# return render_to_response(fp,{'todos',todo})

def showSales(request):
	fp = open('./chieti/templates/chieti/sales.html')
	t = Template(fp.read())
	fp.close()
	todo = product.objects.filter(isPromo='true')
	itemsXPromo=dict()
	for promo in todo:
		itemsXPromo[promo.id]=itemPromo.objects.get(promoFK=promo.id)
		x=itemsXPromo[promo.id]
		print promo.id
	c = Context({'todasPromos':todo,'items':itemsXPromo})
	html = t.render(c)
	return HttpResponse(html)


def changePrice(request):
	fp = open('./chieti/templates/chieti/changePrice.html')
	t = Template(fp.read())
	fp.close()
	todo = product.objects.all()
	c = Context({'todos':todo})
	html = t.render(c)
	return HttpResponse(html)

def changePrice2(request):
	# ids=request['ids']
	ids = request.POST.getlist("ids")
	new = request.POST.getlist("newPrice")
	# pri=request.POST.get('product11')
	# pr=product(measureUnit ='kg',salePrice=pri,name=nam)
	# pr.save()
	i = 0
	for each in ids:
		product.objects.filter(id=each).update(salePrice=new[i])
		i = i + 1
	c = (ids, new)
	return HttpResponse(c)

def addToOrder(request):
	ids = request.POST.get('ids')
	quant = request.POST.get('quantity')
	
	# p=product.object.get(id=ids) 
	# q=quant
	# o=order.objects.filter(id=1)
	
	i = item(productFK=product.objects.get(id=ids),
		quantity=quant,
		orderFK=order.objects.get(id=request.session["order"]))
	i.save()
	c = (ids, quant)
	return HttpResponse(c)

def changeOrder(request):
	fp = open('./chieti/templates/chieti/changeOrder.html')
	t = Template(fp.read())
	fp.close()
	todo = item.objects.filter(orderFK=request.session["order"])
	c = Context({'todos':todo})
	html = t.render(c)
	return HttpResponse(html)
	# return HttpResponse(request.session["order"])
def changeOrder2(request):
	# ids=request['ids']
	itemId = request.POST.getlist("itemId")
	productId = request.POST.getlist("productId")
	quant = request.POST.getlist("quantity")
	# pri=request.POST.get('product11')
	# pr=product(measureUnit ='kg',salePrice=pri,name=nam)
	# pr.save()
	for i in range(0, len(itemId)):
		item.objects.filter(id=itemId[i]).update(quantity=quant[i])
	
	# c=(itemId,productId)
	# return HttpResponse(c)
	return redirect(showProduct)

def removeItem(request):
	itemId = request.POST.get("itemId")	
	ordId = request.session["order"]
	c = order.objects.get(id=ordId).removeItem(itemId)
	
	
	return HttpResponse(c)

def summaryBuy(request):
	
	# Te da JSON array
	# a={"product":prod,"quantity":quant, "measureUnit":mu}
	fp = open('./chieti/templates/chieti/summaryBuy.html')
	t = Template(fp.read())
	fp.close()
	#summary = orderManager.objects.get(id=request.session["orderManager"]).getSummaryBuy()
	summary = orderManager.objects.get(id=1).getSummaryBuy()
	c = Context({'todos':summary})
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
	
	#===========================================================================
	# orders=order.objects.filter(orderManagerFK=1)
	# orderManagerArray=[]
	# for ords in orders:
	# 	items=item.objects.filter(orderFK=ords)
	# 	productArray=[]
	# 	for it in items:
	# 		prod={'productName':it.productFK.name, 
	# 			'quantity':it.quantity,
	# 			'salePrice':it.productFK.salePrice, 
	# 			'subTotal':it.getSubtotal(),
	# 			'canceled':it.productFK.canceled,}
	# 		productArray.append(prod)
	# 	orde={'userName':ords.userFK.name,
	# 		'orderNumber':ords.id,
	# 		'products':productArray,
	# 		'totalPrice':ords.getTotal(),}
	# 	orderManagerArray.append(orde)
	# pass
	#===========================================================================
	
	orderMan = orderManager.objects.get(id=1)
	
	summary = orderMan.getSummarySell()
	
	c = Context({'orderManagerArray':summary})
	html = t.render(c)
	return HttpResponse(html)


def cancelProduct(request):
	fp = open('./chieti/templates/chieti/cancelProduct.html')
	t = Template(fp.read())
	fp.close()
	products = product.objects.all()
	c = Context({'todos':products})
	html = t.render(c)
	return HttpResponse(html)
	

def cancelProduct2(request):
	productId = request.POST.get('productId')
	checked = request.POST.get('checked')
	product.objects.filter(id=productId).update(canceled=checked)
	
	return HttpResponse(checked)

def sendMail(request):
	
	
	#===========================================================================
	# name=request.POST.get('name')
	# lastName=request.POST.get('lastName')
	# email=request.POST.get('email')
	# address=request.POST.get('address')
	#===========================================================================
	
	
	subject, from_email, to = 'Welcome Chieti Online' , 'chietionline@gmail.com', request.session['emailTemp']
	text_content = 'This is an important message.'
	
	# html_content='<a href="localhost:8000/chieti/singUp3/?email='+request.session['emailTemp']+'>Presione aqui para confirmar su registracion</a>'
	
	html_content = render_to_string('chieti/email.html', {'mail': request.session['emailTemp'], 'name':request.session['userNameTemp']})
	#===========================================================================
	# html_content =html_content + ' <p>This is an <strong>important</strong> message.'
	# html_content=html_content + str(name)
	# html_content=html_content +'</p>'
	#===========================================================================
	
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	return HttpResponse('Se le envio un mail para su confirmacion')

def singUp(request):
	fp = open('./chieti/templates/chieti/singUp.html')
	t = Template(fp.read())
	fp.close()
	
	c = Context({'error':''})
	html = t.render(c)
	return HttpResponse(html)
	
def singUpFake(request):
	fp = open('./chieti/templates/chieti/singUpFake.html')
	t = Template(fp.read())
	fp.close()
	
	c = Context({'error':''})
	html = t.render(c)
	return HttpResponse(html)

def singUp2(request):
	pass1 = request.POST.get('password1')
	pass2 = request.POST.get('password2')
	if pass1 == pass2:
		nameT = request.POST.get('name')
		lastNameT = request.POST.get('lastName')
		emailT = request.POST.get('email')
		addressT = request.POST.get('address')
		
		request.session['userNameTemp']=nameT+" "+lastNameT
		request.session['emailTemp']=emailT
		
		u1 = User(username=nameT+" "+lastNameT,  email=emailT, password=pass1)
		u1.save()
		u=user(userDj=u1,address=addressT, phone='',)
		u.save()
		
		return redirect(sendMail)
	else:
		fp = open('./chieti/templates/chieti/singUp.html')
		t = Template(fp.read())
		fp.close()
		
		c = Context({'error':'Claves son distintas'})
		html = t.render(c)
		return HttpResponse(html)

def singUp2Fake(request):
	pass1 = request.POST.get('password1')
	pass2 = request.POST.get('password2')
	if pass1 == pass2:
		nameT = request.POST.get('name')
		lastNameT = request.POST.get('lastName')
		emailT = request.POST.get('email')
		addressT = request.POST.get('address')
		
		
		u1 = User(username=nameT+" "+lastNameT,  email=emailT, password=pass1)
		u1.save()
		u=user(userDj=u1,address=addressT, phone='',)
		
		#u = user(name=nameT, lastName=lastNameT, adress=addressT, phone='', email=emailT, password=pass1)
		u.save()
		om = orderManager.objects.get(id=1)
		orderT1=order(userFK=u, orderManagerFK=om)
		orderT1.save()
		
		request.session["order"]= orderT1.id
		
		request.session['user'] = u.id
		request.session['orderManager'] = om.id
		
		
		
		return redirect(showProduct)
	else:
		fp = open('./chieti/templates/chieti/singUpFake.html')
		t = Template(fp.read())
		fp.close()
		
		c = Context({'error':'Claves son distintas'})
		html = t.render(c)
		return HttpResponse(html)


def singUp3(request):
	
	mailT2 = str(request.GET.get('email'))
	nameT2 = str(request.GET.get('name'))
	
	
	
	
	u=User.objects.get(username=nameT2)
	temp=user.objects.get(userDj=u)
	
	#temp = user.objects.get(userNameDj=nameT2)
	mailT1=temp.userDj.email
	nameT1=temp.userDj.username
	
	if mailT1 == mailT2 and nameT1 == nameT2:
		#=======================================================================
		# nameT = request.session['userNameTemp']
		# lastNameT = request.session['lastNameTemp']
		# emailT = request.session['emailTemp']
		# addressT = request.session['addressTemp']
		# passwordT = request.session['password']
		# 
		# u = user(name=nameT, lastName=lastNameT, adress=addressT, phone='', email=emailT, password=passwordT)
		# u.save()
		#=======================================================================
		
		
		user.objects.filter(id=temp.id).update(activated='true')
		#om=orderManager()
		#om.save()
		om = orderManager.objects.get(id=1)
		orderT1=order(userFK=temp, orderManagerFK=om)
		orderT1.save()
		
		orderT2=orderT1.id
		request.session["order"]= orderT2
		request.session['user'] = temp.id
		request.session['orderManager'] = om.id
		
		return redirect(home)
	else:
		return HttpResponse("Error de confirmacion")

def changeUser(request):
	fp = open('./chieti/templates/chieti/changeUser.html')
	t = Template(fp.read())
	fp.close()
	todo = user.objects.all()
	todo
	c = Context({'todos':todo})
	html = t.render(c)
	return HttpResponse(html)
	# return render_to_response(fp,{'todos',todo})


def changeUser2(request):
	personId = request.POST.get('idPer')
	us=user.objects.get(id=personId)
	request.session["order"]= order.objects.get(userFK=us.id).id
	request.session['user'] = us.id
	return redirect(showProduct)
	# return render_to_response(fp,{'todos',todo})
