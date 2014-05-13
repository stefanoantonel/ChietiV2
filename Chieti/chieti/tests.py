from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader,Template,Context
from chieti.models import *
from django.contrib.auth.models import User
# Create your tests here.

if __name__ == '__main__':
	print 'start'
	productId = 1
	checked = 'true'
	product.objects.filter(id=productId).update(canceled=checked)
	c=round(1.2345,2)
	print c
	#order.objects.get(id=request.session['order']).cancelProduct(productId, checked)
	