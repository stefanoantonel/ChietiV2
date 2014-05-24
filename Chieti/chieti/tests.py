
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager, user, category


# Create your tests here.
if __name__ == '__main__':
	
	a='pedro'
	cate=category.objects.all()
	print cate
	b={'c':a}
	print b['c']