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


from chieti.models import product, orderManager, order, user, Document
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


# Create your tests here.
def home(request):
    fp = open('./chieti/templates/chieti/homePage.html')
    t = Template(fp.read())
    fp.close()
    c=Context()
    html = t.render(c)
    #om=orderManager()
    #om.save()
    #u=user(name="Stefano",lastName="An",adress="Roma 133",phone="3133312212",email="122@hotmail.com",password="12")
    #u.save()
    #om=orderManager.objects.get(id=1)
    #u=user.objects.get(id=2)
    #o=order(userFK=u,orderManagerFK=om)
    #o.save()
    #oro=model
    return HttpResponse(html)

##todo es de prueba... 
def addProd(request):
    fp = open('./chieti/templates/chieti/addProduct.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context())
    return HttpResponse(html)

def mainHead(request):
    fp = open('./chieti/templates/chieti/mainHead.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context())
    return HttpResponse(html)




def addProd2(request):
    nam=request.POST.get('name')
    pri=request.POST.get('sellPrice','')
    im= request.FILES['image'] 
    pr=product(measureUnit ='kg',salePrice=pri,name=nam)
    pr.save()
    ids=pr.id
    path = default_storage.save('./chieti/static/chieti/productImages/'+ str(ids)+ '.jpg', ContentFile(im.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    path2='/static/chieti/productImages/'+ str(ids)+ '.jpg'
    return HttpResponse('<html><img src='+path2+'></html>')



def showProduct(request):
    fp = open('./chieti/templates/chieti/productsTemplate.html')
    t = Template(fp.read())
    fp.close()
    todo=product.objects.all()
    c=Context({'todos':todo})
    html = t.render(c)
    return HttpResponse(html)
    #return render_to_response(fp,{'todos',todo})

def showSales(request):
    fp = open('./chieti/templates/chieti/sales.html')
    t = Template(fp.read())
    fp.close()
    todo=product.objects.all()
    c=Context({'todos':todo})
    html = t.render(c)
    return HttpResponse(html)


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
    
    
    #i=item(productFK=product.object.get(id=ids), 
    #       quantity=quant,
    #       orderFK=order.objects.filter(id=1))
    c=(ids,quant)
    return HttpResponse(c)


def singUp(request):
    ids=request.POST.get('ids')
    quant=request.POST.get('quantity')
    c=(ids,quant)
    return HttpResponse(c)


def sales(request):
    fp = open('./chieti/templates/chieti/sales.html')
    t = Template(fp.read())
    fp.close()
    c=Context()
    html = t.render(c)
    return HttpResponse(html)