from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader,Template,Context
from chieti.models import *
from django.contrib.auth.models import User
# Create your tests here.

if __name__ == '__main__':    
    #p=product(measureUnit='kg', salePrice=30, name='Pera5',isPromo=False)
    #print p.id
    #promo=product(measureUnit='Un', salePrice=50, name='Promo',isPromo=True)

    #p.save()
    #promo.save()
    
    promo=product.objects.get(id=1)
    p=product.objects.get(id=2)
    i=itemPromo(productFK=p,promoFK=promo,promoQuantity=5)
    i.save()
    
    print promo.items.all()
    #x=itemPromo.objects.get(promoFK=12)
    #print promo.itemPromo.all()
    #--------------------------------------
    #a = Article.objects.get(id=1)
    #print a.headlines.all()
    
    
    