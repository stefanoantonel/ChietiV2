from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.template import Context, Template
# Create your tests here.
def index(request):
    
    fp = open('./chieti/templates/chieti/homePage.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context())
    return HttpResponse(html)

def addProd(request):
    fp = open('./chieti/templates/chieti/addProduct.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context())
    return HttpResponse(html)


from django.views.decorators.csrf import csrf_protect

def addProd2(request):
    nam=request.POST.get('name')
    pri=request.POST.get('sellPrice','')
    from chieti.models import product
    pr=product(measureUnit ='kg',salePrice=pri,name=nam)
    
    
    pr.save()
    return HttpResponse(nam)

    
