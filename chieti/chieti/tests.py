

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager, user, category, \
	itemPromo


# Create your tests here.
if __name__ == '__main__':
	p=product.objects.get(id=1)
	it=itemPromo(promoFK_id=p,productFK=p,promoQuantity=3)
	#it.save()
	