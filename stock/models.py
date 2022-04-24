from django.db import models

from brands import models as bm

# Create your models here.
class Brand(models.Model):
    CATEGORY = (
        ('L','Liquor'),
        ('B','Beer'),
        ('M','Misclenious'),
    )
    ncode = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=30)
    scode = models.CharField(max_length=10,unique=True, null=True, blank=True)
    type = models.CharField(max_length=100,choices=CATEGORY)
    price = models.IntegerField()
    qty = models.IntegerField()

    def __str__(self):
        return self.name


class Stock(models.Model):
    date = models.DateField()
    brand = models.ForeignKey(bm.Brand,on_delete=models.CASCADE)
    obal= models.IntegerField()

class Receits(models.Model):
    date =models.DateField()
    brand = models.ForeignKey(bm.Brand,on_delete=models.CASCADE)
    qty= models.IntegerField()
