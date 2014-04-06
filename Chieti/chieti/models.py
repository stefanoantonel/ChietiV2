from django.db import models

# Create your models here.
class product(models.Model):
    measureUnit = models.CharField(max_length=22)
    pub_date = models.DateTimeField('date published')
    salePrice=models.DecimalField(max_digits=7, decimal_places=2)
    name=models.CharField(max_length=50)



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
