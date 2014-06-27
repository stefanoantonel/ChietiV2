from _elementtree import tostring
from decimal import *
import json

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.template.base import Template
from django.template.context import Context
from django.template.loader import render_to_string

from chieti.models import product, orderManager, order, user, item, category, itemPromo

def home(request):
	return render(request, 'chieti/homePage2.html')

def homa(request):
	return render(request, 'chieti/homePage.html')

def quienes(request):
	return render(request, 'chieti/quienesSomos.html')
 
def comoComprar(request):
	return render(request, 'chieti/comoComprar.html')
	
def init(request):
	#om=orderManager()
	#om.save()
	return HttpResponse('Order Manager OK')

def test(request):
	p = request.GET.get('p')
	if p is not None:
		return HttpResponse(p)
	else:
		return HttpResponse("No hay p")

def test1(request):
	fp = open('./chieti/test1.html')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context())
	return HttpResponse(html)

def mainHead(request):
	return render(request, 'chieti/mainHead.html')
	
def auto(request):
	return render(request, 'chieti/autocomplete.html')
	
def complete(request):
	term=request.GET.get('term')
	prod = product.objects.filter(name__icontains=term)
	productArray=[]
	lista=[]
	for p in prod:
		saleP=str(p.salePrice);
		ppp={"label" : p.name,"name" : p.name, "id" : p.id, "um":p.measureUnit, "saleP" : saleP}
		lista.append(ppp)
	lJson=json.dumps(lista)
	return HttpResponse(lJson)

def compCategory(request):
	term=request.GET.get('term')
	cat = category.objects.filter(description__icontains=term)
	productArray=[]
	lista=[]
	for c in cat:
		#ppp={"id":p.id,"label":p.name,"value":p.salePrice}
		ppp={"label" : c.description, "id" : c.number}
		lista.append(ppp)
	lJson=json.dumps(lista)
	
	return HttpResponse(lJson)


# #todo es de prueba... 
@staff_member_required
def addProd(request):
	return render(request, 'chieti/addProduct.html')
	
@staff_member_required
def addProd2(request):
	nam = request.POST.get('name')
	pri = request.POST.get('sellPrice', '')
	buyP=request.POST.get('buyPrice', '')
	meas = request.POST.get('mu', '')
	isP = request.POST.get('promo', '')
	t=request.POST.get('tipoProd', '')
	c=request.POST.get('category','1')
	image=request.POST.get('image')

	
	#--------------
# 	id=1000
# 	destination = open('static/chieti/productImages/'+id+'.png, wb+')
# 	f=request.FILES['file']
# 	for chunk in f.chunks():
# 		destination.write(chunk)
# 	destination.close()
	#---------------
	
	if not c.isdigit():
		c=category.objects.get(description=c).id
		pass
	#items=request.POST.get('items', '')
	#items2=request.POST['itemPromo']
	#print ("i----:",items2)
	cat=category.objects.get(id=c)
	pr = product(measureUnit=meas, salePrice=pri, name=nam,isPromo=isP,category=cat,buyPrice=buyP)
	pr.save()
	
	jsonItemsPromo=request.POST.get('jsonItemPromo')
	j=json.loads(jsonItemsPromo)

	for item in j['itemsPromo']:
		it=itemPromo(promoFK_id=pr.id,productFK_id=item['id'],promoQuantity=item['quant'])
		it.save()
	return redirect(addProd)


#@login_required(login_url='/chieti/singIn/')
def showProduct(request):
	url='chieti/productsTemplate.html'
	a=showProduct2(request,url)
	return HttpResponse(a)

def showProduct2(request,url):
	cat=request.GET.get("id")
	if(cat==None): 
		todo = product.objects.filter(category=1).filter(isPromo="false")
	elif(cat=='4'): 
		todo = product.objects.all().filter(isPromo="false")
	else:
		todo = product.objects.filter(category=cat).filter(isPromo="false")
	#print todo.query
	#c = Context({'todos':todo})
	c={'todos':todo}
	c.update(csrf(request))
	return render(request, url,c)

def showSalesFake(request):
	return render(request, 'chieti/sales2.html')

