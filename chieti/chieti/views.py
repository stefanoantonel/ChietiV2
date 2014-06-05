

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.template.base import Template
from django.template.context import Context

from django.template.loader import render_to_string
import json
from _elementtree import tostring

from chieti.models import product, orderManager, order, user, item, category,itemPromo



# Create your tests here.
def home(request):
		
	return render(request, 'chieti/homePage2.html')
def homa(request):
	
	return render(request, 'chieti/homePage.html')
	
	#return HttpResponse(html)
	
def quienes(request):
 	return render(request, 'chieti/quienesSomos.html')
 
def comoComprar(request):
 	return render(request, 'chieti/comoComprar.html')
	
def init(request):
	
	om=orderManager()
	om.save()
	
	# u=user(name="Florencia",lastName="Bon",adress="Libertad 1833",phone="3133312212",email="122@hotmail.com",password="12")
	
	return HttpResponse('Order Manager OK')
def test(request):
	#logout(request)
	#return render(request, 'chieti/homePage2.html')
	#from django.http import HttpResponse 
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
	print "autooooo"
	term=request.GET.get('term')
	prod = product.objects.filter(name__icontains=term)
	print ("prod:",prod)
	productArray=[]
	lista=[]
	for p in prod:
		saleP=str(p.salePrice);
		ppp={"label" : p.name,"name" : p.name, "id" : p.id, "um":p.measureUnit, "saleP" : saleP}
		lista.append(ppp)
	lJson=json.dumps(lista)
	print ("l:",lJson)
	return HttpResponse(lJson)


def compCategory(request):
	print "category"
	term=request.GET.get('term')
	cat = category.objects.filter(description__icontains=term)
	print ("cat:",cat)
	productArray=[]
	lista=[]
	for c in cat:
		#ppp={"id":p.id,"label":p.name,"value":p.salePrice}
		ppp={"label" : c.description, "id" : c.number}
		lista.append(ppp)
	lJson=json.dumps(lista)
	print ("l:",lJson)
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

	
	if not c.isdigit():
		print 'entro no'
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
	cat=request.POST.get("id")
	if(cat==None): 
		todo = product.objects.filter(category=1)
	elif(cat=='4'): 
		todo = product.objects.all()
	else:
		todo = product.objects.filter(category=cat)
	#print todo.query
	#c = Context({'todos':todo})
	return render(request, 'chieti/productsTemplate.html',{'todos':todo})
	

def showSales(request):
	return render(request, 'chieti/sales2.html')
	
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
	ids = request.POST.get('ids')
	quant = request.POST.get('quantity')
	if quant.isdigit():
		print ('quantity:',quant)
		print ('prod:',ids)
		# p=product.object.get(id=ids) 
		# q=quant
		# o=order.objects.filter(id=1)
		
		i = item(productFK=product.objects.get(id=ids),quantity=quant,orderFK=order.objects.get(id=request.session["order"]))
		i.save()
		return HttpResponse('true')
	return HttpResponse('false')

@login_required(login_url='/chieti/singIn/')
def changeOrder(request):
	
	todo = item.objects.filter(orderFK=request.session["order"])
	#c = Context({'todos':todo})
	
	
	return render(request, 'chieti/changeOrder.html',{'todos':todo})
	
	# return HttpResponse(request.session["order"])

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
	itemId = request.POST.get("itemId")
	quant = request.POST.get("quantity")
	print 'idItem',itemId,' quant', quant
	if float(quant):
	#if quant.isdigit():
		item.objects.filter(id=itemId).update(quantity=quant)
		print item.objects.get(id=itemId)
	return redirect(showProduct)

@login_required(login_url='/chieti/singIn/')
def removeItem(request):
	itemId = request.POST.get("itemId")	
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
	productId = request.POST.get('productId')
	checked = request.POST.get('checked')
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
	return HttpResponse('Se le envio un mail para su confirmacion')

