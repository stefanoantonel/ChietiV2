
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager, user, category


# Create your tests here.
if __name__ == '__main__':
	ords=order.objects.all().distinct()
	item1=item.objects.filter(orderFK__isnull=False)
	print item1
	print
	item2=item.objects.filter(orderFK=ords)
	for i in item2:
		print i
	#print item2
	pass