def showSales(request):
	todasPromos = product.objects.filter(isPromo="true")
	c={'todos':todasPromos,'promo':'productImgSale'}
	c.update(csrf(request))
	return render(request, 'chieti/productsTemplate.html',c)
	#Asi manda a al sales
	#return render(request, 'chieti/sales.html',{'todos':todasPromos})
	#return render(request, 'chieti/productsTemplate.html',{'todos':todasPromos,'promo':'productImgSale'})
	
@staff_member_required
def changePrice(request):
	
	todo = product.objects.all()
	#c = Context({'todos':todo})
	
	return render(request, 'chieti/changePrice.html',{'todos':todo})
	
@staff_member_required
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

@login_required(login_url='/chieti/singIn/')
def addToOrder(request):
	ids = request.GET.get('ids')
	quant = request.GET.get('quantity')
	orderId=request.session.get('order')
	print (ids,quant,orderId)
	return addToOrder2(ids,quant,orderId)
	#if float(quant):
	#	i = item(productFK=product.objects.get(id=ids),quantity=quant,orderFK=order.objects.get(id=orderId))
	#	i.save()
	#	return HttpResponse('true')
	#return HttpResponse('false')


	
@login_required(login_url='/chieti/singIn/')
def changeOrder(request):
	
	todo = item.objects.filter(orderFK=request.session["order"])
	#c = Context({'todos':todo})
	
	
	return render(request, 'chieti/changeOrder.html',{'todos':todo})
	
	# return HttpResponse(request.session["order"])


def confirmOrder(request):
	if(request.GET.get("confirm")):						
		a=order.objects.get(id=request.session["order"])
		a.confirm='true'
		a.save()
	return redirect(showProduct)

@login_required(login_url='/chieti/singIn/')
def changeOrder2(request):
	# ids=request['ids']
	itemId = request.POST.getlist("itemId")
	productId = request.POST.getlist("productId")
	quant = request.POST.getlist("quantity")
	if quant.isdigit():
		# pri=request.POST.get('product11')
		# pr=product(measureUnit ='kg',salePrice=pri,name=nam)
		# pr.save()
		for i in range(0, len(itemId)):
			item.objects.filter(id=itemId[i]).update(quantity=quant[i])
		
		# c=(itemId,productId)
		# return HttpResponse(c)
		return redirect(showProduct)
	return redirect(showProduct) 

@login_required(login_url='/chieti/singIn/')
def changeOrder3(request):
	# ids=request['ids']
	itemId = request.GET.get("itemId")
	quant = request.GET.get("quantity")
	if float(quant):
	#if quant.isdigit():
		item.objects.filter(id=itemId).update(quantity=quant)
	return redirect(showProduct)

@login_required(login_url='/chieti/singIn/')
def removeItem(request):
	itemId = request.GET.get("itemId")	
	ordId = request.session["order"]
	c = order.objects.get(id=ordId).removeItem(itemId)
	return HttpResponse(c)

@staff_member_required
def summaryBuy(request):
	summary = orderManager.objects.get(id=1).getSummaryBuy()
	return render(request, 'chieti/summaryBuy.html',{'todos':summary})

@staff_member_required
def printOrders(request):
	orderMan = orderManager.objects.get(id=1)
	summary = orderMan.getSummarySell()
	return render(request, 'chieti/printOrders.html',{'orderManagerArray':summary})

@staff_member_required
def cancelProduct(request):
	products = product.objects.all()
	return render(request, 'chieti/cancelProduct.html',{'todos':products})
	
def cancelProduct2(request):
	productId = request.GET.get('productId')
	checked = request.GET.get('checked')
	product.objects.filter(id=productId).update(canceled=checked)
	
	return HttpResponse(checked)

def sendMail(request):
	subject, from_email, to = 'Welcome Chieti Online' , 'chietionline@gmail.com', request.session['emailTemp']
	text_content = 'This is an important message.'
	
	# html_content='<a href="localhost:8000/chieti/singUp3/?email='+request.session['emailTemp']+'>Presione aqui para confirmar su registracion</a>'
	
	html_content = render_to_string('chieti/email.html', {'mail': request.session['emailTemp'], 'name':request.session['userNameTemp']})
	
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	return render(request, 'chieti/homePage2.html',{'mnjEmail':'Se le envio un mail para su confirmacion'})