def sendMail2(request,email,context):
	print 'conte', context
	subject, from_email, to = 'Cambiar Clave ChietiOnline' , 'chietionline@gmail.com', email
	text_content = 'This is an important message.'
	html_content = render_to_string('chieti/emailPass.html', context) ##mando username y email
	
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	return HttpResponse('Se le envio un mail para cambiar su clave')

def changePass0(request):
	return render(request, 'chieti/changePass1.html')

def changePass1(request):
	mailT2 = request.POST.get('email')
	usernameT2 = request.POST.get('username')
	
	cont={'mail': mailT2, 'name':usernameT2}
	sendMail2(request, mailT2,cont)
	return HttpResponse('Se le envio un mail para su confirmacion')
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
	
	return render(request, 'chieti/singUp.html',{'error':''})
	
	
def singUpFake(request):
	return render(request, 'chieti/singUpFake.html',{'error':''})
	
def singUp2(request):
	pass1 = request.POST.get('password1')
	pass2 = request.POST.get('password2')
	if pass1 == pass2:
		nameT = request.POST.get('name')
		lastNameT = request.POST.get('lastName')
		emailT = request.POST.get('email')
		addressT = request.POST.get('address')
		uExist=User.objects.get(username=nameT)
		print uExist
		if not uExist:
			request.session['userNameTemp']=nameT
			request.session['emailTemp']=emailT
			
			#u1 = User(username=nameT+" "+lastNameT,  email=emailT, password=pass1)
			u1 = User.objects.create_user(username=nameT,  email=emailT, password=pass1)
			u1.last_name=lastNameT
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
	print("ventana singIn",isVentana);
	return render(request, 'chieti/singIn.html',{'error':'','isVentana':isVentana})

def bienvenido(request):
	return render(request, 'chieti/bienvenido.html')


def singIn2(request):
	username = request.POST['username']
	password = request.POST['password']
	isVentana=0;
	isVentana = request.POST.get('isVentana')
	print("isVentana",isVentana);
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
				print 'es 1'
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
	print ('entro')
	prodId = request.POST.get('idProd')
	#paramName=request.POST.get('paramName')
	#paramValue=request.POST.get('paramValue')
	nam=request.POST.get('name')
	buyPric=request.POST.get('buyPrice')
	salePric=request.POST.get('salePrice')
	categor=request.POST.get('category')
	measureUni=request.POST.get('measureUnit')
	delet=request.POST.get('delete')
	cancele=request.POST.get('canceled','false')
	
	print 'product'
	print nam,buyPric,salePric,categor,measureUni,delet,cancele
	if(delet =='true'):
		product.objects.filter(id=prodId).delete()
	product.objects.filter(id=prodId).update(name=nam,buyPrice=buyPric, salePrice=salePric, category=categor, measureUnit=measureUni, canceled =cancele) 
	return HttpResponse("Todo ok Change PRod")


def usernameExist(request):
	param=request.POST.get('name')
	us=User.objects.filter(username=param)
	
	if not us: #no exist
		#image_data = open("chieti/static/chieti/images/fine.png", "rb").read()
		#return HttpResponse(image_data, mimetype="image/png")
		return HttpResponse("Usuario OK")
	return HttpResponse("Usuario MAL")

def changeUserData(request):
	print request.session['user']
	u=user.objects.get(id=request.session['user'])
	return render(request, 'chieti/changeUserData.html',{'us':u})
	pass

def changeUserData2(request):
	ids=request.POST.get('ids')
	#nam=request.POST.get('username')
	addr=request.POST.get('direccion')
	print addr
	user.objects.filter(id=ids).update(address=addr)
	
	pass

def adm(request):
	return render(request, 'chieti/adm.html')
	pass
	
def findProductById(request):
	prodId=request.POST.get('id')
	prod = product.objects.get(id=prodId)
	saleP=str(prod.salePrice);
	p={"name" : prod.name,"um":prod.measureUnit, "saleP" : saleP}
	pJson=json.dumps(p)
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
