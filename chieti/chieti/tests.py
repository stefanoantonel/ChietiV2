

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager, user, category


# Create your tests here.
if __name__ == '__main__':
	om=orderManager.objects.filter(id=1)
	if not om: #no exist
		om=orderManager()
		om.save()
	
	User.objects.get(email='fede@f.com')
	