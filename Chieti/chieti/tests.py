from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader,Template,Context
from chieti.models import *
from django.contrib.auth.models import User
# Create your tests here.

if __name__ == '__main__':
	print 'start'
	todo = product.objects.filter(isPromo='true')
	itemsXPromo=dict()
	for promo in todo:
		itemsXPromo[promo.id]=itemPromo.objects.get(promoFK=promo.id)
		x=itemsXPromo[promo.id]
		print promo.id