def sendMail2(request,email,context):
	subject, from_email, to = 'Cambiar Clave ChietiOnline' , 'chietionline@gmail.com', email
	text_content = 'This is an important message.'
	html_content = render_to_string('chieti/emailPass.html', context) ##mando username y email
	
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	return HttpResponse('Se le envio un mail para cambiar su clave')

def changePass0(request):
	c={}
	c.update(csrf(request))
	return render(request, 'chieti/changePass1.html',c)

def changePass1(request):
	mailT2 = request.POST.get('email')
	usernameT2 = request.POST.get('username')
	
	cont={'mail': mailT2, 'name':usernameT2}
	sendMail2(request, mailT2,cont)
	return HttpResponse('Revise su email para confirmar, muchas gracias')
	#changePass2(request, mailT2)

def changePass2(request):
	mailT2 = str(request.GET.get('email'))
	usernameT2 = str(request.GET.get('username'))
	
	return render(request, 'chieti/changePass2.html', {'mail':mailT2,'name':usernameT2})
	
def changePass3(request):
	mailT2 = request.POST.get('email')
	usernameT2 = request.POST.get('name')
	
	pass1 = request.POST.get('pass1')
	pass2 = request.POST.get('pass2')
	if pass1==pass2:
		u=User.objects.get(email=mailT2,username=usernameT2)
		u.set_password(pass1)
		u.save()
	return redirect(showProduct)


def singUp(request):
	c={'error':''}
	c.update(csrf(request))
	return render(request, 'chieti/singUp.html',c)
	
	
def singUpFake(request):
	c={'error':''}
	c.update(csrf(request))
	return render(request, 'chieti/singUpFake.html',c)
	
def singUp2(request):
	pass1 = request.POST.get('password1')
	pass2 = request.POST.get('password2')
	if pass1 == pass2:
		nameT = request.POST.get('name')
		lastNameT = request.POST.get('lastName')
		firstNameT = request.POST.get('firstName')
		emailT = request.POST.get('email')
		addressT = request.POST.get('address')
		uExist=User.objects.filter(username=nameT)
		if not uExist:
			request.session['userNameTemp']=nameT
			request.session['emailTemp']=emailT
			
			#u1 = User(username=nameT+" "+lastNameT,  email=emailT, password=pass1)
			u1 = User.objects.create_user(username=nameT,  email=emailT, password=pass1)
			u1.last_name=lastNameT
			u1.first_name=firstNameT
			u1.is_active=0
			u1.save()
			u=user(userDj=u1,address=addressT, phone='',)
			u.save()
			return redirect(sendMail)
		else:
			return render(request, 'chieti/singUp.html',{'error':'Nombre ya en uso'})	
	else:
		return render(request, 'chieti/singUp.html',{'error':'Claves son distintas'})
		

def singUp2Fake(request):
	pass1 = request.POST.get('password1')
	pass2 = request.POST.get('password2')
	if pass1 == pass2:
		nameT = request.POST.get('name')
		lastNameT = request.POST.get('lastName')
		emailT = request.POST.get('email')
		addressT = request.POST.get('address')
		
		u1 = User.objects.create_user(username=nameT,  email=emailT, password=pass1)
		if lastNameT:
			u1.last_name=lastNameT
		u1.is_active=1 # default because don't have email 
		u1.save()
		u=user(userDj=u1,address=addressT, phone='')
		
		#u = user(name=nameT, lastName=lastNameT, adress=addressT, phone='', email=emailT, password=pass1)
		u.save()
		om = orderManager.objects.get(id=1)
		orderT1=order(userFK=u, orderManagerFK=om)
		orderT1.save()

		checkOrderExist(u)
		request.session["order"]= orderT1.id
		
		request.session['user'] = u.id
		request.session['orderManager'] = om.id
		
		
		
		return redirect(showProduct)
	else:
		return render(request, 'chieti/singUpFake.html',{'error':'Claves son distintas'})
		

