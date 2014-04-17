from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from chieti.models import product
# Create your tests here.

def index(request):
	p = request.GET.get('p')
	#if p is not None:
	#    return HttpResponse(p)
	#else:
	
	from django.template import Context, Template
	
	#html = open("/1.html")
	#return HttpResponse(html)
	
	#fp = open('D:\Programas Facultad\Diego G\workspace\github\ChiettiRepo\Chieti\chieti\templates\chieti\1.html')
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
	
	todo=product.objects.all()
	for i in todo:
		print i.name, i.salePrice, i.measureUnit
	pass
