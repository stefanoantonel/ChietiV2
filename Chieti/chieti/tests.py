
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager


# Create your tests here.
if __name__ == '__main__':
	o2=order.objects.filter(delivered='false')
	it2=item.objects.filter(orderFK=o2)
	it=item.objects.values("productFK").annotate(quantity=models.Sum('quantity'))
	print it.query
	
	print it 