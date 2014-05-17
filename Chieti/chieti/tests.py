from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models.base import Model

from chieti.models import order


# Create your tests here.
if __name__ == '__main__':
	qs = order.objects.filter(id=1)
	print qs.query
	pass