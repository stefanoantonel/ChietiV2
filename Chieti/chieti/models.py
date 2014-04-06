from django.db import models

from chieti.user import user
# Create your models here.
class product(models.Model):
    measureUnit = models.CharField(max_length=22)
    pub_date = models.DateTimeField('date published')
    salePrice=models.DecimalField(max_digits=7, decimal_places=2)
    name=models.CharField(max_length=50)
    u=models.user

#===============================================================================
#     class Poll(models.Model):
#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
# 
#     class Choice(models.Model):
#     poll = models.ForeignKey(Poll)
#     choice = models.CharField(max_length=200)
#     votes = models.IntegerField()
#===============================================================================
