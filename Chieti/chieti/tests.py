from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader,Template,Context
from chieti.models import *
from django.contrib.auth.models import User
# Create your tests here.

if __name__ == '__main__':
	
	u=User.objects.get(username='Stefano Ant')
	a=user.objects.get(userDj=u)
	print a.userDj.id
	
	