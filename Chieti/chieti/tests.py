from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models.base import Model

from chieti.models import order, product, item, orderManager


# Create your tests here.
if __name__ == '__main__':
	user1 = authenticate(username='Flor', password='12')
	u2=user1.getUser
	a=order.objects.filter(userFK=u2,delivered="false")
	print 'check',a
	if not a:
		print 'entro'
		om=orderManager.objects.get(id=1)
		b=order(userFK=u2,orderManagerFK=om)
		b.save()
	print 