def singUp3(request):
	
	mailT2 = str(request.GET.get('email'))
	nameT2 = str(request.GET.get('name'))
	
	u=User.objects.get(username=nameT2)
	temp=user.objects.get(userDj=u)
	
	#temp = user.objects.get(userNameDj=nameT2)
	mailT1=temp.userDj.email
	nameT1=temp.userDj.username
	
	if mailT1 == mailT2 and nameT1 == nameT2:
		u.is_active=1
		u.save()
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

@staff_member_required
def changeUser(request):
	todo = user.objects.all()
	return render(request, 'chieti/changeUser.html',{'todos':todo})
	
@staff_member_required
def changeUser2(request):
	personId = request.POST.get('idPer')
	us=user.objects.get(id=personId)
	
	checkOrderExist(us)
	request.session["order"]= order.objects.get(userFK=us.id,delivered='false').id
	request.session['user'] = us.id
	return redirect(showProduct)
	# return render_to_response(fp,{'todos',todo})

def singIn(request):
	isVentana = request.GET.get('ventana')
	c = {'error':'','isVentana':isVentana}
	c.update(csrf(request))
	return render(request, 'chieti/singIn.html',c)

def bienvenido(request):
	return render(request, 'chieti/bienvenido.html')

def singIn2(request):
	username = request.POST['username']
	password = request.POST['password']
	isVentana=0;
	isVentana = request.POST.get('isVentana')
	user1 = authenticate(username=username, password=password)
	if user1 is not None: #if exist
		if user1.is_active: 
			userParent=user1.getUser #not django user
			checkOrderExist(userParent)
			login(request, user1)
			userParentId=userParent.id
			request.session["order"]= order.objects.get(userFK=userParentId,delivered='false').id
			request.session['user'] = userParentId

			if(isVentana=="1"):
				return redirect(bienvenido)
			return redirect(showProduct)

			# Redirect to a success page.
		else:
			# Return a 'disabled account' error message
			return render(request, 'chieti/singIn.html',{'error':'No activado. Revise su email'})
	else:
		# Return an 'invalid login' error message
		return render(request, 'chieti/singIn.html',{'error':'Usuario o clave incorrecta'})
		

@staff_member_required
def markDelivered(request):
#	om=request.session["orderManager"]
	om=orderManager.objects.get(id=1)
	om.markDelivered()
	product.objects.filter().update(canceled='false')
	return redirect(showProduct)
	pass

def checkOrderExist(us):
	a=order.objects.filter(userFK=us,delivered="false")
	if not a:
		om=orderManager.objects.get(id=1)
		b=order(userFK=us,orderManagerFK=om)
		b.save()

@staff_member_required
def changeProduct(request):
	todos = product.objects.all() 
	cate=category.objects.all() 
	return render(request, 'chieti/changeProduct.html',{'todos':todos,'categ':cate})

@staff_member_required
def changeProduct2(request):
	prodId = request.GET.get('idProd')
	#paramName=request.POST.get('paramName')
	#paramValue=request.POST.get('paramValue')
	nam=request.GET.get('name')
	buyPric=request.GET.get('buyPrice')
	salePric=request.GET.get('salePrice')
	categor=request.GET.get('category')
	measureUni=request.GET.get('measureUnit')
	delet=request.GET.get('delete')
	delet = int('true' == delet)
	print (delet)
	cancele=request.GET.get('canceled','false')

	product.objects.filter(id=prodId).update(name=nam,buyPrice=buyPric, salePrice=salePric, category=categor, measureUnit=measureUni, canceled =cancele,isDiscontinued=delet) 
	return HttpResponse("Todo ok Change PRod")

def usernameExist(request):
	param=request.POST.get('name')
	us=User.objects.filter(username=param)
	
	if not us: #no exist
		#image_data = open("chieti/static/chieti/images/fine.png", "rb").read()
		#return HttpResponse(image_data, mimetype="image/png")
		print ('no esta')
		return HttpResponse()
	print('si esta')
	return HttpResponse("MAL")

@login_required(login_url='/chieti/singIn/')
def changeUserData(request):
	idU=request.session.get('user')
	u=user.objects.get(id=idU)
	
	return render(request, 'chieti/changeUserData.html',{'us':u})
	pass

