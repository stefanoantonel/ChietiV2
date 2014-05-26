
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager, user, category


# Create your tests here.
if __name__ == '__main__':
	orderNotDelivered = order.objects.filter(delivered='false')
	it=item.objects.filter(orderFK__in=orderNotDelivered).values("productFK").annotate(quantity=models.Sum('quantity'))
	prod=product.objects.filter(isPromo='true')
	itP=it.filter(productFK=prod)
	for i in itP:
		
		itP.productFK.items.all()
		
	