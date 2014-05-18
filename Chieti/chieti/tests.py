from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models.base import Model

from chieti.models import order, product, item, orderManager


# Create your tests here.
if __name__ == '__main__':
	product.objects.filter().update(canceled='false')
	print 