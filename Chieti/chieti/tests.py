from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models.base import Model

from chieti.models import order, product


# Create your tests here.
if __name__ == '__main__':
#===============================================================================
# 	select productFK_id,sum(quantity) from (
# select * from chieti_item
# union
# select * from chieti_itemPromo) as p
# group by productFK_id
#===============================================================================

	
	a=product.objects.all()
	pass