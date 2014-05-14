from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from chieti.models import orderManager, item, order


# Create your tests here.
if __name__ == '__main__':
	orders=item.objects.all()
	order1=order.objects.filter(getItem=orders)
	
	print order1
	
	