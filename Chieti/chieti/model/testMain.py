from chieti.models import product
from chieti.user import user
from django.utils import timezone
#from chieti.model.order import order
if __name__ == '__main__':
    prod=product(measureUnit="Kg",pub_date=timezone.now(),salePrice=12,name="manzana")
    prod.save()
    print prod.salePrice,prod.id
    print product.objects.all()
    
    us=user(12,33,11,34,33,1)
    prod.u=us
    prod.save()
    
    w=product.objects.filter(u=us)
    print w
    pass
