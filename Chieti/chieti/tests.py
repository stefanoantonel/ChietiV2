
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager, user, category


# Create your tests here.
if __name__ == '__main__':
	nam = 'peras1'
	pri = 23
	meas = 'unidad'
	isP = 'false'
	t=''
	if not t:
		t=1
	t=category.objects.get(id=t)
	print t
	pr = product(measureUnit=meas, salePrice=pri, name=nam,isPromo=isP,category=t)
	pr.save()