<<<<<<< HEAD

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager, user, category
from django.db.models.base import Empty


# Create your tests here.
if __name__ == '__main__':
	user1 = authenticate(username='flor', password='12')
	print user1
	
=======

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

from chieti.models import order, product, item, orderManager, user, category


# Create your tests here.
if __name__ == '__main__':
	p=product.objects.all()
	print p
	print ('pepe')
>>>>>>> 453716cc4cbe205ba1fe17f7371bf28a0475d658
	