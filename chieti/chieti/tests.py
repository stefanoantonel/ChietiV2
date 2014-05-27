
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager, user, category
from django.db.models.base import Empty


# Create your tests here.
if __name__ == '__main__':
	user1 = authenticate(username='flor', password='12')
	print user1
	
	