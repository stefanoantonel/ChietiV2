from chieti.models import product

from django.utils import timezone
#from chieti.model.order import order
if __name__ == '__main__':
    #===========================================================================
    # prod=product(measureUnit="Kg",pub_date=timezone.now(),salePrice=12,name="manzana")
    # prod.save()
    # prod=product(measureUnit="Kg",pub_date=timezone.now(),salePrice=10,name="peras")
    # prod.save()
    # prod=product(measureUnit="Kg",pub_date=timezone.now(),salePrice=9,name="zanahoria")
    # prod.save()
    # prod=product(measureUnit="Kg",pub_date=timezone.now(),salePrice=4,name="zanahoria")
    # prod.save()
    # iw=user(1,2,3,4,'pepe',2)
    # prod.um=iw
    # prod.save()
    # r=product.objects.filter(um=iw)
    # 
    # print product.clean(prod)
    # 
    # u=product.objects.filter(salePrice=4)
    # for i in u:
    #     print i.name
    # u=product.objects.get(id=22)
    # print u.name
    #===========================================================================
    pr=product.objects.filter(name="di")
    for i in pr:
        print i.salePrice
    pass
