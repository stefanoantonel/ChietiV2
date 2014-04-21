from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Template, Context
from chieti.models import item,product,order,singleProduct,user,orderManager,promo
from django.db import models
import views
# Create your tests here.

def index(request):
	p = request.GET.get('p')
	# if p is not None:
	#    return HttpResponse(p)
	# else:
	
	from django.template import Context, Template
	
	# html = open("/1.html")
	# return HttpResponse(html)
	
	# fp = open('D:\Programas Facultad\Diego G\workspace\github\ChiettiRepo\Chieti\chieti\templates\chieti\1.html')
	fp = open('./chieti/templates/chieti/1.html')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context())
	return HttpResponse(html)


if __name__ == '__main__':
#===========================================================================
# prod=product(measureUnit="Kg",pub_date=timezone.now(),salePrice=12,name="manzana")
# prod.save()
# prod=product(measureUnit="Kg",pub_date=timezone.now(),salePrice=10,name="peras")
# prod.save()
# prod=product(measureUnit="Kg",pub_date=timezone.now(),salePrice=9,name="zanahoria")
# prod.save()
# prod=product(measureUnit="Kg",pub_date=timezone.now(),salePrice=4,name="zanahoria")
# prod.save()
# iw=user(1,2,3,4,'pepe',2)
# prod.um=iw
# prod.save()
# r=product.objects.filter(um=iw)
# 
# print product.clean(prod)
# 
# u=product.objects.filter(salePrice=4)
# for i in u:
#     print i.name
# u=product.objects.get(id=22)
# print u.name
#===========================================================================
	
	todo = product.objects.all()
	
	om = orderManager()
	# om.save()
	
	us = user(name='federico', lastName='sar', adress='poeta 122', phone='1223344', email='f@g.com', password=123)
	# us.save()
	
	orde = order(userFK=us, orderManagerFK=om)
	# orde.save()
	
	sin = singleProduct(measureUnit='Kg', salePrice=22, name='Zapallito', buyPrice=19)
	# sin.save()
	
	it = item(productFK=sin, quantity=2, orderFK=orde)
	# it.save()
	
	w = item.objects.filter(productFK=singleProduct.objects.all())
	
	#===========================================================================
	# orders=order.objects.filter(orderManagerFK=1)
	# for ords in orders:
	# 	#print ords.userFK.name, " Numero de Orden:",ords.id
	# 	items=item.objects.filter(orderFK=ords)
	# 	for it in items:
	# 		#print it.productFK.name, it.quantity, it.productFK.salePrice, it.getSubtotal()
	# 		pass
	# 	#print ords.getTotal()
	#===========================================================================
	
	
	#===========================================================================
	# orders=order.objects.filter(orderManagerFK=1)
	# orderManagerArray=[]
	# for ords in orders:
	# 	orderArray=[]
	# 	orderArray.append({'userName':ords.userFK.name},)
	# 	orderArray.append({'orderNumber':ords.id})
	# 	items=item.objects.filter(orderFK=ords)
	# 	productArray=[]
	# 	for it in items:
	# 		productArray.append({'productName':it.productFK.name},) 
	# 		productArray.append({'quantity':it.quantity})
	# 		productArray.append({'salePrice':it.productFK.salePrice}) 
	# 		productArray.append({'subTotal':it.getSubtotal()})
	# 	orderArray.append({'products':productArray})
	# 	orderArray.append({'total':ords.getTotal()})
	# 	orderManagerArray.append(orderArray)
	#===========================================================================
	
#===============================================================================
# 	orders=order.objects.filter(orderManagerFK=1)
# 
# 	orderManagerArray=[]
# 	for ords in orders:
# 		
# 		
# 		items=item.objects.filter(orderFK=ords)
# 		
# 		productArray=[]
# 		for it in items:
# 			print it.productFK.name
# 			prod={'productName':it.productFK.name,
# 				'quantity':it.quantity,
# 				'salePrice':it.productFK.salePrice, 
# 				'subTotal':it.getSubtotal(),}
# 			productArray.append(prod)
# 		orde={'userName':ords.userFK.name,
# 			'orderNumber':ords.id,
# 			'products':productArray,
# 			'total':ords.getTotal(),
# 			'products':productArray,}
# 		orderManagerArray.append(orde)	
#===============================================================================

	#===========================================================================
	# from django.core.mail import EmailMultiAlternatives
	# subject, from_email, to = 'Welcome Chieti Online', 'chietionline@gmail.com', 'chietionline@gmail.com'
	# text_content = 'This is an important message.'
	# html_content = ' <p>This is an <strong>important</strong> message. {{user}}</p>'
	# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	# msg.attach_alternative(html_content, "text/html")
	# msg.send()
	# print 'send!'
	#===========================================================================
	#views.sendMail()
	
	
	#===========================================================================
	# from django.core.mail import send_mail
	# a="<input type='text'>"
	# send_mail('Bienvenido a Chieti Online',a , 'chietionline@gmail.com',['chietionline@gmail.com'], fail_silently=False)
	# print 'listo send'
	#===========================================================================

	
	mailT2="chietionline@gmail.com"
	nameT2="Federico"
	
	temp = user.objects.get(email=mailT2, name=nameT2)
	#om=orderManager()
	#om.save()
	om = orderManager.objects.get(id=1)
	orderT1=order(userFK=temp, orderManagerFK=om)
	orderT1.save()
	orderT2=orderT1.id
	print orderT2