from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models.base import Model

from chieti.models import order, product, item


# Create your tests here.
if __name__ == '__main__':
#===============================================================================
# 	select productFK_id,sum(quantity) from (
# select * from chieti_item
# union
# select * from chieti_itemPromo) as p
# group by productFK_id
#===============================================================================
	items=item.objects.all()
	orders=order.objects.filter(getItem=items,delivered='false').distinct() #if item is in order, order is not empty
	print orders