
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager, user


# Create your tests here.
if __name__ == '__main__':
	
	for u in user.objects.all():
		a=order.objects.filter(userFK=u,delivered="false")
		if not a:
			om=orderManager.objects.get(id=1)
			b=order(userFK=u,orderManagerFK=om)
			b.save()
		