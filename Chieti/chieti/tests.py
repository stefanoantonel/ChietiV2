from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Template, Context
from chieti.models import item,product,order,singleProduct,user,orderManager,promo
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
	for i in todo:
		print i.name, i.salePrice, i.measureUnit
	
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
	
	for i in w:
		print i.quantity, i.productFK.salePrice, i.productFK.name, i.productFK.measureUnit, i.orderFK.orderManagerFK.id, i.orderFK.userFK.type
	pass
	
	i=item(productFK=product.objects.get(id=1), 
		quantity=4,
		orderFK=order.objects.get(id=1))
	i.save()
		
	t = Template("My name is {{ my_name }}.")
	c = Context({"my_name": "Adrian"})
	t.render(c)