def changeUserData2(request):
	ids=request.POST.get('ids')
	#nam=request.POST.get('username')
	print ids
	addr=request.POST.get('direccion')
	first=request.POST.get('firstName')
	last=request.POST.get('lastName')
	u=User.objects.filter(id=ids).update(first_name=first,last_name=last)
	user.objects.filter(userDj_id=ids).update(address=addr)
	#user.objects.filter(id=ids).update(address=addr)
	#u.update(userDj.first_name=first,userDj.last_name=last)
	return render(request, 'chieti/homePage2.html')
	pass

def adm(request):
	return render(request, 'chieti/adm.html')
	pass
	
def findProductById(request):
	prodId=request.GET.get('id')
	prod = product.objects.get(id=prodId)
	saleP=str(prod.salePrice);
	p={"name" : prod.name,"um":prod.measureUnit, "saleP" : saleP}
	#---------------------------
	# items=[]
	# for i in prod.items.all():
	# 	item={"prod":i.productFK.name,"quantity":str(i.promoQuantity),"mu":i.productFK.measureUnit}
	# 	items.append(item)
	# rta={"prod":p,"items":items}
	#---------------------
	pJson=json.dumps(p)
	#pJson=json.dumps(rta)
	return HttpResponse(pJson)

@staff_member_required
def printPrice(request):
	p=product.objects.all()
	return render(request, 'chieti/printPrice.html',{'todos':p})

def logOut(request):
	logout(request)
	return render(request, 'chieti/homePage2.html')

def singInPop(request):
	return render(request, 'chieti/singInPop.html')

def deleteOldUser(request):
	u=user.objects.filter(userDj__is_active=0).delete()
	#print ('user',u)
	udj=User.objects.filter(is_active=0).delete()
	print (udj)
	return render(request, 'chieti/homePage2.html')

def getProducts(request):
	url='chieti/getProducts.html'
	a=showProduct2(request,url)
	return HttpResponse(a)

def getTotalPriceOrder(request):
	o1=request.session['order']
	o2=order.objects.get(id=o1)
	total=o2.getTotal()
	return HttpResponse(total)

def changePromo(request):
	combos = product.objects.filter(isPromo="true")
	todos = product.objects.all()
	c={'todos':todos,'combos':combos}
	c.update(csrf(request))
	return render(request, 'chieti/changePromo.html',c)

def changePromo2(request):
	pr=request.GET.get("id")
	prodInCombo = itemPromo.objects.filter(promoFK=pr)
	lista=[]
	for p in prodInCombo:
		d1={'id':p.productFK.id,'name':p.productFK.name,'quantity':str(p.promoQuantity),'mu':p.productFK.measureUnit}
		lista.append(d1)
	js=json.dumps(lista)
	return HttpResponse(js)

def changePromo3(request):
	pr=request.POST.get("array")
	jsonArray=json.loads(pr)
	print(jsonArray["promo"])
	#print (jsonArray["items"])
	promoId= jsonArray["promo"]
	itemPromo.objects.filter(promoFK_id=promoId).delete()
	for item in jsonArray["items"]:
		it=itemPromo(promoFK_id=promoId,productFK_id=item["id"],promoQuantity=item["quant"])
		it.save()
	return HttpResponse(promoId)

@login_required(login_url='/chieti/singIn/')
def myList(request):
	c={}
	c.update(csrf(request))	
	return render(request, 'chieti/myList.html',c)

def myList2(request):
	array=request.POST.get("array")
	jsonArray=json.loads(array)
	print (jsonArray)
	for prod in jsonArray:

		ids=prod['id']
		quantity=prod['quant']
		orderId=request.session["order"]
		print (ids,quantity,orderId)
		#,{ids=prod['id'],quantity=prod['quant']}
		#redirect(addToOrder,{ "ids":ids ,"quantity":quantity} )
		addToOrder2(ids,quantity,orderId)
	return redirect(showProduct)

def addToOrder2(ids,quant,orderId):
	if float(quant):
		i = item(productFK=product.objects.get(id=ids),quantity=quant,orderFK=order.objects.get(id=orderId))
		i.save()
		return HttpResponse('true')
	return HttpResponse('false')
